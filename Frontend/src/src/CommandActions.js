import { addCommand, removeCommand } from './Api';

export const handleAddCommand = (command, response, setCommands) => {
  const newCommandObj = { command, response };

  addCommand(newCommandObj)
    .then((success) => {
      if (success) {
        setCommands((prevCommands) => [...prevCommands, newCommandObj]);
      } else {
        console.error('Failed to add command');
      }
    })
    .catch((error) => console.error('Error adding command:', error));
};

export const handleRemoveCommand = (command, setCommands) => {
  removeCommand(command)
    .then((success) => {
      if (success) {
        setCommands((prevCommands) =>
          prevCommands.filter((c) => c.command !== command)
        );
      } else {
        console.error('Failed to remove command');
      }
    })
    .catch((error) => console.error('Error removing command:', error));
};
