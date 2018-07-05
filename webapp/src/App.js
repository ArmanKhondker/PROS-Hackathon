import React, { Component } from 'react'
import './App.css'

import axios from 'axios'

class App extends Component {
  constructor () {
    super()
    this.state = {
      model: '',
      zoomW: '',
      releaseDate: '',
      estimatedPrice: '',
      maxRes: '',
      lowRes: '',
      effPix: '',
      zoomT: '',
      normalFocus: '',
      macroFocus: '',
      storage: '',
      weight: '',
      dimension: ''
      
    }

    // this.handleClick = this.handleClick.bind(this);
    this.handleModelChange = this.handleModelChange.bind(this);
    this.handleSumbitClick = this.handleSumbitClick.bind(this);
    this.handleZoomWChange = this.handleZoomWChange.bind(this);
    this.handleDateChange = this.handleDateChange.bind(this);
    this.handlePriceChange = this.handlePriceChange.bind(this);
    this.handleMaxResChange = this.handleMaxResChange.bind(this);
    this.handleLowResChange = this.handleLowResChange.bind(this);
    this.handlePixelChange = this.handlePixelChange.bind(this);
    this.handleZoomTChange = this.handleZoomTChange.bind(this);
    this.handleNormalFocusChange = this.handleNormalFocusChange.bind(this);
    this.handleMacroFocusChange = this.handleMacroFocusChange.bind(this);
    this.handleStorageChange = this.handleStorageChange.bind(this);
    this.handleWeightChange = this.handleWeightChange.bind(this);
    this.handleDimensionChange = this.handleDimensionChange.bind(this);
  }

  handleModelChange = e => {
    this.setState({model:e.target.value});
  }

  handlePixelChange = e => {
    this.setState({effPix:e.target.value});
  }

  handleMaxResChange = e => {
    this.setState({maxRes:e.target.value});
  }

  handleLowResChange = e => {
    this.setState({lowRes:e.target.value});
  }

  handleZoomWChange = e => {
    this.setState({zoomW:e.target.value});
  }

  handleZoomTChange = e => {
    this.setState({zoomT:e.target.value});
  }

  handleDateChange = e => {
    this.setState({releaseDate:e.target.value});
  }

  handlePriceChange = e => {
    this.setState({estimatedPrice:e.target.value});
  }

  handleNormalFocusChange = e => {
    this.setState({normalFocus:e.target.value});
  }

  handleMacroFocusChange = e => {
    this.setState({macroFocus:e.target.value});
  }

  handleStorageChange = e => {
    this.setState({storage:e.target.value});
  }

  handleWeightChange = e => {
    this.setState({weight:e.target.value});
  }

  handleDimensionChange = e => {
    this.setState({dimension:e.target.value});
  }


  hideView () {
    console.log("test");
  }

  handleSumbitClick = () => {
    const inputValues = {
      model: this.state.model,
      zoomW: this.state.zoomW,
      releaseDate: this.state.releaseDate,
      maxRes: this.state.maxRes,
      lowRes: this.state.lowRes,
      effPix: this.state.effPix,
      zoomT: this.state.zoomT,
      normalFocus: this.state.normalFocus,
      macroFocus: this.state.macroFocus,
      storage: this.state.storage,
      weight: this.state.weight,
      dimension: this.state.dimension
    }

    axios.get('http://localhost:5000', {
      params: inputValues
    }).then(response => this.setState({estimatedPrice: response.data.price}))
    //get/post with params
    // console.log(this.state.model);
    // console.log(this.state.zoomW);
    // console.log(this.state.releaseDate);
    // console.log(this.state.effPix);
    // console.log(this.state.dimension);
    // console.log(this.state.lowRes);
    // console.log(this.state.macroFocus);
    // console.log(this.state.maxRes);
    // console.log(this.state.normalFocus);
    // console.log(this.state.storage);
    // console.log(this.state.weight);
    // console.log(this.state.zoomT);

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
                <option value="select_model">Select Brand</option>
                <option value="Nikon">Nikon</option>
                <option value="Canon">Canon</option>
                <option value="Sony">Sony</option>
            </select>

            <select name="choose_release_date" className = "dropdownbox" onChange={this.handleDateChange}>
                <option value="select_release_date">Select Release Date</option>
                <option value="1997">1997</option>
                <option value="2000">2000</option>
                <option value="2004">2004</option>
            </select>

            <select name="choose_max_res" className = "dropdownbox" onChange={this.handleMaxResChange}>
                <option value="select_max_res">Select Maximum Resolution</option>
                <option value="1024.0">1024.0</option>
                <option value="1152.0">1152.0</option>
                <option value="1600">1600</option>
            </select>

            <select name="choose_low_res" className = "dropdownbox" onChange={this.handleLowResChange}>
                <option value="select_low_res">Select Lowest Resolution</option>
                <option value="640.0">640.0</option>
                <option value="1024.0">1024.0</option>
                <option value="1600">1600</option>
            </select>

            <div className = "divider"></div>

             <select name="choose_eff_pix" className = "dropdownbox" onChange={this.handlePixelChange}>
                <option value="select_eff_pix">Select Effective Pixels</option>
                <option value="0.0">0.0</option>
                <option value="1.0">1.0</option>
                <option value="3.0">3.0</option>
            </select>

            <select name="choose_zoom_W" className = "dropdownbox" onChange={this.handleZoomWChange}>
                <option value="select_zoom">Select Zoom wide (W)</option>
                <option value="38.0">38.0</option>
                <option value="45.0">45.0</option>
                <option value="50.0">50.0</option>
            </select>

            <select name="choose_zoom_T" className = "dropdownbox" onChange={this.handleZoomTChange}>
                <option value="select_zoom">Select Zoom tele (T)</option>
                <option value="114.0">114.0</option>
                <option value="51.0">51.0</option>
                <option value="102.0">102.0</option>
            </select>

            <select name="choose_normal_focus" className = "dropdownbox" onChange={this.handleNormalFocusChange}>
                <option value="select_normal_focus">Select Normal Focus Range</option>
                <option value="70.0">70.0</option>
                <option value="50.0">50.0</option>
                <option value="40.0">40.0</option>
            </select>

            <select name="choose_macro_focus" className = "dropdownbox" onChange={this.handleMacroFocusChange}>
                <option value="select_macro_focus">Select Macro Focus Range</option>
                <option value="20.0">20.0</option>
                <option value="10.0">10.0</option>
                <option value="40.0">40.0</option>
            </select>

            <div className = "divider"></div>

            <select name="choose_storage" className = "dropdownbox" onChange={this.handleStorageChange}>
                <option value="select_storage">Select Storage Included</option>
                <option value="32.0">32.0</option>
                <option value="16.0">16.0</option>
                <option value="40.0">40.0</option>
            </select>

            <select name="choose_weight" className = "dropdownbox" onChange={this.handleWeightChange}>
                <option value="select_weight">Select Weight</option>
                <option value="420.0">420.0</option>
                <option value="300.0">300.0</option>
                <option value="270.0">270.0</option>
            </select>

            <select name="choose_dimensions" className = "dropdownbox" onChange={this.handleDimensionChange}>
                <option value="select_dimension">Select Dimensions</option>
                <option value="95.0">95.0</option>
                <option value="158.0">158.0</option>
                <option value="110.0">110.0</option>
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
