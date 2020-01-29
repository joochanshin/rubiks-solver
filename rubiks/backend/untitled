  
const express = require('express');
require('./server/config/config.js');

// Set up the express app
const app = express();

// Require our routes into the application.
require('./server/routes')(app);

app.get('*', (req, res) => res.status(200).send({
  message: 'Welcome to the beginning of nothingness.',
}));

module.exports = app;