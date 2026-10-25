# CENG413 HW-2: Two Services with Docker Compose
Setup env: `cp .env.example .env`
Start: `docker compose up -d --build`
Test state: `curl http://localhost:8000/visit` and `curl "http://localhost:8000/notes?add=study-docker"`
Stop: `docker compose down`
