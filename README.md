# README

## Backend (Python)
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Apply database migrations with SQLAlchemy :
   ```bash
   python -m flask db upgrade  
   ```
3. Start the server:
   ```bash
   python server.py
   ```

## Frontend (React)
1. Install dependencies:
   ```bash
   npm install
   ```
2. Start the frontend:
   ```bash
   npm start
   ```

## Database (PostgreSQL)
1. Start a PostgreSQL instance (example with Docker):
   ```bash
   docker run --name postgres -e POSTGRES_PASSWORD=mysecretpassword -p 5432:5432 -d postgres
   ```
2. Provide the backend with a connection string via environment variable:
   ```bash
   export DATABASE_URL=postgresql://username:password@localhost:5432/databasename
   ```

## Required Environment Variables
Backend:
Either export or use .env file
```bash
export DATABASE_URL=postgresql://user:password@localhost:5432/dbname
export AZURE_OPENAI_KEY=your_azure_openai_api_key
```

Frontend:
```bash
export REACT_APP_API_BASE=http://localhost:5000
```

## Summary
- pip install -r requirements.txt
- python apply_migrations.py
- python server.py
- npm install
- npm start
- Set DATABASE_URL, AZURE_OPENAI_KEY, and REACT_APP_API_BASE before running.
