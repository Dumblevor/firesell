import React from 'react'
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom'
import { Link } from 'react-router-dom'
import Home from "./Components//Home"
import Navbar from './Components/UI/Navbar'
import Login from './Components/Login'
import CustomerReg from './Components/CustomerReg'
import ProductPage from './Components/products/ProductPage'

function App() {
  return (
    <>
    <Router>
      <Navbar />
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/login" element={<Login />} />
        <Route path="/register" element={<CustomerReg />} />
        <Route path="/product/:productID" element={<ProductPage />} />
      </Routes>
    </Router>
  </>
  )
}

export default App
