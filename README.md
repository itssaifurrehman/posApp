# posApp
Entire Application built using NextJS and Python Django with PostgresSQL

Install Python, Django, Nodejs, NPM, Postgres

Versions
This project is developed using
Python 3.13.1
django-admin 5.1.5
Node v22.14.0
npm 10.9.2
next 15.1.7
react 19.0.0


Step 1: Set Up Backend (Django + PostgreSQL)
1. Create a Virtual Environment

First, install Python and create a virtual environment:

mkdir pos-system && cd pos-system
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

2. Install Django & DRF (Django REST Framework)

pip install django djangorestframework django-cors-headers psycopg2-binary

3. Create a Django Project

django-admin startproject backend
cd backend

4. Set Up PostgreSQL Database

    Install PostgreSQL if not installed.

    Create a database:

CREATE DATABASE posdb;
CREATE USER posuser WITH PASSWORD 'yourpassword';
ALTER ROLE posuser SET client_encoding TO 'utf8';
ALTER ROLE posuser SET default_transaction_isolation TO 'read committed';
ALTER ROLE posuser SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE posdb TO posuser;

Run:

python manage.py migrate
python manage.py runserver

✅ Django backend is ready!
Step 2: Set Up Frontend (Next.js + Tailwind)
1. Create Next.js App

npx create-next-app frontend with-tailwindcss

npm run dev

