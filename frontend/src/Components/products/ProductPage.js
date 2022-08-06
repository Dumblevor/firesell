import React, { useState, useEffect } from 'react'
import { Link, useNavigate, useParams } from "react-router-dom"
import axios from "axios"
import baseUrl from "../../config"



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
  })


  return (
    <>
      {productData ?
        <div className="card">

          <Link to={`/product/${productData.id}`}>
            <div>Logo</div>
            <div className="title is-4">{productData.name}</div>
          </Link>

          <div className="subtitle is-6">
            sold by: (seller id) - {productData.product_owner_ID}
          </div>

          <div>{productData.description}</div>

          <div>Preview image</div>

          <div>Rating:{productData.rating}</div>

          <div>€ {productData.price}</div>

        </div>
        : <p>Loading product</p>
      }
    </>
  )

}