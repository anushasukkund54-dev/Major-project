# Major-project

# Job Search AI

An AI-powered job search platform that integrates third-party job search APIs with a FastAPI backend and an LLM-based matching system to help users discover and evaluate jobs based on their resumes, skills, experience, and preferences.

## Overview

Job Search AI provides a complete workflow for discovering relevant job opportunities and evaluating how well they match a user's profile.

The system combines:

* REST APIs built with FastAPI
* Third-party job search API integration
* PostgreSQL for persistent data storage
* JWT-based authentication
* Resume upload and parsing
* LLM-powered resume analysis
* AI-based job matching and ranking
* Saved jobs and application tracking
* Docker-based deployment

## Architecture

```text
                         ┌──────────────────┐
                         │     Frontend     │
                         └────────┬─────────┘
                                  │
                              REST API
                                  │
                                  ▼
                    ┌─────────────────────────┐
                    │     FastAPI Backend     │
                    │                         │
                    │  Auth │ Jobs │ Resume  │
                    │       │       │        │
                    │       │       │   AI   │
                    └───────┼───────┼────┬────┘
                            │       │    │
              ┌─────────────┘       │    └──────────────┐
              │                     │                   │
              ▼                     ▼                   ▼
       ┌─────────────┐      ┌──────────────┐    ┌─────────────┐
       │ PostgreSQL  │      │ Third-Party  │    │ AI / LLM    │
       │             │      │ Job Search   │    │ Provider     │
       │ Users       │      │ API          │    │             │
       │ Resumes     │      │              │    │ Analysis    │
       │ Jobs        │      │ Job listings │    │ Matching    │
       │ Applications│      └──────────────┘    │ Ranking     │
       └─────────────┘                          └─────────────┘
```

## Core Workflow

### Job Search

```text
User
 ↓
FastAPI /jobs/search
 ↓
Job Search Service
 ↓
Third-Party Job Search API
 ↓
Normalize Job Results
 ↓
Return Jobs
```

### Resume Analysis

```text
Resume Upload
 ↓
Resume Service
 ↓
Document Parser
 ↓
Structured Resume Data
 ↓
AI Analysis
 ↓
Skills / Experience / Strengths / Gaps
 ↓
PostgreSQL
```

### AI Job Matching

```text
User Resume
     │
     ▼
Resume Skills & Experience
     │
     ▼
Job Search Results
     │
     ▼
Matching Service
     │
     ▼
LLM
     │
     ▼
Match Score
     │
     ├── Matched Skills
     ├── Missing Skills
     ├── Experience Fit
     └── Explanation
```

## Features

### Authentication

* User registration
* Secure password hashing
* JWT-based authentication
* Protected API endpoints
* Current-user profile

### Job Search

* Search jobs using a third-party Job Search API
* Keyword-based search
* Location filtering
* Experience filtering
* Job details
* Pagination
* Job result normalization

### Resume Management

* Resume upload
* Resume parsing
* Structured resume information
* Skill extraction
* Resume analysis
* Resume storage

### AI Features

* Resume skill extraction
* Job-resume matching
* Match scoring
* Missing-skill identification
* AI-generated match explanations
* Personalized job recommendations

### Application Tracking

* Save jobs
* Track applications
* Update application status
* View application history

## REST API

The backend exposes versioned REST APIs.

### Authentication

```text
POST /api/v1/auth/register
POST /api/v1/auth/login
POST /api/v1/auth/refresh
GET  /api/v1/auth/me
```

### Jobs

```text
GET  /api/v1/jobs
POST /api/v1/jobs/search
GET  /api/v1/jobs/{job_id}
POST /api/v1/jobs/{job_id}/save
DELETE /api/v1/jobs/{job_id}/save
```

### Resumes

```text
POST /api/v1/resumes
GET  /api/v1/resumes
GET  /api/v1/resumes/{resume_id}
POST /api/v1/resumes/{resume_id}/parse
DELETE /api/v1/resumes/{resume_id}
```

### AI

```text
POST /api/v1/ai/resume/analyze
POST /api/v1/ai/match
GET  /api/v1/ai/recommendations
```

### Applications

```text
POST   /api/v1/applications
GET    /api/v1/applications
GET    /api/v1/applications/{application_id}
PATCH  /api/v1/applications/{application_id}
DELETE /api/v1/applications/{application_id}
```

### Health

```text
GET /api/v1/health
```

## Example AI Matching Response

```json
{
  "match_score": 87,
  "matched_skills": [
    "Python",
    "FastAPI",
    "PostgreSQL"
  ],
  "missing_skills": [
    "AWS"
  ],
  "experience_fit": "Strong",
  "explanation": "The candidate has strong backend development experience that aligns with the core requirements of the position."
}
```

