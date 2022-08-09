import React, { useState, useEffect } from 'react'
import { Link, useNavigate, useParams } from "react-router-dom"
import axios from "axios"
import baseUrl from "../../config"
import Rating from '@mui/material/Rating';
import Stack from '@mui/material/Stack';
import Card from '@mui/material/Card';
import CardActions from '@mui/material/CardActions';
import CardContent from '@mui/material/CardContent';
import CardMedia from '@mui/material/CardMedia';
import Button from '@mui/material/Button';
import Typography from '@mui/material/Typography';
import Product from './Product.js'


export default function ProductPage() {
  const [productData, setProductData] = useState(undefined)
  const { productID } = useParams()


  useEffect(() => {
    async function fetchOneProduct() {
      fetch(`${baseUrl}/products/${productID}`)
        .then(respo => respo.json())
        .then(data => setProductData(data))
    }
    fetchOneProduct()

  }, [productID])


  function handleAddtoCart() {
    let currentItems = JSON.parse(localStorage.getItem('cartItems'))
    currentItems.push(productID)
    localStorage.setItem('cartItems', JSON.stringify(currentItems))
  }

  return (
    <>
      {productData ?
        <Product
        {...productData} />
        : <p>Loading product</p>
      }
    </>
  )

}