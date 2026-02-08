# ERP-based Integrated Student Management System

Lightweight, low-cost ERP for college administration — admissions, fee collection, hostel allocation, and exam records. Designed to be deployable on a small VM or laptop and to integrate with common office tools.

## Background
Many public colleges cannot afford full commercial ERP suites. This project demonstrates how a cohesive, low-cost solution can be built by connecting web forms, a central database, and lightweight automation to provide a single source of truth with minimal staff training.

## Features (implemented)
- **Secure authentication**: Flask-Login session management with bcrypt-hashed passwords
- **Role-based access control (RBAC)**: Admin, staff, and student roles with endpoint protection
- Admission intake form (web) that creates a `student_mastertb` record and auto-generates student login credentials.
- Fee payment recording with receipt number generation.
- Hostel allocation form and allocation records.
- Examination record entry and simple grade calculation.
- Admin dashboard showing total students, total fees, and hostel occupancy (live updates every 5s).
- Student portal showing personal fees, hostel allocation, and exam records.
- Authentication endpoint with bcrypt-hashed passwords and role support (admin/staff/student).
- Student self-registration page that posts to the admission endpoint.
- Basic frontend UI under `Frontend/` (static HTML + shared `style.css`).

## Project layout
- `Backend/` — Flask backend application (`app.py`) and helper scripts (`create_admin.py`, `set_admin_password.py`).
- `Frontend/` — static HTML pages and `style.css`.
- `Database/` — `student_erp_db.sql` MySQL dump for schema and seed data.

## Quick start (development)
Prerequisites
- Python 3.10+ installed
- MySQL server running locally (or adjust DB settings in `Backend/app.py`)

### Easiest Way: Use Startup Script

**Windows:**
```bash
start_servers.bat
```

**Mac/Linux:**
```bash
bash start_servers.sh
```

Then open: `http://127.0.0.1:8000/login.html`

### Manual Setup

1. **Create the database** from the SQL dump:

```sql
CREATE DATABASE student_erp_db;
USE student_erp_db;
SOURCE Database/student_erp_db.sql;
```

2. **Install Python dependencies:**

```bash
pip install -r requirements.txt
```

3. **(Optional) Create/reset admin user:**

```bash
python Backend/create_admin.py    # creates admin if missing
python Backend/set_admin_password.py  # sets password to admin123
```

4. **Start Terminal 1 - Backend:**

```bash
python Backend/app.py
```
Backend runs on: `http://127.0.0.1:5000`

5. **Start Terminal 2 - Frontend Web Server:**

```bash
python serve_frontend.py
```
Frontend runs on: `http://127.0.0.1:8000`

6. **Open in Browser:**

Navigate to: `http://127.0.0.1:8000/login.html`

**Login with:** `admin` / `admin123`

> ⚠️ **Important**: Use the HTTP server (port 8000) instead of opening HTML files directly. Opening `file://` paths causes CORS issues.

See `QUICK_START.md` for detailed troubleshooting and `RBAC_IMPLEMENTATION.md` for authentication details.

## API Endpoints (summary)
- `GET /` — health check.
- `POST /admission` — create student admission record (form POST fields: `full_name`, `dob`, `gender`, `department`, `year`, `email`, `mobile`). Returns an HTML snippet showing Student ID and password (DOB).
- `POST /fee` — record fee payment (fields: `student_id`, `fee_type`, `amount`).
- `POST /hostel` — allocate hostel (fields: `student_id`, `hostel_name`, `room_no`).
- `POST /exam` — save exam record (fields: `student_id`, `semester`, `subject`, `marks`).
- `POST /login` — login (form fields: `username`, `password`) — returns JSON `{status: 'success'|'fail', role?: 'admin'|'student'}`.
- `GET /dashboard` — JSON summary metrics for admin dashboard.
- `GET /student_dashboard?student_id=<id>` — student-specific JSON summary.

> Note: Endpoints currently accept `application/x-www-form-urlencoded` form POSTs from the static frontend.

## Database schema
See `Database/student_erp_db.sql` for the full schema. Core tables:
- `student_mastertb(student_id, full_name, dob, department, year, email, mobile, admission_date)`
- `userstb(user_id, username, password, role, status)` — passwords stored as bcrypt strings
- `fee_detailstb`, `hostel_allocationtb`, `exam_recordstb`

## Security & operational notes
- Passwords are hashed with `bcrypt` before storage. Keep `create_admin.py` and `set_admin_password.py` offline or remove after use.
- Run behind TLS (nginx/letsencrypt) in production.
- Use parameterized queries (already used) to avoid SQL injection.
- Configure regular database backups; export `Database/` periodically or use automated dumps.

## Next improvements (suggested roadmap)
- Add RBAC middleware and login session management (Flask-Login / JWT).
- Return JSON from `/admission` and auto-login students after registration.
- PDF receipt generation and email delivery (SMTP), or integrate with Google Workspace for receipts/backup.
- WebSocket or SSE for live dashboard updates.
- Add unit tests and a Dockerfile for repeatable deployment.

## Contributing / Demo notes
- This repo is designed as a hackathon/demo project. The UI is intentionally simple so workflows can be showcased quickly.
- For a demo: show admission → generated credentials → login → pay fee → see dashboard update.

## Contact
If you want me to implement any of the next steps (RBAC, PDF/email receipts, live dashboard, Dockerization), tell me which one and I will add an implementation plan and start coding.
