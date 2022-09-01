import React from 'react'
import { NavLink,Link } from "react-router-dom";
import './Navbar.css'
import $ from 'jquery';

function Navbar() {
    window.addEventListener('scroll', () => {
        if(window.scrollY > 20){
            $('.nav').addClass("nav-sticky");
            $('.nav-mobile').addClass("nav-mobile-sticky");
        }else{
            $('.nav').removeClass("nav-sticky");
            $('.nav-mobile').removeClass("nav-mobile-sticky");
        }
        if(window.scrollY > 500){
            $('.scroll-up-btn i').addClass("show");
        }else{
            $('.scroll-up-btn i').removeClass("show");
        }
      });

    const toggle = () =>{
        $('.nav').toggleClass("nav_active");
        $('.nav-mobile-btn span i').toggleClass("btn_active");
    }
    const navclose = () =>{
        $('.nav').toggleClass("nav_active");
        $('.nav-mobile-btn span i').toggleClass("btn_active");
    }
    return (
        <>
            <nav>
                <div className="nav">
                <Link to="/"><h2>Markhor<span>Softs</span></h2></Link>
                <ul>
                    <li><NavLink to="/" activeclassname="active" onClick={navclose}><i className='fas fa-home' ></i>Home</NavLink></li>
                    <li><NavLink to="/about" activeclassname="active" onClick={navclose}><i className='fas fa-user' ></i>About</NavLink></li>
                    <li><NavLink to="/services" activeclassname="active" onClick={navclose}><i className='fas fa-cogs' ></i>Services</NavLink></li>
                    <li><NavLink to="/blogs" activeclassname="active" onClick={navclose}><i className='fas fa-pen-to-square' ></i>Blogs</NavLink></li>
                    <li><NavLink to="/teams" activeclassname="active" onClick={navclose}><i className='fas fa-users' ></i>Teams</NavLink></li>
                    <li><NavLink to="/contact" activeclassname="active" onClick={navclose}><i className='fas fa-phone' ></i>Contact us</NavLink></li>
                </ul>
                </div>
                <div className="nav-mobile">
                    <Link to="/"><h2>Markhor<span>Softs</span></h2></Link>
                    <div className="nav-mobile-btn" onClick={toggle}>
                    <span><i className='fas fa-bars'></i></span>
                    </div>
                </div>
            </nav>
            <div className='nav-space'></div>
        </>
    )
}

export default Navbar
