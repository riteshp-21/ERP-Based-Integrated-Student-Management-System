# Quick Start Guide

## Starting the ERP System

### Option 1: Automated Startup (Recommended)

**For Windows users:**
```batch
# Run both servers at once
start_servers.bat
```

**For Mac/Linux users:**
```bash
# Run both servers at once
bash start_servers.sh
```

### Option 2: Manual Startup

**Terminal 1 - Start Backend (API)**
```bash
python Backend/app.py
```
Backend runs on: `http://127.0.0.1:5000`

**Terminal 2 - Start Frontend (Web Server)**
```bash
python serve_frontend.py
```
Frontend runs on: `http://127.0.0.1:8000`

### Option 3: Direct File Access (Not Recommended - CORS Issues)
~~Do NOT open Frontend/login.html directly in browser (file:// protocol causes CORS errors)~~

## Access the System

1. **Open your browser** to: `http://127.0.0.1:8000/login.html`
2. **Login with admin account**:
   - Username: `admin`
   - Password: `admin123`
3. **Or register as a new student** using the registration link

## System URLs

- **Login Page**: http://127.0.0.1:8000/login.html
- **Admin Dashboard** (after login): http://127.0.0.1:8000/dashboard.html
- **Student Dashboard** (after login): http://127.0.0.1:8000/student_dashboard.html
- **Backend API**: http://127.0.0.1:5000

## Important Notes

✅ **Always use HTTP server** - Do not open HTML files directly (file:// protocol)

✅ **Keep both terminals open** - Frontend server and Backend API must run together

✅ **Check browser console** if you encounter errors - Press F12, go to Console tab for details

✅ **Clear cookies** if login issues persist - Settings → Privacy → Clear Cookies for 127.0.0.1

## Troubleshooting

### "Server error — check backend" on login
- Ensure `python Backend/app.py` is running
- Ensure `python serve_frontend.py` is running on port 8000
- **Try the connection test**: Open http://127.0.0.1:8000/test_connection.html and click "Run All Tests"
- Open browser DevTools (F12) → Console for detailed error messages
- Check Network tab in DevTools to see if POST request to `/login` is being made

### Cannot connect to frontend
- Ensure `python serve_frontend.py` is running  
- Try `http://127.0.0.1:8000` (not localhost)
- Check if port 8000 is already in use:
  - **Windows**: `netstat -ano | findstr :8000`
  - **Mac/Linux**: `lsof -i :8000`

### Cannot connect to backend
- Ensure `python Backend/app.py` is running
- Check if port 5000 is already in use:
  - **Windows**: `netstat -ano | findstr :5000`
  - **Mac/Linux**: `lsof -i :5000`
- Test backend directly: Open http://127.0.0.1:5000/ in browser (should show "ERP Backend Connected Successfully!")

### Session issues
- Clear browser cookies for 127.0.0.1:
  1. Open DevTools (F12)
  2. Go to "Application" → "Cookies"
  3. Delete all cookies for 127.0.0.1
- Clear localStorage:
  1. Open DevTools (F12)
  2. Go to "Application" → "Local Storage"
  3. Clear all items
- Close and reopen browser
- Restart both servers

## Default Credentials

- **Admin**
  - Username: `admin`
  - Password: `admin123`

- **Student** (Example - auto-generated on registration)
  - Username: {student_id}
  - Password: {date_of_birth} (as entered during registration)

---

Need help? Check `README.md` or `RBAC_IMPLEMENTATION.md` for more details.
