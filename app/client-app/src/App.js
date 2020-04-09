import React, {useState, useEffect} from 'react';
import './App.css';
import { BrowserRouter as Router, Switch, Route, Link, useRouteMatch, useParams } from "react-router-dom";

import { Genes, Diseases, Compounds, Assays } from './components/Entities';
import Search from './components/Search';


export default function App() {
  return (
    <Router>
      <div>
        <ul>
          <li>
            <Link to="/">Home</Link>
          </li>
          {/* <li>
            <Link to="/about">About</Link>
          </li> */}
          <li>
            <Link to="/gene">Genes</Link>
          </li>
          <li>
            <Link to="/disease">Diseases</Link>
          </li>
          <li>
            <Link to="/compound">Compound</Link>
          </li>
          <li>
            <Link to="/assay">Assay</Link>
          </li>
        </ul>

        <Switch>
          {/* <Route path="/about">
            <About />
          </Route> */}
          <Route path="/gene">
            <Genes />
          </Route>
          <Route path="/disease">
            <Diseases />
          </Route>
          <Route path="/compound">
            <Compounds />
          </Route>
          <Route path="/assay">
            <Assays />
          </Route>
          <Route path="/">
            <Search />
          </Route>
        </Switch>
      </div>
    </Router>
  );
}

function About() {
  return <h2>About</h2>;
}
