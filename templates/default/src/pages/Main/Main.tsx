import React, { useEffect, useState } from "react";
import axios from "axios";
import { URL_API, URL_DATALIST } from "../../constants/Urls";
import * as Styled from "./Main.style";

const Main = () => {
  const [datalist, setDatalist] = useState<{name: string; type: string;}[]>([]);
  const [output, setOutput] = useState<string>("");

  useEffect(() => {
    const request = {
      url: URL_DATALIST,
      method: "GET",
      headers: {
        "Accept": "application/json",
        "Content-Type": "application/json;charset=utf-8",
      },
    };
    axios(request)
      .then(response => {
        setDatalist(response.data);
      });
  }, []);

  const handleSubmit = (event: React.FormEvent<HTMLFormElement>) => {
    event.preventDefault();

    const formData = new FormData(event.currentTarget);
    const request = {
      url: URL_API,
      method: "POST",
      headers: {
        "Accept": "application/json",
        "Content-Type": "multipart/form-data",
      },
      data: formData,
    };
    axios(request)
      .then(response => {
        setOutput(response.data.output);
      })
  };

  return (
    <Styled.Container>
      <h1>Input inference parameters</h1>

      <form onSubmit={handleSubmit}>
        {datalist.map(item =>
          <div key={item.name}>
            <label htmlFor={item.name}>{item.name}: </label>
            <input id={item.name} name={item.name} type="text" />
          </div>
        )}
        <button type="submit">Submit</button>
      </form>

      {output.length > 0 &&
        <div>
          <h1>Inference result:</h1>
          <p>{output}</p>
        </div>
      }
    </Styled.Container>
  )
};

export default Main;
