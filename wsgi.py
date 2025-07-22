#!/usr/bin/env python3
"""
WSGI entry point for gunicorn deployment
"""

from app import app, socketio

# Flask-SocketIO patches the Flask app to handle WebSocket upgrades
# The Flask app itself becomes the WSGI application
application = app

if __name__ == "__main__":
    # For direct execution, run with the built-in server
    socketio.run(app, host='0.0.0.0', port=5000)