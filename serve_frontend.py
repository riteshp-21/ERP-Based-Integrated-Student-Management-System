#!/usr/bin/env python
"""
Simple HTTP server to serve static frontend files.
Run this to serve the Frontend folder on http://127.0.0.1:8000
"""

import http.server
import socketserver
import os
from pathlib import Path

# Change to Frontend directory
frontend_dir = Path(__file__).parent / "Frontend"
os.chdir(frontend_dir)

PORT = 8000
Handler = http.server.SimpleHTTPRequestHandler

print(f"Serving frontend from: {frontend_dir}")
print(f"Open your browser to: http://127.0.0.1:{PORT}/login.html")
print(f"Backend API: http://127.0.0.1:5000")
print("\nPress Ctrl+C to stop the server.")

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nServer stopped.")
