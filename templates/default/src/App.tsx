import { BrowserRouter, Routes, Route } from 'react-router-dom';
import { TopNav } from "./components/common";
import * as Screen from "./pages";

function App() {
  return (
    <BrowserRouter>
      <TopNav />
      <Routes>
        <Route path="/" element={<Screen.Main />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;
