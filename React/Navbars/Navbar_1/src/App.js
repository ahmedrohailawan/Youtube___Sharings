import './App.css';
import * as React from "react";
import { Routes, Route} from "react-router-dom";
import Home from "./pages/Home/Home"
import About from "./pages/About/About"
import Service from "./pages/Service/Service"
import Blog from "./pages/Blog/Blog"
import Team from "./pages/Team/Team"
import Contact from "./pages/Contact/Contact"
import Navbar from './components/Navbar/Navbar'

function App() {
  return (
    <>
      <Navbar/>
      <Routes>
        <Route exact path="/" element={<Home />} />
        <Route exact path="/about" element={<About />} />
        <Route exact path="/services" element={<Service />} />
        <Route exact path="/blogs" element={<Blog />} />
        <Route exact path="/teams" element={<Team />} />
        <Route exact path="/contact" element={<Contact />} />
      </Routes>
      
    </>
  );
}
export default App;
