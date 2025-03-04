import React, { useState } from 'react';
import './App.css';

function App() {
  const [username, setUsername] = useState('');
  const [website, setWebsite] = useState('');
  const [password, setPassword] = useState('');

  const generatePassword = () => {
    const chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()";
    let pass = "";
    for (let i = 0; i < 12; i++) {
      pass += chars.charAt(Math.floor(Math.random() * chars.length));
    }
    setPassword(pass);
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    await fetch('http://localhost:5000/store', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ username, website, password })
    });
    setUsername('');
    setWebsite('');
    setPassword('');
  };

  return (
    <div className="App">
      <h1>Password Manager</h1>
      <form onSubmit={handleSubmit}>
        <input type="text" placeholder="Username" value={username} onChange={(e) => setUsername(e.target.value)} required />
        <input type="text" placeholder="Website" value={website} onChange={(e) => setWebsite(e.target.value)} required />
        <input type="text" placeholder="Password" value={password} onChange={(e) => setPassword(e.target.value)} required />
        <button type="button" onClick={generatePassword}>Generate Password</button>
        <button type="submit">Save</button>
      </form>
    </div>
  );
}

export default App;
