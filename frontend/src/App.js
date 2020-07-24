import React from 'react';
import './App.css';

function App() {
  
  fetch("/test")
    .then(response => response.json())
    .then(data => {console.log(data)
    });

  

  return (
    <div className="App">
      Welcome!
    </div>
  );
}

export default App;
