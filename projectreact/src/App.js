import React from 'react'
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom'
import Homepage from './Homepage/Homepage'
import About from './About/About'
import Package from './Package/Package'
import Contactus from './ContactUs/Contactus'
import Navbar from './Navbar/Navbar'
import Footer from './Footer/Footer'

function App() {
  return (
    <div>
      <Router>
        <Navbar/>
        <Routes>
          <Route path='/' element={<Homepage/>}/>
          <Route path="/about" element={<About />} />
          <Route path="/package" element={<Package/>} />
          <Route path="/contactus" element={<Contactus />} />
        </Routes>
        <Footer/>
      </Router>
    </div>
  )
}

export default App