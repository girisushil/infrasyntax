# Use an official Node runtime as a parent image
FROM node:20-alpine

# Set the working directory
WORKDIR /app

# Copy package files and install dependencies
COPY package*.json ./
RUN npm install

# Copy the rest of the application code
COPY . .

# Make port 5173 available to the world outside this container
EXPOSE 5173

# Command to run the app
CMD ["npm", "run", "dev"]