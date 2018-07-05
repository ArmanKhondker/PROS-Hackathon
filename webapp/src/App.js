import React, { Component } from 'react'
import './App.css'

import axios from 'axios'

class App extends Component {
  constructor () {
    super()
    this.state = {
      // username: '',
      model: '',
      zoom: '',
      releaseDate: '',
      estimatedPrice: ''
      
    }

    // this.handleClick = this.handleClick.bind(this);
    this.handleModelChange = this.handleModelChange.bind(this);
    this.handleSumbitClick = this.handleSumbitClick.bind(this);
    this.handleZoomChange = this.handleZoomChange.bind(this);
    this.handleDateChange = this.handleDateChange.bind(this);
    this.handlePriceChange = this.handlePriceChange.bind(this);
  }

  handleModelChange = e => {
    this.setState({model:e.target.value});
  }

  handleZoomChange = e => {
    this.setState({zoom:e.target.value});
  }

  handleDateChange = e => {
    this.setState({releaseDate:e.target.value});
  }

  handlePriceChange = e => {
    this.setState({estimatedPrice:e.target.value});
  }

  // handleClick () {
  //   axios.get('https://api.github.com/users/youcanjewett')
  //     .then(response => this.setState({username: response.data.name}))
  // }

  hideView () {
    console.log("test");
  }

  handleSumbitClick = () => {
    const inputValues = {
      model: this.state.model,
      zoom: this.state.zoom,
      releaseDate: this.state.releaseDate
    }

    axios.get('http://localhost:5000/?model=MODEL&releaseDate=RELEASE&zoom=ZOOM').then(response => this.setState({estimatedPrice: response.data.price}))
    //get/post with params
    // console.log(this.state.model);
    // console.log(this.state.zoom);
    // console.log(this.state.releaseDate);
  }

  render () {
    
    return (
      <div>
        <div className = "top"></div>
        <div className ="enter_data">
          Product to Price: Camera 
        </div>
      
         
        <div className = "product_inputs">
            Please select product details:
            <div className = "dropdowns">

            <select name="choose_model" className = "dropdownbox"  onChange={this.handleModelChange}>
                <option value="select_model">Select Model</option>
                <option value="Model A">Model A</option>
            </select>

            <select name="choose_release_date" className = "dropdownbox" onChange={this.handleDateChange}>
                <option value="select_release_date">Select Release Date</option>
                <option value="Date A">Date A</option>
            </select>

            <select name="choose_zoom" className = "dropdownbox" onChange={this.handleZoomChange}>
                <option value="select_zoom">Select Zoom</option>
                <option value="Zoom A">Zoom A</option>
            </select>

            <button className = "getPriceBtn" onClick={this.handleSumbitClick} >Price this item</button>
            </div>
        </div>

        <div className = "price_container" ></div>
           <div className = "pricing">
              <div className = "price_text">The suggested price for this product is:</div>
        </div>  

        <div className = "pricing">
            <div className = "price_est">${this.state.estimatedPrice}</div>
        </div>

      {/* <div className='button__container'>
        <button className='button' onClick={this.handleClick}>Click Me</button>
        <p>{this.state.username}</p>
      </div> */}
      </div>
    )
  }
}
export default App
