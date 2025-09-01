# ---------- Frontend Build ----------
FROM node:20-slim as frontend

WORKDIR /app
COPY emp-app/package*.json ./emp-app/
WORKDIR /app/emp-app
RUN npm install
COPY emp-app .
RUN npm run build


# ---------- Backend ----------
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Copy built frontend into backend "static" folder
COPY --from=frontend /app/emp-app/dist ./static

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
