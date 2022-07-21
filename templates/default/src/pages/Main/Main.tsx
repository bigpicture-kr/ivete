import { useEffect, useState } from "react";
import axios from "axios";
import { URL_DATALIST } from "../../constants/Urls";
import * as Styled from "./Main.style";

const Main = () => {
  const [datalist, setDatalist] = useState<{name: string; type: string;}[]>([]);

  useEffect(() => {
    const request = {
      url: URL_DATALIST,
      method: "GET",
      header: {
        "Accept": "application/json",
        "Content-Type": "application/json;charset=utf-8",
      },
    };
    axios(request)
      .then(response => {
        setDatalist(response.data);
      });
  }, []);

  return (
    <Styled.Container>
      <h1>Input inference parameters</h1>
      {datalist.map(item =>
        <div key={item.name}>
          <span>{item.name}: </span>
          <input name={item.name} type="text" />
        </div>
      )}
      <button type="submit">Submit</button>
    </Styled.Container>
  )
};

export default Main;
