# YouTube Shorts Automation

Automatically generates and uploads motivational YouTube Shorts using Python.

## Features

- Reads quotes from a text file
- Automatically keeps track of uploaded quotes
- Generates quote image
- Creates a vertical YouTube Short
- Adds background music
- Uploads directly to YouTube
- OAuth authentication
- Supports Windows Task Scheduler

## Tech Stack

- Python
- Pillow
- MoviePy
- YouTube Data API v3
- OAuth 2.0

## Project Structure
assets/
output/
main.py
create_image.py
create_video.py
upload_youtube.py
quotes.txt
current_index.txt

## Workflow
Read Quote
↓

Create Image
↓

Create Video
↓

Upload to YouTube
↓

Update Index


## Installation

```bash
git clone <repo>

pip install -r requirements.txt

python main.py
Note
Google OAuth credentials (client_secret.json) are intentionally excluded from this repository.


---

# Git Commands

```powershell
git init

git add .

git commit -m "Initial commit"

git branch -M main

git remote add origin YOUR_GITHUB_REPO

git push -u origin main
