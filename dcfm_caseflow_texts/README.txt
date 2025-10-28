# Original path: README.md


# DCFM Caseflow (Django + SQLite)

A simple Differentiated Case Flow Management app:
- Case intake (with parties basic fields inline)
- Compute priority & auto-schedule to earliest slot within SLA
- Daily Cause List (page + API)
- Seed command for judges, benches, slots, and time standards
- Simple Django templates (no React) so it's easy to deploy

## Quick Start
```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py seed_caseflow
python manage.py runserver
```
Open http://127.0.0.1:8000

## Notes
- Uses SQLite by default (db.sqlite3 in project root)
- Time zone: Asia/Kolkata
- Minimal code aimed for clarity over features
