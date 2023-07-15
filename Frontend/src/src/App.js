import React, { useEffect, useState } from 'react';
import './App.css'; // Assuming the CSS file is named App.css

function App() {
  const [commands, setCommands] = useState([]);
  const [newCommand, setNewCommand] = useState('');
  const [newResponse, setNewResponse] = useState('');

  useEffect(() => {
    fetch('https://mrdrift.live/api/get_commands')
      .then((response) => response.json())
      .then((data) => setCommands(data.commands))
      .catch((error) => console.error('Error fetching commands:', error));
  }, []);

  const handleCommandChange = (event) => {
    setNewCommand(event.target.value);
  };

  const handleResponseChange = (event) => {
    setNewResponse(event.target.value);
  };

  const handleAddCommand = () => {
    const newCommandObj = { command: newCommand, response: newResponse };

    fetch('https://mrdrift.live/api/add_command', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(newCommandObj),
    })
      .then((response) => response.json())
      .then((data) => {
        if (data.success) {
          // Command added successfully, update the list of commands
          setCommands([...commands, newCommandObj]);
          setNewCommand('');
          setNewResponse('');
        } else {
          console.error('Failed to add command:', data.error);
        }
      })
      .catch((error) => console.error('Error adding command:', error));
  };

  const handleRemoveCommand = (command) => {
    fetch('https://mrdrift.live/api/remove_command', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ command }),
    })
      .then((response) => response.json())
      .then((data) => {
        if (data.success) {
          // Command removed successfully, update the list of commands
          setCommands(commands.filter((c) => c.command !== command));
        } else {
          console.error('Failed to remove command:', data.error);
        }
      })
      .catch((error) => console.error('Error removing command:', error));
  };

  return (
    <div className="App">
      <h1>Commands</h1>
      <ul>
        {commands.map((command) => (
          <li key={command.command}>
            {command.command}: {command.response}
            <button onClick={() => handleRemoveCommand(command.command)}>
              Remove
            </button>
          </li>
        ))}
      </ul>
      <div>
        <input
          type="text"
          placeholder="Enter command"
          value={newCommand}
          onChange={handleCommandChange}
        />
        <input
          type="text"
          placeholder="Enter response"
          value={newResponse}
          onChange={handleResponseChange}
        />
        <button onClick={handleAddCommand}>Add Command</button>
      </div>
    </div>
  );
}

export default App;
