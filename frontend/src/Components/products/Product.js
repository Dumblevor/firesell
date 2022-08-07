import { Link, NavLink} from "react-router-dom"
import * as React from 'react';
import Rating from '@mui/material/Rating';
import Stack from '@mui/material/Stack';
import Card from '@mui/material/Card';
import CardActions from '@mui/material/CardActions';
import CardContent from '@mui/material/CardContent';
import CardMedia from '@mui/material/CardMedia';
import Button from '@mui/material/Button';
import Typography from '@mui/material/Typography';
import { spacing } from '@mui/system'
import Avatar from '@mui/material/Avatar';



export default function Product(props) {


  return (
    <Card sx={{ maxWidth: 345, py: 1, pl: 2 }}>
      <Stack direction="row" spacing={2}>
        <Avatar alt="Remy Sharp" src="/static/images/avatar/1.jpg" />
      </Stack>

      <CardContent >
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

      <Stack spacing={2}>
        {/* <Rating name="half-rating" defaultValue={2.5} precision={0.5} /> */}
        <Rating name="half-rating-read" defaultValue={2.5} precision={0.5} readOnly />
        €{props.price}
      </Stack>

        <Button component={NavLink} sx={{ mx: 1, m: 2 }} variant="outlined" to={`/checkout/${props.id}`}>Purchase now</Button>

    </Card >
  )
}


