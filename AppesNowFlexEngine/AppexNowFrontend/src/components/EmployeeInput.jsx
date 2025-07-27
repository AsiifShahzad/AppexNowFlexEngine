import React, { useState } from "react";
import "./EmployeeInput.css";

const EmployeeInput = () => {
  const [formData, setFormData] = useState({
    employeeId: "",
    currentSalary: "",
    yearsExperience: "",
    performanceScore: "",
    jobRole: "",
    location: "",
  });

  const [response, setResponse] = useState(null);

  const handleChange = (e) => {
    setFormData((prev) => ({
      ...prev,
      [e.target.name]: e.target.value,
    }));
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    console.log("Form data before transform:", formData);

    const payload = {
      employeeId: formData.employeeId,
      currentSalary: parseFloat(formData.salary),
      yearsExperience: parseFloat(formData.tenure),
      performanceScore: parseFloat(formData.score),
      jobRole: formData.role,
      location: formData.location,
    };

    console.log("Transformed payload:", payload);

    try {
      const res = await fetch("http://localhost:8000/calculate", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(payload),
      });
      if (!res.ok) throw new Error(`HTTP ${res.status}`);
      const data = await res.json();
      setResponse(data);
      console.log("Backend response:", data);
    } catch (err) {
      console.error("Error:", err);
    }
  };

  return (
    <div className="form-container">
      <form onSubmit={handleSubmit} className="employee-form">
        <label htmlFor="employeeId">Employee ID</label>
        <input
          className="form-input"
          type="text"
          name="employeeId"
          placeholder="Employee ID"
          value={formData.employeeId}
          onChange={handleChange}
          required
        />

        <label htmlFor="salary">Current Salary</label>
        <input
          className="form-input"
          type="number"
          name="salary"
          placeholder="Current Salary"
          value={formData.salary}
          onChange={handleChange}
          required
        />

        <label htmlFor="tenure">Years of Experience</label>
        <input
          className="form-input"
          type="number"
          name="tenure"
          placeholder="Years of Experience"
          value={formData.tenure}
          onChange={handleChange}
          required
        />

        <label htmlFor="score">Performance Score</label>
        <input
          className="form-input"
          type="number"
          name="score"
          placeholder="Performance Score"
          value={formData.score}
          onChange={handleChange}
          required
        />

        <label htmlFor="role">Job Role</label>
        <input
          className="form-input"
          type="text"
          name="role"
          placeholder="Job Role"
          value={formData.role}
          onChange={handleChange}
          required
        />

        <label htmlFor="location">Location</label>
        <input
          className="form-input"
          type="text"
          name="location"
          placeholder="Location"
          value={formData.location}
          onChange={handleChange}
          required
        />

        <button className="submit-btn" type="submit">
          Calculate My Raise & Bonus
        </button>
      </form>

      {response && (
        <div className="result">
          <p>
            <strong>Employee ID:</strong> {response.employeeId}
          </p>
          <p>
            <strong>Estimated Raise:</strong> {response.raiseAmount}
          </p>
          <p>
            <strong>Estimated Bonus:</strong> {response.bonusAmount}
          </p>
          <p>
            <strong>New Total Salary:</strong> {response.totalNewSalary}
          </p>
        </div>
      )}
    </div>
  );
};

export default EmployeeInput;
