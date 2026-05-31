# Welcome to Ravel's Github Repository! 

Here are the programming files, code, scripts, and how to set up the code.

## TL;DR
- **What it is:** Web-based music streaming app (Spotify-style) with listener & musician portals
- **AI feature:** “Debussy” chat assistant for mood-based playlist creation and discovery support
- **Stack:** Flask, SQLite, HTML/CSS/JS, OpenAI Python SDK (DashScope/Qwen model endpoint), PythonAnywhere
- **Key features:** playlist management, uploads (.mp3), listening history, AI chat sessions

## Contributors

| Name   | Contributions        | GitHub |
|--------|-------------|--------|
| Aaron Novesteras  | Lead Architect & AI Integration: Architected the Flask backend application and designed the 9-table SQLite relational database schema to manage user states and track metadata. Engineered the "Debussy" agent using the DashScope (Qwen3.5-plus) API, crafting dynamic system prompts to trigger targeted discovery algorithms based on user listening history. Directed the agentic implementation of the full stack (Python, HTML, CSS, JS) by translating high-level system requirements into deployable code.   | [@Paradoxidus](https://github.com/Paradoxidus) |
| Rexter Gonzales  | Documentation & QA: Authored the comprehensive technical manual, structured the GitHub repository documentation, and executed quality assurance testing across the application.  | n/a|
| James Bongcac   | UI/UX & QA: Directed user interface design paradigms, verified user experience flows for the web-based music player and library views, and assisted in frontend QA testing.  | [@YuanSol30](https://github.com/YuanSol30) |

## Deployment Link (May be closed due to limited-tier selection)
https://melodymelon23.pythonanywhere.com/login

**If you are interested in hosting this your own, then you can refer to Part 4B.**

## 1. What is Ravel?
Ravel is a web-based music streaming application similar to Spotify, YouTube Music, Apple Music, etc. Its friendly UI helps users navigate and create their own musical paradise hub with the tap of their fingertips without the unnecessary excruciating ads. All for a reasonable price! Blending AI-integrated systems and artist-focus algorithms, Ravel ensures that everyone has a voice!

### a. What makes us different from other musical streaming apps?
Since Ravel is a web-based music streaming application similar to Spotify, YouTube Music, Apple Music, etc., it offers a unique perspective in listener-artist philosophy! Due to multiple user complaints, new and fresh artists observe that their music receive low stream counts which is likely due to mainstream artists receiving more attention than necessary. Based on their music philosophy and themes, those would act as inputs for the algorithm to ensure that their music would go to the right people who are interested in those themes. They would also be heard by users who decide to enable fresh artist spolights! 

Because of user complaints, new and fresh artists observe that their music receive low stream counts which is likely due to mainstream artists receiving more attention than necessary. Based on their music philosophy and themes, those would act as inputs for the algorithm to ensure that their music would go to the right people who are interested in those themes. They would also be heard by users who decide to enable fresh artist spolights! 

## 2. Core Features
Agentic AI Assistant (Debussy): Ravel features an integrated conversational AI agent named Debussy that personalizes the listening experience, creates custom playlists based on user mood, and actively prioritizes underrepresented artists.
- Listener & Musician Portals: Users can register as standard listeners to discover music, or as musicians to upload and distribute their own .mp3 tracks.
- Dynamic Library Management: Users can create custom playlists, save tracks, and manage their listening history seamlessly.
- Algorithmic Discovery: The platform tracks user listening habits to generate customized suggestions and highlights artists with lower stream counts to democratize exposure.

## 3. Tech Stack
- Frontend: HTML, CSS, JavaScript (Custom UI with interactive player overlays and modals).
- Backend: Python with the Flask web framework.
- Database: SQLite3 for managing users, artists, tracks, playlists, and AI chat sessions.

### 4. AI Assistant (Debussy)
Debussy is a conversational assistant integrated into the app.
- **Client:** OpenAI Python SDK (OpenAI-compatible API interface)
- **Provider/Endpoint:** Alibaba Cloud DashScope
- **Model:** Qwen (e.g., qwen3.5-plus)
- **Config:** requires `DASHSCOPE_API_KEY` in a `.env` file

## 4A. Local Setup & Installation
Follow these steps to get Ravel running on your local machine.

### a. Prerequisites
- Python 3.8+ installed on your system.
- Basic knowledge of running terminal commands.

### b. Step-by-Step Guide
1. Clone the repository:
```
git clone https://github.com/Paradoxidus/group9-ravel-appdevproject.git
cd group9-ravel-appdevproject
```
2. Install the required dependencies:
You will need Flask, python-dotenv, and the OpenAI client.

```
pip install Flask python-dotenv openai
```
3. Set up Environment Variables:
Create a .env file in the root directory of the project and add your DashScope API key:

```
DASHSCOPE_API_KEY=your_api_key_here
```
4. Initialize the Database:
Run the database setup script. This will create the ravel_database.db file and populate it with dummy artists and tracks for testing.

```
python setup_db.py
```
5. Run the Application:
Start the Flask development server.

```
python app.py
```

6. Access Ravel:
Open your web browser and go to http://127.0.0.1:5000 to start using the app.


## 4B. Deployment
Ravel is webhosted using PythonAnywhere due to its free hosting services compared to other webhosting alternatives.

### 1. Upload your files
1. Create a PythonAnywhere account and log into your Dashboard.

2. Go to the Files tab.

3. Upload the entire Ravel project folder into a directory (e.g., `/home/yourusername/mysite`). Ensure `app.py`, `setup_db.py`, and the templates/static folders are all present.

4. Upload your `.env` file containing your `DASHSCOPE_API_KEY` into this same directory.

### Step 2: Set Up a Virtual Environment
1. Go to the Consoles tab and open a new Bash console.

2. Create and activate a virtual environment by running:
```
mkvirtualenv --python=/usr/bin/python3.10 ravel-env
```

3. Install the required dependencies inside the console:
```
pip install Flask python-dotenv openai
```

4. While still in the console, initialize your database:
```
cd /home/yourusername/mysite
python setup_db.py
```
### Step 3: Configure the Web App
1. Navigate to the Web tab and click Add a new web app.

2. Select Manual Configuration (do not select Flask) and choose the Python version that matches your virtual environment (e.g., Python 3.10).

3. Scroll down to the Virtualenv section and enter the path to the environment you just created:
```
/home/yourusername/.virtualenvs/ravel-env
```
4. Scroll to the Code section and set the Source code directory to:
```
/home/yourusername/mysite
```

### Step 4: Edit the WSGI File
PythonAnywhere uses a WSGI file to connect the web server to your Flask application.

1. Still in the Web tab, click the link to your WSGI configuration file (it will look like `/var/www/yourusername_pythonanywhere_com_wsgi.py`).

2. Delete the boilerplate code inside and replace it with the following configuration to ensure your environment variables and Flask app load correctly:
```
import sys
import os
from dotenv import load_dotenv

# 1. Expand Python classes path with your app's path
project_home = '/home/yourusername/mysite'
if project_home not in sys.path:
    sys.path = [project_home] + sys.path

# 2. Load environment variables from your .env file
load_dotenv(os.path.join(project_home, '.env'))

# 3. Import the Flask app
from app import app as application
```
**(Note: Replace yourusername with your actual PythonAnywhere username and mysite with your specific folder name if different).**

### Step 5: Reload and Launch
Go back to the Web tab and click the green Reload button at the top. Your instance of Ravel should now be live at https://yourusername.pythonanywhere.com!

*** This covers everything needed to get Ravel live. Let me know if you'd like to add a "Future Features" or "Contributing" section to round out the bottom of the repository!

### 6. Future Roadmap & Known Limitations and Bugs
Ravel was developed as an exploratory application development project. While fully functional, there are several areas planned for future expansion:
- Advanced AI Context: Currently, Debussy handles immediate conversational context. Future updates would implement a more robust Retrieval-Augmented Generation (RAG) pipeline to give the assistant deeper memory of a user's long-term listening history.
- Expanded Audio Support: The upload feature is currently limited to .mp3 files. Adding support for .wav and .flac with automatic compression is a priority.
- Enhanced Recommendation Algorithm: The current algorithm tracks play counts and genre tags. The goal is to transition to a more complex machine-learning model to analyze audio features directly for better underrepresented artist matching.
- Production Database: Migrating from the current SQLite3 setup to a more scalable solution like PostgreSQL for handling larger concurrent user bases.
- Known bugs involve Debussy (AI) failing to add songs based on theme. 
