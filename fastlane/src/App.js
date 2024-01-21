import ReactDOM from "react-dom/client";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import Layout from "./Layout";
import HomePage from "./HomePage";
import CarInfo from "./CarInfo";
import UserInfo from "./UserInfo";
import Booking from "./Booking";

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Layout />}>
          <Route index element={<HomePage />} />
          <Route path="Booking" element={<Booking />} />
          <Route path="CarInfo" element={<CarInfo />} />
          <Route path="UserInfo" element={<UserInfo />} />
        </Route>
      </Routes>
    </BrowserRouter>
  );
}

const root = ReactDOM.createRoot(document.getElementById("root"));
root.render(<App />);

export default App;
