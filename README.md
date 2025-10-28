# DCFM Caseflow Django Project

This repository contains the Differentiated Case Flow Management demo built with Django. It provisions sample judges, benches, and hearing slots so you can explore the scheduling workflow locally without any external services.

## Getting Started

1. **Create a virtual environment**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # Windows: .venv\Scripts\activate
   ```
2. **Install dependencies**
   ```bash
   pip install -r dcfm_caseflow_texts/requirements.txt
   ```
3. **Apply migrations**
   ```bash
   cd dcfm_caseflow_texts
   python manage.py migrate
   ```
4. **(Optional) Seed demo data**
   ```bash
   python manage.py seed_caseflow
   ```
5. **Run the development server**
   ```bash
   python manage.py runserver
   ```
6. Visit http://127.0.0.1:8000/ in your browser.

## Project Layout
- `dcfm_caseflow_texts/` – Django project root containing apps, templates, and management commands.
- `cases/` – Models for case intake and scheduling metadata.
- `scheduling/` – Bench, judge, and slot models plus the `seed_caseflow` management command.
- `templates/` – HTML templates served by Django views.
- `static/` – CSS assets referenced by the templates.

## Seeding Details
Running `python manage.py seed_caseflow` will:
- Create sample judges and benches.
- Generate a rolling calendar of hourly bench slots.
- Insert time-standard rules to prioritize cases.

The command can be re-run safely; it performs idempotent upserts for demo data.

## Testing & Maintenance
- `python manage.py check` – Verify project configuration and Django apps.
- `python manage.py test` – Execute the Django test suite (currently placeholder).
- `python manage.py migrate` – Apply database schema changes.

For a fresh start, delete `db.sqlite3` (ignored by git) and rerun migrations and seed data.
