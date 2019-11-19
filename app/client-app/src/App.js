import React, {useState, useEffect} from 'react';
import logo from './logo.svg';
import Genes from './components/Genes';
import Diseases from './components/Diseases';
import DTable from './components/GeneTable';
import './App.css';
import { BrowserRouter as Router, Switch, Route, Link, useRouteMatch, useParams } from "react-router-dom";

export default function App() {
  return (
    <Router>
      <div>
        <ul>
          <li>
            <Link to="/">Home</Link>
          </li>
          <li>
            <Link to="/about">About</Link>
          </li>
          <li>
            <Link to="/gene">Genes</Link>
          </li>
          <li>
            <Link to="/disease">Diseases</Link>
          </li>
          <li>
            <Link to="/dtable">TableTrial</Link>
          </li>
        </ul>

        <Switch>
          <Route path="/about">
            <About />
          </Route>
          <Route path="/gene">
            <Genes />
          </Route>
          <Route path="/disease">
            <Diseases />
          </Route>
          <Route path="/">
            <Home />
          </Route>
          <Route path="/dtable">
            <DTable />
          </Route>
        </Switch>
      </div>
    </Router>
  );
}

function Home() {
  return <h2>Home</h2>;
}

function About() {
  return <h2>About</h2>;
}