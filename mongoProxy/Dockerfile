FROM node:10

RUN git clone https://github.com/JamesOsgood/mongodb-grafana.git

WORKDIR /mongodb-grafana

RUN npm install
CMD npm run server
