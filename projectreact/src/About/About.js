import React from "react";

function About() {
  return (
    <div className="container">
      <section className="jumbotron text-center">
        <div className="container">
          <h1 className="display-4">About Kerja Kampung</h1>
          <p className="lead">
            Kerja Kampung is dedicated to enhancing the lives of villagers by
            empowering them with sustainable opportunities and support.
          </p>
        </div>
      </section>

      <section className="py-5">
        <div className="container">
          <div className="row">
            <div className="col-lg-6">
              <h2>Our Mission</h2>
              <p>
                Our mission is to create economic opportunities for villagers
                through skill development, employment generation, and community
                empowerment projects.
              </p>
            </div>
            <div className="col-lg-6">
              <h2>Our Vision</h2>
              <p>
                We envision vibrant rural communities where every villager has
                the opportunity to thrive, contributing to a sustainable and
                inclusive society.
              </p>
            </div>
          </div>
        </div>
      </section>

      <section className="py-5 bg-light">
        <div className="container">
          <div className="row">
            <div className="col-lg-6">
              <h2>Our Impact</h2>
          <p className="lead">
            Since our inception in 2024, we have impacted over 1000 villages,
            creating opportunities for hundreds of families.
          </p>
            </div>
            <div className="col-lg-6">
              <h2>Our Values</h2>
              <ul className="list-unstyled">
                <li>- Community Engagement</li>
                <li>- Sustainability</li>
                <li>- Empowerment</li>
                <li>- Integrity</li>
                <li>- Innovation</li>
              </ul>
            </div>
          </div>
        </div>
      </section>

      <section className="text-center py-5">
        <div className="container">
        <h2>Founder's Message</h2>
              <img
                src={"founder.png"}
                alt="Founder"
                className="img-fluid rounded-circle mb-3"
                style={{ maxWidth: "200px" }}
              />
              <p className="lead">
                "Founder's Message: Founder. Meet Hamza, the founder of Kerja
                Kampung. He is dedicated to enhancing village life through
                sustainable development initiatives. His passion for community
                empowerment drives our mission to create lasting impact."
              </p>
        </div>
      </section>
    </div>
  );
}

export default About;
