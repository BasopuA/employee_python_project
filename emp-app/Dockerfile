# Use Node for frontend
FROM node:20-slim AS build

WORKDIR /app

COPY package*.json ./

RUN npm install

COPY . .

RUN npm run build

# Stage 2: Serve the React application with Nginx
FROM nginx:alpine

# Copy the built React app from the previous stage to Nginx's web server directory
COPY --from=build /app/dist /usr/share/nginx/html

EXPOSE 80

# Start Nginx when the container runs
CMD ["nginx", "-g", "daemon off;"]
