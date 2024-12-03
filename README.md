# Telegram Group Deleted Accounts Cleaner

A Python script to analyze and optionally remove deleted accounts from Telegram groups/channels.

## Features

- Count total members
- Detect deleted accounts
- Calculate percentage of deleted accounts
- Optional removal of deleted accounts

## Installation

```bash
# Create virtual environment
python -m venv venv

# Activate
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

# Install dependencies
pip install telethon
```

## Configuration

1. Get API credentials from https://my.telegram.org
2. Set the following variables in script:
   - `api_id`
   - `api_hash`
   - `channel_username`

## Usage

Analysis only:
```bash
python tg-group-members-cleaner.py
```

Analysis and removal of deleted accounts:
```bash
python tg-group-members-cleaner.py --rm
```

## Requirements

- Python 3.7+
- Telethon

## Note

You need to be an admin of the group/channel to remove deleted accounts.
