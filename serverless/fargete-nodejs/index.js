// This line must come before importing any instrumented module.
const tracer = require('dd-trace').init({
	logInjection: true
});

const express = require('express');
const logger = require('./winston');
const cors = require('cors');
const app = express();
app.use(cors({
	origin: '*'
}));

app.use((req, res, next) => {
  logger.info(`Request received: ${req.method} ${req.url}`);
  next();
});

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  logger.info(`Server is running on port ${PORT}`);
});

app.use((err, req, res, next) => {
  logger.error(`Error occurred: ${err.message}`);
  res.status(500).send('Internal Server Error');
});

app.get("/msg", (req, res, next) => {
  logger.info(`get called: ${req.method} ${req.url} ${res.statusCode}`);
  res.status(200).send(`Api called: ${req.method} ${req.url}`);
});

app.post("/msg", (req, res, next) => {
  logger.info(`post called: ${req.method} ${req.url} ${res.statusCode}`);
  const newMessage = new Message(req.body.message);
  res.json({"receivedMessage": newMessage.getContent()});
  res.status(201);
  
});

