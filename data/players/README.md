# Player Character Data

This directory contains JSON files for each player character in the campaign.

## File Format

Each player should have their own JSON file (e.g., `player_name.json`) with the following structure:

```json
{
  "name": "Character Name",
  "player": "Player's Real Name",
  "class": "Character Class",
  "level": 5,
  "race": "Character Race",
  "portrait": null,
  "backstory": "Character's background story...",
  "abilities": [
    {
      "name": "Ability Name",
      "icon": "fas fa-icon-name",
      "description": "Brief description"
    }
  ],
  "recent_quote": {
    "text": "Memorable quote",
    "context": "When/where it was said"
  },
  "stats": {
    "ac": 15,
    "hp": 45,
    "speed": 30
  },
  "background": "D&D Background",
  "alignment": "Character Alignment",
  "active": true
}
```

## Managing Characters

- **Add new character**: Create a new `.json` file in this directory
- **Remove character**: Set `"active": false` or delete the file
- **Update character**: Edit the JSON file and refresh the website
- **Character portraits**: Add image URL to `"portrait"` field

## FontAwesome Icons

Use FontAwesome classes for ability icons:
- `fas fa-sword` - Combat abilities
- `fas fa-magic` - Magical abilities  
- `fas fa-shield-alt` - Defensive abilities
- `fas fa-eye` - Perception/stealth
- `fas fa-heart` - Healing abilities
- `fas fa-bolt` - Quick actions

## Example Files

See the sample files in this directory for reference formatting.