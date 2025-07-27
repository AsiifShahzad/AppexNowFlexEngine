
import Header from "./components/Header"
import EmployeeInput from "./components/EmployeeInput"

import './App.css'

function App() {
  const handleCalculate = (data) => {
    console.log("Form Data:", data);
    // You can call your API here
  };

  return (
    <>
      <Header/>
      <EmployeeInput onSubmit={handleCalculate} />
    </>
  )
}

export default App
