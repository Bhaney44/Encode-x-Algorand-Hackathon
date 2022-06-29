import { useSelector } from "react-redux";
// import Schedule from "./schedule";
import { NavLink, Route, Routes } from "react-router-dom";
import TopNavigationBar from "./statics/TopNavigationBar";
import Compliance from "./components/Compliance";

const MainPage = () => {
  const darkTheme = useSelector((state) => state.status.darkTheme);

  return (
    <main
      className={`${
        darkTheme ? "dark_theme big_screen" : "light_theme big_screen"
      }`}
      id="main_main"
    >
      <div
        style={{
          top: 0,
          left: 0,
          right: 0,
          bottom: 0,
          content: "",
          width: "100%",
          height: "100%",
          opacity: darkTheme ? 0.008 : 0.018,
          position: "fixed",
          pointerEvents: "none",
          // backgroundColor: "#757589",
          // opacity: 0.3;
          // backgroundImage: radial-gradient(circle at center center, #2d2d30, #757589), repeating-radial-gradient(circle at center center, #2d2d30, #2d2d30, 10px, transparent 20px, transparent 10px),
          // background-blend-mode: multiply;
          // background: `url("./img/background${darkTheme ? "2" : ""}.svg")`,

        }}
        className="compliance__background"
      />

      <TopNavigationBar darkTheme={darkTheme} NavLink={NavLink} />

      <Routes>
      
        {/* <Route path="/schedule" element={<Schedule />} /> */}
        
        <Route path="/" element={<Compliance/>}  />
      </Routes>

      
       
  
    </main>
  );
};

export default MainPage;
