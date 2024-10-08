FROM node:14-slim

RUN apt-get update && apt-get install -y procps

WORKDIR /app

COPY package.json ./
RUN npm install

COPY main.js ./

CMD ["node", "main.js"]
