# FastAPI TDD Docker

![CI/CD](https://github.com/MikhailZakharov-dev/fastapi-tdd-docker/actions/workflows/main.yml/badge.svg?branch=main)

A FastAPI application built with Test-Driven Development (TDD) principles, containerized with Docker and Docker Compose.

## Features

- 🚀 FastAPI web framework
- 🐘 PostgreSQL database with Tortoise ORM
- 🧪 Pytest for testing
- 🐳 Docker & Docker Compose for containerization
- 📦 UV for fast dependency management
- 🔄 Database migrations with Aerich

## Prerequisites

- Docker and Docker Compose installed
- Git

## Quick Start

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd fastapi-tdd-docker
   ```

2. **Start the application**
   ```bash
   docker-compose up --build
   ```

3. **Access the application**
   - API: http://localhost:8004
   - API Documentation: http://localhost:8004/docs
   - Alternative Docs: http://localhost:8004/redoc

## Development

### Running the Application

The development setup includes hot-reload and volume mounting:

```bash
docker-compose up
```

The application will be available at `http://localhost:8004` with auto-reload enabled.

### Running Tests

```bash
docker-compose exec web pytest
```

### Database Migrations

The application uses Aerich for database migrations. Migrations are automatically applied on startup.

## API Endpoints

### Health Check
- `GET /ping` - Returns pong with environment info

### Summaries
- `POST /summaries/` - Create a new summary
- `GET /summaries/` - Get all summaries
- `GET /summaries/{id}/` - Get a specific summary by ID

## Project Structure

```
fastapi-tdd-docker/
├── docker-compose.yml      # Docker Compose configuration
└── project/
    ├── app/                # Application code
    │   ├── api/           # API routes
    │   ├── models/        # Database and Pydantic models
    │   ├── config.py      # Configuration settings
    │   ├── db.py          # Database initialization
    │   └── main.py        # FastAPI application
    ├── tests/             # Test files
    ├── migrations/        # Database migrations
    ├── Dockerfile         # Development Docker image
    ├── Dockerfile.prod    # Production Docker image
    └── pyproject.toml     # Project dependencies
```

## Production Deployment

For production, use the production Dockerfile:

```bash
docker build -f project/Dockerfile.prod -t fastapi-tdd-docker:prod ./project
```

The production image runs with Gunicorn and Uvicorn workers.

## Environment Variables

- `ENVIRONMENT` - Environment (dev/prod)
- `TESTING` - Testing mode flag
- `DATABASE_URL` - PostgreSQL connection string
- `DATABASE_TEST_URL` - Test database connection string
- `PORT` - Server port (production)

## License

MIT

