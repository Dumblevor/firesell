// import logoFile from '../../assets/logo.ico'
import { NavLink, Link } from "react-router-dom"
import React, { useState, useEffect } from 'react'
import { useLocation } from "react-router-dom";
import Button from '@mui/material/Button';
import ButtonGroup from '@mui/material/ButtonGroup';


export default function Navbar() {
  const location = useLocation()
  const [isLoggedIn, setIsLoggedIn] = React.useState(Boolean(localStorage.getItem("loggedIn")))


  useEffect(() => {
    setIsLoggedIn(Boolean(localStorage.getItem("loggedIn")))
  }, [isLoggedIn, location])

  function Logout() {
    window.localStorage.clear()
    setIsLoggedIn(false)
  }


  return (
    <>
      <header>
        <nav >
          <div className="container-navbar ">
            <div className="navbar-brand"></div>
            <div className="navbar-menu">
              <div className="navbar-start">
                <NavLink to="/" className="navbar-item is-size-4 has-text-weight-bold ml-3">
                  Products
                </NavLink>
              </div>
              <div className="navbar-end">
                <ButtonGroup variant="outlined" aria-label="outlined button group">

                  {!isLoggedIn && <Button component={NavLink} to="/login" variant="outlined">
                    Login
                  </Button>}
                  {!isLoggedIn && <Button component={NavLink} to="/register" variant="outlined" >
                    Register
                  </Button>}
                  {isLoggedIn && <Button component={NavLink} to="/" onClick={Logout} variant="outlined">
                    Logout
                  </Button>}

                </ButtonGroup>
              </div>
            </div>
          </div>
        </nav>
      </header>
    </>
  )
}



