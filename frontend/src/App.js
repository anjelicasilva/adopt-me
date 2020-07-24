import React from 'react';
import logo from './logo.svg';
import './App.css';

function App() {
  fetch("/test")
    .then(response => response.json())
    .then(data => {
      console.log('hey', data.test)
    });

  return (
    <div className="App">
      Yo!
    </div>
  );
}

export default App;
