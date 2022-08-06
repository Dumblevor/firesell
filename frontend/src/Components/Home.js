import React, { useState, useEffect } from 'react'
import baseUrl from "../config.js"
import axios from 'axios'
import Product from './products/Product.js'
import { useLocation } from "react-router-dom";

export default function Home() {
  const location = useLocation()

  const [allProducts, setAllProducts] = useState([])
  const [search, setSearch] = React.useState("")


  const getProductData = async () => {
    const { data } = await axios.get(`${baseUrl}/allproducts`)
    setAllProducts(data)
    data && console.log(data)
  }


  useEffect(() => {
    getProductData()
    const productInterval = setInterval(() => {
      getProductData()
    }, 1000);
    return () => {clearInterval(productInterval)}
  }, [])

  function productFilter() {
    return allProducts.filter((product) => {
      return (
        product.name.toLowerCase().includes(search.toLowerCase())
      )
    }
    )
  }

  return (
    <>
      {
        allProducts ? productFilter().map((productData, index) => {
          return <div key={index} className="">
            <Product
              {...productData} />
          </div>

        }
        ) : < p > Loading products, please wait. </p >}
    </>
  )
}
