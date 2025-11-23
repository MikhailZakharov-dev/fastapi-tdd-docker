# FastAPI TDD Docker

![CI/CD](https://github.com/MikhailZakharov-dev/fastapi-tdd-docker/actions/workflows/main.yml/badge.svg?branch=main)

A FastAPI application built with Test-Driven Development (TDD) principles, containerized with Docker and Docker Compose.

## Features

- 🚀 FastAPI web framework
- 🐘 PostgreSQL database with Tortoise ORM
- 🧪 Pytest for testing with coverage reports
- 🐳 Docker & Docker Compose for containerization
- 📦 UV for fast dependency management
- 🔄 Database migrations with Aerich
- 📰 Web scraping and article summarization using newspaper3k
- ⚡ Background task processing for async summary generation
- 🔍 Code linting with Ruff

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

Run all tests:
```bash
docker-compose exec web pytest
```

Run tests with coverage:
```bash
docker-compose exec web pytest --cov=app --cov-report=html
```

Coverage reports are generated in the `htmlcov/` directory.

### Database Migrations

The application uses Aerich for database migrations. Migrations are automatically applied on startup.

## API Endpoints

### Health Check
- `GET /ping` - Returns pong with environment info

### Version
- `GET /version` - Returns deployment version information (commit SHA, build time, environment)

### Summaries
The summaries feature extracts and summarizes articles from web URLs using web scraping.

- `POST /summaries/` - Create a new summary from a URL
  - Accepts a URL in the request body
  - Returns immediately with summary ID (processing happens asynchronously in background)
  - Payload: `{"url": "https://example.com/article"}`
- `GET /summaries/` - Get all summaries
- `GET /summaries/{id}/` - Get a specific summary by ID
- `PUT /summaries/{id}/` - Update a summary
- `DELETE /summaries/{id}/` - Delete a summary

## Project Structure

```
fastapi-tdd-docker/
├── docker-compose.yml      # Docker Compose configuration
├── docker-login.sh         # Docker registry login script
├── docker-push.sh          # Docker image push script
├── docker-verify.sh        # Docker image verification script
├── release.sh              # Heroku deployment script
└── project/
    ├── app/                # Application code
    │   ├── api/           # API routes (ping, summaries, version)
    │   ├── models/        # Database and Pydantic models
    │   ├── config.py      # Configuration settings
    │   ├── db.py          # Database initialization
    │   ├── main.py        # FastAPI application
    │   └── summarizer.py  # Article summarization logic
    ├── db/                 # Database setup
    │   ├── Dockerfile     # PostgreSQL Docker image
    │   └── create.sql     # Database initialization script
    ├── tests/             # Test files
    ├── migrations/        # Database migrations (Aerich)
    ├── htmlcov/           # HTML coverage reports
    ├── Dockerfile         # Development Docker image
    ├── Dockerfile.prod    # Production Docker image
    ├── entrypoint.sh      # Container entrypoint script
    ├── pyproject.toml     # Project dependencies and config
    └── uv.lock            # UV lock file
```

## Production Deployment

For production, use the production Dockerfile:

```bash
docker build -f project/Dockerfile.prod -t fastapi-tdd-docker:prod ./project
```

The production image runs with Gunicorn and Uvicorn workers.

## Environment Variables

- `ENVIRONMENT` - Environment (dev/prod, default: dev)
- `TESTING` - Testing mode flag (0 or 1, default: 0)
- `DATABASE_URL` - PostgreSQL connection string
- `DATABASE_TEST_URL` - Test database connection string
- `PORT` - Server port (production, default: 8000)
- `GIT_COMMIT_SHA` - Git commit SHA for version endpoint (optional)
- `BUILD_TIME` - Build timestamp for version endpoint (optional)

## License

MIT

