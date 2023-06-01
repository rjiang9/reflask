import logo from './logo.svg';
import './App.css';
import React, { useEffect, useState } from 'react';
import axios from 'axios'

function App() {
  const [getMessage, setGetMessage] = useState({})

  useEffect(()=>{
    axios.get('http://localhost:5000/auth/profile').then(response => {
      console.log("SUCCESS", response)
      setGetMessage(response)
    }).catch(error => {
      console.log(error)
    })

    // axios.get('http://localhost:5000/flask/hello').then(response => {
    //   console.log("SUCCESS", response)
    //   setGetMessage(response)
    // }).catch(error => {
    //   console.log(error)
    // })

  }, [])
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>React + Flask Tutorial Ray</p>
        <p>{getMessage.status}</p>
        <div>{getMessage.status === 200 ? 
          <h3>{getMessage.data.name} {getMessage.data.about}</h3>
          :
          <h3>LOADING</h3>}</div>
      </header>
    </div>
  );
}


export default App;
