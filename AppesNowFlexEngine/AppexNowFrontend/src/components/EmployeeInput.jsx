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

  const [errors, setErrors] = useState({});

  const [response, setResponse] = useState(null);

  const handleChange = (e) => {
    setFormData((prev) => ({
      ...prev,
      [e.target.name]: e.target.value,
    }));
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    const newErrors = {};

    // ✅ Validate Current Salary
    const salary = parseFloat(formData.currentSalary);
    if (!formData.currentSalary || isNaN(salary) || salary <= 0) {
      newErrors.currentSalary = "Please enter a valid salary (greater than 0)";
    }
    // ✅ Experience validation
    const experience = parseFloat(formData.yearsExperience);
    if (!formData.yearsExperience || isNaN(experience) || experience < 0) {
      newErrors.yearsExperience = "Experience cannot be negative";
    }
    // ✅ Validate Performance Score
    const score = parseFloat(formData.performanceScore);
    if (!formData.performanceScore || isNaN(score) || score < 1 || score > 10) {
      newErrors.performanceScore = "Score must be a number between 1 and 10";
    }

    if (Object.keys(newErrors).length > 0) {
      setErrors(newErrors);
      return;
    }

    setErrors({}); // clear errors if valid

    const payload = {
      employeeId: formData.employeeId,
      currentSalary: salary,
      yearsExperience: experience,
      performanceScore: score,
      jobRole: formData.jobRole,
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
          placeholder="e.g. emp1234"
          value={formData.employeeId}
          onChange={handleChange}
          required
        />

        <label htmlFor="salary">Current Salary</label>
        <input
          className="form-input"
          type="number"
          name="currentSalary"
          placeholder="salary in PKR"
          value={formData.currentSalary}
          onChange={handleChange}
          required
        />
        {errors.currentSalary && (
          <span className="error-text">{errors.currentSalary}</span>
        )}
        <label htmlFor="tenure">Years of Experience</label>
        <input
          className="form-input"
          type="number"
          name="yearsExperience"
          placeholder="experience in years"
          value={formData.tenure}
          onChange={handleChange}
          required
        />
        {errors.yearsExperience && (
          <span className="error-text">{errors.yearsExperience}</span>
        )}

        <label htmlFor="score">Performance Score</label>
        <input
          className="form-input"
          type="number"
          name="performanceScore"
          placeholder="score between 1-10"
          value={formData.performanceScore}
          onChange={handleChange}
          min={1}
          max={10}
          required
        />
        {errors.performanceScore && (
          <span className="error-text">{errors.performanceScore}</span>
        )}

        <label htmlFor="role">Job Role</label>
        <input
          className="form-input"
          type="text"
          name="jobRole"
          placeholder="e.g. Software Engineer"
          value={formData.role}
          onChange={handleChange}
          required
        />

        <label htmlFor="location">Location</label>
        <input
          className="form-input"
          type="text"
          name="location"
          placeholder="e.g. Lahore"
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
