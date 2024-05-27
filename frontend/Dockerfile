# Use the official Node.js image as a parent image
FROM node:14

# Set the working directory
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages
RUN npm install

# Make port 3000 available to the world outside this container
EXPOSE 3000

# Define environment variable for backend URL
ENV REACT_APP_BACKEND_URL=http://localhost:5000

# Run npm start to launch the application
CMD ["npm", "start"]


##### original #####
# FROM node:20.11-bookworm

# WORKDIR /app

# COPY package.json ./
# COPY package-lock.json ./

# RUN npm ci

# COPY ./ ./

# ENTRYPOINT ["npm", "start"]
