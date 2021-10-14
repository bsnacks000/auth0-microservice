import React, { Fragment } from "react";

import HomeContent from "../components/HomeContent";
import Hero from "../components/Hero"

const Home = () => (
  <Fragment>
    <Hero />
    <hr />
    <HomeContent />
  </Fragment>
);

export default Home;