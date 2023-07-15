import React from 'react';
import { handleRemoveCommand } from './CommandActions';

const CommandList = ({ commands, setCommands }) => {
  return (
    <ul>
      {commands.map((command) => (
        <li key={command.command}>
          {command.command}: {command.response}
          <button
            onClick={() => handleRemoveCommand(command.command, setCommands)}
          >
            Remove
          </button>
        </li>
      ))}
    </ul>
  );
};

export default CommandList;
