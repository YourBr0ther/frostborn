#!/usr/bin/env python3
"""
WSGI entry point for gunicorn deployment
"""

from app import socketio

# The socketio object IS the WSGI application
application = socketio

if __name__ == "__main__":
    # For direct execution, run with the built-in server
    from app import app
    socketio.run(app, host='0.0.0.0', port=5000)