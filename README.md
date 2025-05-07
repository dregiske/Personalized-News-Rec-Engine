# Personalized News Recommendation Engine — Project Plan

## 1. Project Overview

Build a web application that suggests news articles tailored to each user based on (a) collaborative filtering of reading histories and (b) content-based similarity on article metadata.

## 2. Objectives

Implement both collaborative and content-based recommendation models

Expose a Python API (FastAPI) serving recommendations

Build a responsive frontend (React/Vue) showing a personalized "For You" feed

Store data in PostgreSQL and optimize queries for performance

Deploy end-to-end in a containerized setup (Docker)

## 3. MVP Features

User onboarding (simple sign-up/login)

Article ingestion pipeline (static dataset or News API)

Recording user interactions (clicks, likes, reads)

Batch model training and nightly updates

Endpoint: GET /recommendations?user_id=...

Frontend: display recommended articles with title, summary, and image

## 4. Tech Stack

Backend & ML: Python 3.10+, FastAPI, scikit-learn / surprise.psych, PySpark (optional)

Database: PostgreSQL (ORM via SQLAlchemy)

Frontend: React (TypeScript) or Vue (TypeScript)

Infrastructure: Docker, Docker-Compose, GitHub Actions CI

## 5. Data Sources

Initial: Kaggle "All the News" dataset (NYTimes, The Huffington Post)

Later: integrate a live News API (e.g., NewsAPI.org) for fresh articles

## 6. Database Schema (Draft)

users: id, email, hashed_password, created_at

articles: id, title, content, source, publish_date, keywords

interactions: id, user_id, article_id, event_type (click/read/like), timestamp

## 7. Milestones & Timeline

Week 1: Repo setup, environment, database schema & migrations

Week 2: Data ingestion & storage; seed with static dataset

Week 3: Basic content-based recommender + API endpoint

Week 4: Collaborative filtering implementation + nightly batch job

Week 5: Frontend scaffolding + integrate recommendation API

Week 6: Deployment pipeline, Dockerization, and testing

## 8. Next Immediate Step

Define and finalize the MVP scope: confirm which features we’ll include for initial launch and what can be deferred.

## 9. Setup

### Step 1. Clone the repo
1. In your terminal, clone this github repository
```
git clone https://github.com/dregiske/Personalized-News-Rec-Engine/tree/main
cd Personalized-News-Rec-Engine
```
### Step 2. Virtual Environment
1. In your repo root, create and activate a virtual environment
``` 
python3 -m venv venv
source venv/bin/activate	# macOS/Linux
venv\Scripts\activate		# Windows
```

2. Install core dependencies and record them
```
pip install fastapi uvicorn sqlalchemy psycopg2-binary
pip freeze > requirements.txt
```
### Step 3. Database Schema & Migrations
1. Create a `.env` file in the project root with your database URL
```
DATABASE_URL=postgresql://<user>:password@localhost:5432/<dbname>
```

2. Initialize alembic for migrations
```
alembic init migrations
```

3. Configure `alembic.ini`
- Set `sqlalchemy.url` to reference env("DATABASE_URL") by loading `.env` in `.env.py` via python-dotenv
- In `env.py`, import your SQLAlchemy `Base` metadata from `app/models.py`

4. Define your models in `app/models.py`

5. Generage and apply the initial migration
```
alembic revision --autogenerate -m "Initial schema"
alembic upgrade head
```

### Step 4. Spin Up PostgreSQL Locally
1. If you don't have Postgres installed, use Docker
```
docker run --name news-db \
	-e POSTGRES_USER=user \
	-e POSTGRES_PASSWORD=pass \
	-e POSTGRES_DB=newsdb \
	-p 5432:5432 -d postgres