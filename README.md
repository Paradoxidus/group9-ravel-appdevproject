# Welcome to Ravel's Github Repository! 

Here are the programming files, code, scripts, and how to set up the code, 

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
- AI Integration: OpenAI Python client connected to the DashScope API (Qwen3.5-plus model) for the Debussy assistant. **Take note**: DashScope API is part of the Alibaba Cloud. You may need to sign up to use their services. You may also use their free trial to get almost a million credits!
- Deployment: PythonAnywhere.

## 4A. Local Setup & Installation
Follow these steps to get Ravel running on your local machine.

### a. Prerequisites
- Python 3.8+ installed on your system.
- Basic knowledge of running terminal commands.

### b. Step-by-Step Guide
1. Clone the repository:
```
git clone https://github.com/yourusername/ravel.git
cd ravel
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
