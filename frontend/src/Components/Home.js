import React, { useState, useEffect } from 'react'
import baseUrl from "../../config"


export default function Home() {
  const [allProducts, setAllProducts] = useState([])


  const getProductData = async () => {
    const { data } = await axios.get(`${baseUrl}/allproducts/`)
    setAllProducts(data)
  }
}

useEffect(() => {
  getProductData()
  setInterval(() => {
    getProductData()
  }, 1000);
}, [])

function productFilter() {
  return allProducts.filter((product) => {
    return (
      product.toLowerCase().includes(search.toLowerCase())
      )
  }
  )
}


return (

  {allProducts ? productFilter().map((product, index) => {
    return <div key={index} className="">
      <ProductElement
        {...product}
    </div>
  }
  ) : <p> Loading products, please wait. </p>}
)