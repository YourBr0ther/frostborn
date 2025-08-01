from flask import Flask, render_template, jsonify
from flask_socketio import SocketIO, emit
from datetime import datetime
import json
import os
import glob

app = Flask(__name__)
app.config['SECRET_KEY'] = 'frostborn_prophecy_secret_key'
socketio = SocketIO(app, cors_allowed_origins="*", async_mode='threading')

# Data storage configuration
MESSAGES_FILE = 'chat_messages.json'
PLAYERS_DIR = 'data/players'

def load_players():
    """Load all player character data from JSON files"""
    players = []
    
    # Create players directory if it doesn't exist
    if not os.path.exists(PLAYERS_DIR):
        os.makedirs(PLAYERS_DIR, exist_ok=True)
        return players
    
    # Load all JSON files in the players directory
    for file_path in glob.glob(os.path.join(PLAYERS_DIR, '*.json')):
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                player_data = json.load(f)
                # Only include active players
                if player_data.get('active', True):
                    players.append(player_data)
        except (json.JSONDecodeError, IOError, KeyError) as e:
            print(f"Error loading player file {file_path}: {e}")
            continue
    
    # Sort players by name for consistent display
    players.sort(key=lambda x: x.get('name', ''))
    return players

def load_messages():
    """Load messages from JSON file"""
    if os.path.exists(MESSAGES_FILE):
        try:
            with open(MESSAGES_FILE, 'r', encoding='utf-8') as f:
                return json.load(f)
        except (json.JSONDecodeError, IOError):
            return []
    return []

def save_message(message_data):
    """Save a single message to JSON file"""
    messages = load_messages()
    messages.append(message_data)
    
    # Keep only last 500 messages to prevent file from growing too large
    if len(messages) > 500:
        messages = messages[-500:]
    
    try:
        with open(MESSAGES_FILE, 'w', encoding='utf-8') as f:
            json.dump(messages, f, ensure_ascii=False, indent=2)
    except IOError:
        print("Error saving message to file")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/players')
def players():
    players_data = load_players()
    return render_template('players.html', players=players_data)

@app.route('/npcs')
def npcs():
    return render_template('npcs.html')

@app.route('/sessions')
def sessions():
    return render_template('sessions.html')

@app.route('/lore')
def lore():
    return render_template('lore.html')

@app.route('/timeline')
def timeline():
    return render_template('timeline.html')

@app.route('/factions')
def factions():
    return render_template('factions.html')

@app.route('/prophecy')
def prophecy():
    return render_template('prophecy.html')

@app.route('/gallery')
def gallery():
    return render_template('gallery.html')

@app.route('/map')
def map():
    return render_template('map.html')

@app.route('/bestiary')
def bestiary():
    return render_template('bestiary.html')

@app.route('/items')
def items():
    return render_template('items.html')

@app.route('/resources')
def resources():
    return render_template('resources.html')

@app.route('/chat')
def chat():
    return render_template('chat.html')

@app.route('/api/messages')
def get_messages():
    """API endpoint to get chat messages"""
    messages = load_messages()
    return jsonify(messages)

@socketio.on('message')
def handle_message(data):
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    display_timestamp = datetime.now().strftime('%H:%M:%S')
    
    message_data = {
        'message': data['message'],
        'username': data.get('username', 'Anonymous'),
        'timestamp': timestamp,
        'display_timestamp': display_timestamp
    }
    
    # Save message to file
    save_message(message_data)
    
    # Broadcast to all connected clients
    emit('message', {
        'message': message_data['message'],
        'username': message_data['username'],
        'timestamp': display_timestamp
    }, broadcast=True)

@socketio.on('connect')
def handle_connect():
    # Simply acknowledge connection without broadcasting a message
    # This prevents "new adventurer joined" spam on page reloads
    print(f"Client connected at {datetime.now().strftime('%H:%M:%S')}")
    pass

# WSGI application - exported for external servers like gunicorn
application = socketio

if __name__ == '__main__':
    # Check if running in production (Docker) or development
    is_production = os.getenv('FLASK_ENV') == 'production'
    
    if is_production:
        # Production mode - use allow_unsafe_werkzeug for Docker deployment
        socketio.run(app, host='0.0.0.0', port=5000, debug=False, allow_unsafe_werkzeug=True)
    else:
        # Development mode
        socketio.run(app, host='0.0.0.0', port=5000, debug=True)