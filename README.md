# Job Board API

A REST API built with Django and Django REST Framework that allows companies to post jobs and job seekers to apply.

## Tech Stack
- Django
- Django REST Framework
- SimpleJWT
- SQLite (development)
- PostgreSQL (production)

## Features
- JWT Authentication
- Role based access — company owners and job seekers
- Job posting and management
- Job applications
- Filtering by location and job type
- Search by title and description
- Pagination

## Setup Instructions
1. Clone the repo
2. Create virtual environment — `python -m venv env`
3. Activate — `env\Scripts\activate`
4. Install dependencies — `pip install -r requirements.txt`
5. Run migrations — `python manage.py migrate`
6. Run server — `python manage.py runserver`

## API Endpoints
| Endpoint | Method | Permission |
|---|---|---|
| /api/auth/register/ | POST | Anyone |
| /api/auth/login/ | POST | Anyone |
| /api/auth/token/refresh/ | POST | Anyone |
| /api/companies/ | GET | Anyone |
| /api/companies/ | POST | Company only |
| /api/jobs/ | GET | Anyone |
| /api/jobs/ | POST | Company only |
| /api/jobs/?location=Delhi | GET | Anyone |
| /api/jobs/?search=Django | GET | Anyone |
| /api/applications/ | POST | Job seeker only |
| /api/applications/ | GET | Job seeker — own only |
