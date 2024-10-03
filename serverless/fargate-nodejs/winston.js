const { createLogger, format, transports } = require('winston');
const appRoot = require('app-root-path');
const logger = createLogger({
  level: 'info',
  exitOnError: false,
  format: format.json(),
  transports: [
    new transports.Console(),
    new transports.File({ filename: `${appRoot}/logs/rest-api.log` }),
  ],
});

module.exports = logger;