import React, {useState, useEffect} from 'react';
import './App.css';
import { BrowserRouter as Router, Switch, Route, Link, useRouteMatch, useParams } from "react-router-dom";

import { Genes, Diseases, Proteins } from './components/Entities';
import Gene from './components/Gene';
import Disease from './components/Disease';
import Protein from './components/Protein';
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
            <Link to="/protein">Proteins</Link>
          </li>
        </ul>

        <Switch>
          {/* <Route path="/about">
            <About />
          </Route> */}
          <Route path={`/gene/:geneName`}>
            <Gene />
          </Route>
          <Route path={`/disease/:diseaseName`}>
            <Disease />
          </Route>
          <Route path={`/protein/:ensp_id`}>
            <Protein />
          </Route>
          <Route path="/gene">
            <Genes />
          </Route>
          <Route path="/disease">
            <Diseases />
          </Route>
          <Route path="/protein">
            <Proteins />
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
