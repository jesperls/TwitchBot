import React, { useState } from 'react';
import { handleAddCommand } from './CommandActions';

const CommandForm = ({ setCommands }) => {
  const [newCommand, setNewCommand] = useState('');
  const [newResponse, setNewResponse] = useState('');

  const handleCommandChange = (event) => {
    setNewCommand(event.target.value);
  };

  const handleResponseChange = (event) => {
    setNewResponse(event.target.value);
  };

  const handleSubmit = () => {
    handleAddCommand(newCommand, newResponse, setCommands);
    setNewCommand('');
    setNewResponse('');
  };

  return (
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
      <button onClick={handleSubmit}>Add Command</button>
    </div>
  );
};

export default CommandForm;
