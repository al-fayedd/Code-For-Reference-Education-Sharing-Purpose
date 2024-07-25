import React from "react";
import "./Package.css"; // Import your CSS file for additional styling

function Package() {
  const packages = [
    {
      id: 1,
      title: "Gardening Services",
      description: "Hire villagers to tend to your garden and maintain plants.",
      price: "RM20 per hour",
      image:
        "https://cdn2.iconfinder.com/data/icons/gardening-and-pet-care/64/Regular_Garden_Service-512.png",
      // Add a `style` object to control the image size
      style: {
        width: "150px",
        height: "150px",
        objectFit: "cover", // Maintain aspect ratio and cover the area
        borderRadius: "50%", // Optional: Rounded corners
      },
    },
    {
      id: 2,
      title: "Handyman Services",
      description: "Get help with repairs and odd jobs around the house.",
      price: "Prices vary based on job",
      image:
        "https://png.pngtree.com/png-vector/20220517/ourmid/pngtree-handyman-worker-color-icon-vector-png-image_4660998.png", // Example image link (replace with actual image link)
      style: {
        width: "150px",
        height: "150px",
        objectFit: "cover", // Maintain aspect ratio and cover the area
        borderRadius: "50%", // Optional: Rounded corners
      },
    },
    {
      id: 3,
      title: "Crafting Workshops",
      description: "Learn traditional crafting skills from skilled villagers.",
      price: "RM30 per session",
      image: "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR6bxivghw2DGqxVxTahEx-lDcuVoB3fEtVmg&s", // Example image link (replace with actual image link)
      style: {
        width: "150px",
        height: "150px",
        objectFit: "cover", // Maintain aspect ratio and cover the area
        borderRadius: "50%", // Optional: Rounded corners
      },
    },
    {
      id: 4,
      title: "Visit Village Experience",
      description: "Experience the culture and hospitality of our village.",
      price: "RM50 per person",
      image: "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRVEQHScnqx7UhYPqsr-4i9UH2Y7RGl3JKr4A&s", // Example image link (replace with actual image link)
      style: {
        width: "150px",
        height: "150px",
        objectFit: "cover",
        borderRadius: "50%",
      },
    },
  ];

  return (
    <div className="package-container">
      <h1>Our Packages</h1>
      <div className="packages">
        {packages.map((pkg) => (
          <div key={pkg.id} className="package">
            <img
              src={pkg.image}
              alt={pkg.title}
              className="package-image"
              style={pkg.style}
            />
            <h2>{pkg.title}</h2>
            <p>{pkg.description}</p>
            <p className="price">{pkg.price}</p>
          </div>
        ))}
      </div>
    </div>
  );
}

export default Package;
