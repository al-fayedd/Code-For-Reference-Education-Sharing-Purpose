import React from "react";

function Homepage() {
  return (
    <div className="container">
      <section className="jumbotron text-center">
        <div className="container">
          <img src="rumahkampung.png" alt="HomepageImage" className="img-fluid mb-4" style={{ height: '200px' }}/>
          <h1 className="display-4">Welcome to Kerja Kampung</h1>
          <p className="lead">
            Empowering villagers through local services and opportunities.
          </p>
          <hr className="my-4" />
          <p>
            Explore our community, learn about our services, and connect with
            us!
          </p>
        </div>
      </section>
    </div>
  );
}

export default Homepage;
