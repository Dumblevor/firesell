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
        <Card sx={{ maxWidth: 345 }}>

          <div>Logo</div>
          <CardContent>
            <Link to={`/product/${productData.id}`}>
              <Typography gutterBottom variant="h5" component="div">{productData.name}</Typography>
            </Link>

            <CardMedia
              component="img"
              height="140"
              image="/static/images/cards/contemplative-reptile.jpg"
              alt="green iguana"
            />
            <div className="subtitle is-6">sold by: (seller id) - {productData.product_owner_ID}</div>
            <Typography variant="body2" color="text.secondary">{productData.description}</Typography>

          </CardContent>

          <Stack spacing={1}>
            {/* <Rating name="half-rating" defaultValue={2.5} precision={0.5} /> */}
            <Rating name="half-rating-read" defaultValue={2.5} precision={0.5} readOnly />
          </Stack>

          <div>€ {productData.price}</div>

          <CardActions>
            <Button component={ Link } variant="outlined" to={`/checkout/${productData.id}`}>
              Purchase now</Button>
          </CardActions>
        </Card >
        : <p>Loading product</p>
      }
    </>
  )

}