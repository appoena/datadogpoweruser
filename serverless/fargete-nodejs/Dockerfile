FROM node:slim

WORKDIR 	/app
COPY 		. /app/
RUN 		npm install dd-trace --save
EXPOSE 		3000
ENTRYPOINT 	["node", "index.js"]


