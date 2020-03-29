import React, { useState, useEffect } from 'react';
import { Link, useParams } from "react-router-dom";

import { loadProteinInfo } from './functions';

export default function Protein() {
    return (
        <div>
      <center><h1>Protein Details</h1></center>
      <div>
        Associated Diseases
          {/* <ul>
          {genes.map((gene) => (
            <li><Link to={`/gene/${gene}`}>{gene}</Link></li>
          ))}
        </ul> */}
      </div>
        
    </div>
    )
}