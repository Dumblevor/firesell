import React, { useState, useEffect } from 'react'
import baseUrl from "../config.js"
import axios from 'axios'
import { useNavigate } from 'react-router-dom'
import Button from '@mui/material/Button';
import ToggleButton from '@mui/material/ToggleButton';
import ToggleButtonGroup from '@mui/material/ToggleButtonGroup';

export default function Checkout() {

  const [alignment, setAlignment] = React.useState('web');

  const handleChange = (event, newAlignment) => {
    setAlignment(newAlignment);
  };




  return (
    <>

      <ToggleButtonGroup
        color="primary"
        value={alignment}
        exclusive
        onChange={handleChange}
      >
        <ToggleButton value="card">Card</ToggleButton>
        <ToggleButton value="applepay">Apple Pay</ToggleButton>
        <ToggleButton value="paypal">PayPal</ToggleButton>
      </ToggleButtonGroup>
      <Button>Complete Purchaase</Button>

    </>
  )
}