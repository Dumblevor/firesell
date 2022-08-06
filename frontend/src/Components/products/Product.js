import { Link } from "react-router-dom"
import * as React from 'react';
import Rating from '@mui/material/Rating';
import Stack from '@mui/material/Stack';
import Card from '@mui/material/Card';
import CardActions from '@mui/material/CardActions';
import CardContent from '@mui/material/CardContent';
import CardMedia from '@mui/material/CardMedia';
import Button from '@mui/material/Button';
import Typography from '@mui/material/Typography';
import ButtonGroup from '@mui/material/ButtonGroup';




export default function Product(props) {



  return (
    <Card sx={{ maxWidth: 345 }}>


      <div>Logo</div>
      <CardContent>
        <Link to={`/product/${props.id}`}>
          <Typography gutterBottom variant="h5" component="div">{props.name}</Typography>
        </Link>

        <CardMedia
          component="img"
          height="140"
          image="/static/images/cards/contemplative-reptile.jpg"
          alt="green iguana"
        />
        <div className="subtitle is-6">sold by: (seller id) - {props.product_owner_ID}</div>
        <Typography variant="body2" color="text.secondary">{props.description}</Typography>

      </CardContent>

      <Stack spacing={1}>
        {/* <Rating name="half-rating" defaultValue={2.5} precision={0.5} /> */}
        <Rating name="half-rating-read" defaultValue={2.5} precision={0.5} readOnly />
      </Stack>

      <div>€ {props.price}</div>

      <CardActions>
        <ButtonGroup variant="outlined" aria-label="outlined button group">
          <Button variant="outlined" size="small">Add to cart</Button>
          <Button variatn="" size="small">Purchase now</Button>
        </ButtonGroup>
      </CardActions>
    </Card >
  )
}