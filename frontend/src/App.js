import React from 'react'
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom'
import { Link } from 'react-router-dom'

function App() {
  return (
    <>
    <Router>
      <Navbar />
      <Routes>
        <Route path="/" element={<Home />} />
      </Routes>
      <footer className="footer column is-narrow">
        <div className="box content has-text-centered">
         
          <br />
          <div className="content has-text-centered ">
            <p>
              <strong>Firesell.com</strong> proudly developed by
              <Link to="https://github.com/dancfc84" className=""> Dimitar Vidolov</Link>,
              as part of Software Engineering Immersive 23 at
              <Link to="https://generalassemb.ly" className=""> General Assembly</Link>.
            </p>
          </div>
        </div>
      </footer>
    </Router>
  </>
  )
}

export default App
