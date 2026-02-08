#!/bin/bash
# Automated startup script for Mac/Linux
# This script starts both the backend and frontend servers

echo ""
echo "========================================"
echo "  ERP System Startup"
echo "========================================"
echo ""

# Start Backend in background
echo "Starting Backend Server (Python Flask API)..."
python Backend/app.py &
BACKEND_PID=$!

# Wait for backend to start
sleep 2

# Start Frontend in background
echo "Starting Frontend Server (HTTP Server)..."
python serve_frontend.py &
FRONTEND_PID=$!

# Wait a moment to let both servers start
sleep 2

echo ""
echo "========================================"
echo "  System Started Successfully!"
echo "========================================"
echo ""
echo "Open your browser to:"
echo "  http://127.0.0.1:8000/login.html"
echo ""
echo "Login with:"
echo "  Username: admin"
echo "  Password: admin123"
echo ""
echo "Backend API: http://127.0.0.1:5000"
echo ""
echo "Press Ctrl+C to stop both servers"
echo "========================================"
echo ""

# Wait for user to press Ctrl+C
wait

# Cleanup on exit
kill $BACKEND_PID 2>/dev/null
kill $FRONTEND_PID 2>/dev/null
echo "Servers stopped."
