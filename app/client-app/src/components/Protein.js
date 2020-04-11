import React, { useState, useEffect } from 'react';
import { Link, useParams } from "react-router-dom";

import { loadProteinInfo } from './functions';

export default function Protein() {
  let { ensp_id } = useParams();
  const [data, setData] = useState({});

  useEffect(() => {
    setData({
      Neighbors: [],
      RelatedProtein: []
    })
    async function fetchData() {
      const response = await loadProteinInfo(ensp_id);
      console.log(response)
      setData(response);
    }
    fetchData();
  }, [ensp_id]);

  let related = Object.assign({}, data.Neighbors)
  let proteins = [].concat(related.Protein)

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
        Encoded By Gene
      </div>
        
    </div>
    )
}