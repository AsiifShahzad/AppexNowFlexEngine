import React, { useState } from 'react';
import './Login.css';

const allowedUsers = {
  'admin.abc@gmail.com': 'admin123',
  'hr.abc@gmail.com':    'hr123'
};

export default function Login({ onLoginSuccess }) {
  const [email, setEmail]       = useState('');
  const [password, setPassword] = useState('');
  const [error, setError]       = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();
    if (allowedUsers[email] && allowedUsers[email] === password) {
      onLoginSuccess(email);
    } else {
      setError('Invalid credentials.');
    }
  };

  return (
    <div className="login-container">
      <form className="login-form" onSubmit={handleSubmit}>
        <h2>Sign In</h2>

        <label>
          Email
          <input
            type="email"
            value={email}
            onChange={e => setEmail(e.target.value.trim())}
            required
          />
        </label>

        <label>
          Password
          <input
            type="password"
            value={password}
            onChange={e => setPassword(e.target.value)}
            required
          />
        </label>

        <button type="submit">Log In</button>
        {error && <p className="error">{error}</p>}
      </form>
    </div>
  );
}