import React, { useState } from 'react';
import Header from "./components/Header";
import EmployeeInput from "./components/EmployeeInput";
import Login from "./components/Login";

import './App.css';

function App() {
  // initialize logged‑in state from localStorage
  const [loggedIn, setLoggedIn] = useState(false
  );

  // callback passed down to Login
  const handleLoginSuccess = () => {
    setLoggedIn(true);
  };

  const handleCalculate = (data) => {
    console.log("Form Data:", data);
    // You can call your API here
  };

  // if not logged in, show only the Login screen
  if (!loggedIn) {
    return <Login onLoginSuccess={handleLoginSuccess} />;
  }

  // once logged in, render your normal app
  return (
    <>
      <Header />
      <EmployeeInput onSubmit={handleCalculate} />
    </>
  );
}

export default App;
