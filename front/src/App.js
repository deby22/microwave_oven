import './App.css';
import { useState, useEffect } from "react";

function App() {
  const [state, setState] = useState({})
  const [token, setToken] = useState("");


  const fetchState = () => {
    fetch("http://localhost:8000/state")
      .then(response => {return response.json()})
      .then(data => {setState(data)})
  }

  const increasePower = () => {updatePower(10)}
  const updatePower = (power) => {
    fetch("http://localhost:8000/power", {
        method: "POST",
        headers: {
          'Accept': 'application/json',
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({power})
    })
      .then(response => {return response.json()})
      .then(data => {setState(data)})
  }
  const updateCounter = (time) => {
    fetch("http://localhost:8000/time", {
        method: "POST",
        headers: {
          'Accept': 'application/json',
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({time})
    })
      .then(response => {return response.json()})
      .then(data => {setState(data)})
  }

  const obtainToken = () => {
    fetch("http://localhost:8000/signup", {
        method: "POST",
        headers: {
          'Accept': 'application/json',
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({email: "sample@email.com"})
    })
      .then(response => {return response.json()})
      .then(data => {setToken(data)})
  }
  const cancel = () => {
    fetch("http://localhost:8000/cancel", {
        method: "POST",
        headers: {
          'Accept': 'application/json',
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${token}`
        }}
    )
      .then(response => {return response.json()})
      .then(data => {setState(data)})
  }
  const decreasePower = () => {updatePower(-10)}
  const increaseCounter = () => {updateCounter(10)}
  const decreaseCounter = () => {updateCounter(-10)}


  useEffect(() => {
      fetchState();
  }, [])


  return (
    <div className="App">
      <div className="preference">
        <label htmlFor="state">State</label> <input readOnly name="state" id="state" value={state.state}/>
      </div>
      <div className="preference">
        <label htmlFor="power">Power</label> <input readOnly name="power" id="power" value={state.power}/>
        <button onClick={increasePower}>Increase Power by 10%</button>
        <button onClick={decreasePower}>Decrease Power by 10%</button>
      </div>
      <div className="preference">
        <label htmlFor="counter">Counter</label> <input readOnly name="counter" id="counter" value={state.counter}/>
        <button onClick={increaseCounter}>Increase Counter by 10 sec</button>
        <button onClick={decreaseCounter}>Decrease Counter by 10 sec</button>
      </div>
      <div className="preference">
          <label htmlFor="token">Token</label> <input readOnly name="token" id="token" value={token}/>
          <button onClick={obtainToken}>getToken</button>
      </div>
      <div className="preference">
          <button onClick={cancel}>CANCEL</button>
      </div>
    </div>
  );
}

export default App;
