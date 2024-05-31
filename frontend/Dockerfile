FROM node:14

WORKDIR /app

COPY . /app

RUN npm install

EXPOSE 3000

ENV REACT_APP_BACKEND_URL=http://localhost:5000

CMD ["npm", "start"]

