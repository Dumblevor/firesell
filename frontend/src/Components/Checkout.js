import React, { useState, useEffect } from 'react'
import baseUrl from "../config.js"
import axios from 'axios'
import { Link, useNavigate, useParams } from "react-router-dom"
import Button from '@mui/material/Button';
import ToggleButton from '@mui/material/ToggleButton';
import ToggleButtonGroup from '@mui/material/ToggleButtonGroup';
import Box from '@mui/material/Box';
import Grid from '@mui/material/Grid';
import Rating from '@mui/material/Rating';
import Stack from '@mui/material/Stack';
import Card from '@mui/material/Card';
import CardContent from '@mui/material/CardContent';
import CardMedia from '@mui/material/CardMedia';
import Typography from '@mui/material/Typography';

export default function Checkout() {
  const navigate = useNavigate()
  const { productID } = useParams()
  const [productData, setProductData] = useState(undefined)
  const [alignment, setAlignment] = React.useState('card');

  const [cardData, setCardData] = useState({
    name: "",
    number: "",
    expiry: "",
    security: "",
  })

  let cartItems = JSON.parse(localStorage.getItem('cartItems'))

  useEffect(() => {
    const fetchOneProduct = async () => {
      const { data } = await axios.get(`${baseUrl}/products/${productID}`)
      setProductData(data)
    }
    fetchOneProduct()
  }, [productID])


  const handleChangeToggle = (event, newAlignment) => {
    setAlignment(newAlignment);
  };

  function handleChange(e) {
    setCardData((prevState) => {
      return {
        ...prevState,
        [e.target.name]: e.target.value,
      }
    })
  }


  async function handleOrderSubmit(e) {
    e.preventDefault()

    try {
      const { response } = await axios.post(`${baseUrl}/neworder`, productID)
      navigate('/sucessfulorder', { state: { productID } })
    } catch (e) {
      console.log(e.response.data)
    }
  }



  return (
    <>
      <Box sx={{ flexGrow: 1 }}>
        <Grid container spacing={2}>
          <Grid item xs={1}></Grid>
          <Grid item xs={6}>
            <ToggleButtonGroup
              color="primary"
              value={alignment}
              exclusive
              onChange={handleChangeToggle}
            >
              <ToggleButton value="card">Card</ToggleButton>
              <ToggleButton value="applepay">Apple Pay</ToggleButton>
              <ToggleButton value="paypal">PayPal</ToggleButton>
            </ToggleButtonGroup>

            <form name="orderForm" onSubmit={handleOrderSubmit}>
              <div >
                <label className="label">Name</label>
                <div>
                  <textarea
                    className="input"
                    type="text"
                    name={'name'}
                    value={cardData.email}
                    onChange={handleChange}
                    placeholder="e.g. Richard Branson"
                  />
                </div>
              </div>
              <div>
                <label className="label">Card number</label>
                <div >
                  <textarea
                    className="input"
                    type="text"
                    name={'number'}
                    value={cardData.number}
                    onChange={handleChange}
                    placeholder="0123 4567 8910 1112"
                  />
                </div>
              </div>
              <div>
                <label className="label">Expiry Date</label>
                <div >
                  <textarea
                    className="input"
                    type="text"
                    name={'expiry'}
                    value={cardData.expiry}
                    onChange={handleChange}
                    placeholder="1222"
                  />
                </div>
              </div>
              <div>
                <label className="label">Security code</label>
                <div >
                  <textarea
                    className="input"
                    type="text"
                    name={'security'}
                    value={cardData.security}
                    onChange={handleChange}
                    placeholder="last 3 digits on the back, e.g. 123"
                  />
                </div>
              </div>
            </form>
          </Grid>


          <Grid item xs={5}>
            {productData ?
              <Card sx={{
                maxWidth: 345, mx: 'auto',
                p: 1,
                m: 1,
                fontSize: '0.875rem',
                fontWeight: '700',
              }} >
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
              </Card>
              : <p> Loading your products</p>}
          </Grid>
          <Grid item xs={8}>
            <Box textAlign='center'>
              <Button variant="contained" type="submit" form="orderForm" onClick={(e) => handleOrderSubmit(e)} color="success">
                Complete Purchase
              </Button>
            </Box>
          </Grid>
        </Grid>
      </Box>
    </>
  )
}