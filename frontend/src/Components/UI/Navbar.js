// import logoFile from '../../assets/logo.ico'
import { NavLink } from "react-router-dom"
import React from "react"
import { useLocation } from "react-router-dom";


export default function Navbar() {
  const location = useLocation()
  const [isLoggedIn, setIsLoggedIn] = React.useState(Boolean(localStorage.getItem("loggedIn")))
  
  
  React.useEffect(() => {
    setIsLoggedIn(Boolean(localStorage.getItem("loggedIn")))
  }, [location])

  function Logout() {
    window.localStorage.clear()
    setIsLoggedIn(false)
  }


  return (
    <>
      <header className={styles.nav_container}>
        <nav >
          <div className="container-nav ">
            <div className="navbar-brand">
              <NavLink to="/"><img className="logo image image is-128x128 p-1 mx-5" src={logoFile} /></NavLink>
              <NavLink to="/newsfeed" className={`navbar-item is-size-4 has-text-weight-bold ml-3 ${}`}>
                Products
              </NavLink>
              {isLoggedIn && <NavLink to="/" onClick={NavbarChange} className={`navbar-item is-size-4 has-text-weight-bold ml-3 ${}`}>
                Logout
              </NavLink>}
            </div>
          </div>
        </nav>
      </header>
    </>
  )
}



