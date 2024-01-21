import { Outlet, Link } from "react-router-dom";

const Layout = () => {
  return (
    <>
      <nav>
        <ul>
          <li>
            <Link to="/">Home</Link>
          </li>
          <li>
            <Link to="/CarInfo">Car Information</Link>
          </li>
          <li>
            <Link to="/Booking">Booking</Link>
          </li>
          <li>
            <Link to="/UserInfo">User Information</Link>
          </li>
        </ul>
      </nav>
      <Outlet />
    </>
  );
};

export default Layout;
