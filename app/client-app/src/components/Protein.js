import React, { useState, useEffect } from 'react';
import { Link, useParams } from "react-router-dom";

import { loadProteinInfo } from './functions';

export default function Protein() {
  let { proteinName } = useParams();

  const [data, setData] = useState({});

  useEffect(() => {
    async function fetchData() {
      const response = await loadProteinInfo(proteinName);
      console.log(response)
      setData(response);
    }
    fetchData();
  }, [proteinName]);

  // let related = Object.assign({}, data.Neighbors)
  let proteins = [].concat(data.RelatedProtein)
  // var genes = [].concat(related.Gene)
  // related = Object.assign({}, data.RelatedDisease)
  // var diseases = [].concat(related.RelatedByGene)

    return (
        <div>
      <center><h1>Protein Details</h1></center>
      <div>
        Protein Interactions
          <ul>
          {proteins.map((protein) => (
            <li><Link to={`/protein/${protein}`}>{protein}</Link></li>
          ))}
        </ul>
      </div>
      <div>
        Genes Encoded For
      </div>
        
    </div>
    )
}