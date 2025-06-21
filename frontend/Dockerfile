# Dockerfile for the frontend application

# Stage 1: Build the frontend
FROM node:18-alpine AS builder

# Set working directory
WORKDIR /app

# Copy package files and install dependencies
COPY package*.json ./
RUN npm install

# Copy the rest of the app and build
COPY . .
RUN npm run build

# Stage 2: Serve the frontend using a minimal image
FROM node:18-alpine

WORKDIR /app

# Copy the built output from the builder
COPY --from=builder /app ./

# Expose port 3000
EXPOSE 3000

# Start the frontend
CMD ["npm", "start"]
