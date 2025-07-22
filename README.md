# ❄️ Frostborn Prophecy Campaign Website 🔥

A beautiful, interactive Flask-based website for your D&D campaign featuring dark mode, medieval theming, and real-time chat functionality.

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Python](https://img.shields.io/badge/python-3.11+-green.svg)
![Flask](https://img.shields.io/badge/Flask-2.3.3-red.svg)

## ✨ Features

- **🌙 Dark/Light Mode Toggle** - Medieval-themed with atmospheric colors
- **📱 Responsive Design** - Mobile-friendly Bootstrap 5 layout
- **⚔️ D&D-Themed UI** - Gold, bronze, silver accents with fantasy styling
- **🎭 Character Management** - Player bios, relationships, and gear tracking
- **👥 NPC Library** - Faction-organized NPCs with relationship tracking
- **📜 Session Archives** - Recording embeds and detailed summaries
- **🗺️ Interactive World Map** - Clickable locations with lore
- **🔮 Prophecy Board** - Fragment collection and theory tracking
- **💬 Real-time Chat** - WebSocket-powered with dice roller
- **📈 Progress Tracking** - Campaign timeline and faction relationships
- **🐉 Bestiary** - Creature encounters and stats
- **⚡ Fast & Lightweight** - Optimized for quick loading

## 🚀 Quick Start

### Local Development

```bash
# Clone the repository
git clone git@github.com:YourBr0ther/frostborn.git
cd frostborn

# Install dependencies
pip install -r requirements.txt

# Run the application
python app.py

# Visit http://localhost:5000
```

### Docker Deployment

```bash
# Build the Docker image
docker build -t frostborn-site .

# Run the container
docker run -p 5000:5000 frostborn-site

# Visit http://localhost:5000
```

## 📁 Project Structure

```
frostborn_site/
├── app.py                  # Main Flask application with WebSocket support
├── requirements.txt        # Python dependencies
├── Dockerfile             # Container configuration
├── README.md              # This file
├── .gitignore            # Git ignore rules
├── templates/            # Jinja2 HTML templates
│   ├── base.html         # Base template with navigation & theme toggle
│   ├── index.html        # Homepage with hero banner
│   ├── players.html      # Character bios and party sheet
│   ├── npcs.html         # NPC library with factions
│   ├── sessions.html     # Session recordings & summaries
│   ├── lore.html         # World lore and timeline
│   ├── timeline.html     # Campaign timeline
│   ├── factions.html     # Faction tracker
│   ├── prophecy.html     # Interactive prophecy board
│   ├── map.html          # Interactive world map
│   ├── bestiary.html     # Creature encounters
│   ├── items.html        # Artifacts and player gear
│   ├── resources.html    # House rules and survival guide
│   ├── gallery.html      # Art and memorable moments
│   └── chat.html         # Real-time chat with dice roller
└── static/
    └── css/
        └── style.css     # Custom D&D-themed styles with dark mode
```

## 🎨 Theme Customization

The website features a comprehensive theming system with CSS variables:

### Light Theme (Parchment & Medieval)
- Parchment backgrounds
- Gold, silver, bronze accents
- Warm color palette

### Dark Theme (Atmospheric & Fantasy)  
- Deep medieval blacks
- Glowing gold highlights
- Enhanced shadows and depth

Toggle between themes using the moon/sun button in the navigation bar!

## 🔧 Configuration

### Environment Variables
Create a `.env` file for production settings:

```env
FLASK_ENV=production
SECRET_KEY=your-secret-key-here
```

### WebSocket Features
- Real-time party chat
- Integrated dice roller (d4, d6, d8, d10, d12, d20)
- Connection status indicators
- Message history

## 📖 Usage Guide

### Adding Campaign Content

1. **Player Characters**: Edit `templates/players.html` to add character details
2. **NPCs**: Update `templates/npcs.html` with your campaign's NPCs
3. **Session Summaries**: Add session recaps in `templates/sessions.html`
4. **World Lore**: Customize `templates/lore.html` with your world's history
5. **Prophecy Fragments**: Update `templates/prophecy.html` as players discover clues

### Customizing the Theme

Edit `static/css/style.css` to modify:
- Color schemes (CSS variables in `:root` and `[data-theme=\"dark\"]`)
- Fonts and typography
- Card styles and animations
- Button designs

## 🐳 Docker Deployment

The included Dockerfile creates a lightweight, production-ready container:

- Based on `python:3.11-slim`
- Non-root user for security
- Optimized for fast startup
- Exposes port 5000

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🎲 Campaign Inspiration

Perfect for:
- **Epic Fantasy Campaigns** - Dragons, magic, and ancient prophecies
- **Political Intrigue** - Faction relationships and alliance tracking  
- **Exploration Campaigns** - Interactive maps and location discovery
- **Long-term Campaigns** - Session archives and character development
- **Online/Hybrid Games** - Real-time chat and remote participation

---

**"When the sun fades, who will shape the world's fate?"** ❄️🔥

Built with ❤️ for the D&D community