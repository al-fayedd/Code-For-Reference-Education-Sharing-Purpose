import React from "react";

const footerStyle = {
  position: "fixed",
  bottom: 0,
  left: 0,
  width: "100%",
  backgroundColor: "rgba(128, 128, 128, 0.8)", // Grey color with 80% opacity
  textAlign: "center",
  padding: "10px", // Add padding for better visibility
  marginTop: "80px", // Add margin top for space above the footer
};

const textStyle = {
  color: "white",
  fontSize: "15px",
};

function Footer() {
  return (
    <div style={footerStyle}>
      <p style={textStyle}>&copy; 2024 Kerja Kampung. All rights reserved.</p>
    </div>
  );
}

export default Footer;
