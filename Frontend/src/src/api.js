// api.js
const BASE_URL = 'https://mrdrift.live/api';

export const getCommands = () => {
  return fetch(`${BASE_URL}/get_commands`)
    .then((response) => response.json())
    .then((data) => data.commands)
    .catch((error) => {
      console.error('Error fetching commands:', error);
      return [];
    });
};

export const addCommand = (newCommandObj) => {
  return fetch(`${BASE_URL}/add_command`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify(newCommandObj),
  })
    .then((response) => response.json())
    .then((data) => data.success)
    .catch((error) => {
      console.error('Error adding command:', error);
      return false;
    });
};

export const removeCommand = (command) => {
  return fetch(`${BASE_URL}/remove_command`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({ command }),
  })
    .then((response) => response.json())
    .then((data) => data.success)
    .catch((error) => {
      console.error('Error removing command:', error);
      return false;
    });
};
