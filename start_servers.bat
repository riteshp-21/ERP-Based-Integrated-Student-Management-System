@echo off
REM Automated startup script for Windows
REM This script starts both the backend and frontend servers

echo.
echo ========================================
echo   ERP System Startup
echo ========================================
echo.

REM Start Backend in a new window
echo Starting Backend Server (Python Flask API)...
start "ERP Backend" cmd /k python Backend/app.py

REM Wait a moment for backend to start
timeout /t 2 /nobreak

REM Start Frontend in a new window
echo Starting Frontend Server (HTTP Server)...
start "ERP Frontend" cmd /k python serve_frontend.py

echo.
echo ========================================
echo   System Started Successfully!
echo ========================================
echo.
echo Open your browser to:
echo   http://127.0.0.1:8000/login.html
echo.
echo Login with:
echo   Username: admin
echo   Password: admin123
echo.
echo Backend API: http://127.0.0.1:5000
echo.
echo Close these windows to stop the servers.
echo ========================================
echo.
pause
