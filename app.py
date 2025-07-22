from flask import Flask, render_template
from flask_socketio import SocketIO, emit
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'frostborn_prophecy_secret_key'
socketio = SocketIO(app, cors_allowed_origins="*")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/players')
def players():
    return render_template('players.html')

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

@socketio.on('message')
def handle_message(data):
    timestamp = datetime.now().strftime('%H:%M:%S')
    emit('message', {
        'message': data['message'],
        'username': data.get('username', 'Anonymous'),
        'timestamp': timestamp
    }, broadcast=True)

@socketio.on('connect')
def handle_connect():
    emit('message', {
        'message': 'A new adventurer has joined the chat!',
        'username': 'System',
        'timestamp': datetime.now().strftime('%H:%M:%S')
    }, broadcast=True)

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000, debug=True)