## Technology Stack

| Layer             | Technology                 |
| ----------------- | -------------------------- |
| Backend           | Python, FastAPI            |
| API               | REST                       |
| Database          | PostgreSQL                 |
| ORM               | SQLAlchemy                 |
| Migrations        | Alembic                    |
| Authentication    | JWT                        |
| AI                | LLM API                    |
| Job Data          | Third-Party Job Search API |
| Resume Processing | PDF/DOCX Parser            |
| Containerization  | Docker                     |
| Testing           | Pytest                     |
| API Documentation | OpenAPI / Swagger          |

## Project Structure

```text
job-search-ai/
│
├── backend/
│   ├── app/
│   │   ├── main.py
│   │   │
│   │   ├── api/
│   │   │   ├── auth.py
│   │   │   ├── jobs.py
│   │   │   ├── resumes.py
│   │   │   ├── ai.py
│   │   │   └── applications.py
│   │   │
│   │   ├── services/
│   │   │   ├── auth_service.py
│   │   │   ├── job_service.py
│   │   │   ├── resume_service.py
│   │   │   └── ai_service.py
│   │   │
│   │   ├── integrations/
│   │   │   ├── job_api_client.py
│   │   │   └── llm_client.py
│   │   │
│   │   ├── models/
│   │   │   ├── user.py
│   │   │   ├── resume.py
│   │   │   ├── saved_job.py
│   │   │   └── application.py
│   │   │
│   │   ├── schemas/
│   │   │   ├── auth.py
│   │   │   ├── job.py
│   │   │   ├── resume.py
│   │   │   └── ai.py
│   │   │
│   │   ├── db/
│   │   │   ├── session.py
│   │   │   └── base.py
│   │   │
│   │   └── core/
│   │       ├── config.py
│   │       ├── security.py
│   │       └── logging.py
│   │
│   ├── tests/
│   ├── alembic/
│   ├── requirements.txt
│   ├── Dockerfile
│   └── .env.example
│
└── frontend/
```

## Database Design

The initial database can contain:

```text
users
 ├── id
 ├── email
 ├── password_hash
 └── created_at

resumes
 ├── id
 ├── user_id
 ├── file_path
 ├── parsed_data
 └── created_at

jobs
 ├── id
 ├── external_id
 ├── title
 ├── company
 ├── location
 ├── description
 └── source_url

saved_jobs
 ├── user_id
 ├── job_id
 └── created_at

applications
 ├── id
 ├── user_id
 ├── job_id
 ├── status
 └── applied_at

match_results
 ├── id
 ├── user_id
 ├── resume_id
 ├── job_id
 ├── match_score
 └── analysis
```

## Environment Variables

Create a `.env` file locally.

```env
DATABASE_URL=your_postgresql_connection_string

JWT_SECRET_KEY=your_secret_key
JWT_ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30

JOB_API_KEY=your_job_search_api_key
JOB_API_URL=your_job_search_api_url

LLM_API_KEY=your_llm_api_key
```

Never commit the `.env` file or expose API keys in source code.

## Running the Backend

Create a virtual environment:

```bash
python -m venv venv
```

Activate it on Windows:

```powershell
.\venv\Scripts\Activate.ps1
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run database migrations:

```bash
alembic upgrade head
```

Start the FastAPI application:

```bash
uvicorn app.main:app --reload
```

API documentation will be available through FastAPI's generated OpenAPI documentation.

## Testing

Run the test suite using:

```bash
pytest
```

Tests should cover:

* Authentication
* JWT validation
* Job API integration
* Resume processing
* AI matching
* Database operations
* Application tracking
* API error handling

## Docker

The backend can be containerized using Docker.

Build the image:

```bash
docker build -t job-search-ai .
```

Run the container:

```bash
docker run -p 8000:8000 job-search-ai
```

For a multi-service setup, Docker Compose can be used to run the backend and PostgreSQL together.

## Security

The application follows basic production-oriented security practices:

* Passwords are stored as hashes
* JWT is used for authenticated API access
* Secrets are stored through environment variables
* Input validation is performed through API schemas
* Database access uses parameterized queries/ORM operations
* Protected endpoints require authentication
* API errors are handled without exposing sensitive information

## Future Improvements

Potential extensions include:

* Semantic/vector-based job matching
* Job recommendation engine
* Redis caching
* Background job processing
* Email notifications
* Application deadline reminders
* Advanced analytics
* Cloud deployment
* CI/CD pipeline
* Observability and monitoring

## Project Goal

The goal of this project is to demonstrate how a modern AI-powered application can combine **REST API development, third-party API integration, database management, authentication, document processing, and LLM-based reasoning** into a single practical system.
