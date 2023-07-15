import React, { useEffect, useState } from 'react';
import './App.css';
import CommandList from './CommandList';
import CommandForm from './CommandForm';
import { getCommands } from './api';

function App() {
  const [commands, setCommands] = useState([]);

  useEffect(() => {
    getCommands()
      .then((data) => setCommands(data))
      .catch((error) => console.error('Error fetching commands:', error));
  }, []);

  return (
    <div className="App">
      <h1>Commands</h1>
      <CommandList commands={commands} setCommands={setCommands} />
      <CommandForm setCommands={setCommands} />
    </div>
  );
}

export default App;
