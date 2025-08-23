# Habit Tracker App

A simple habit tracking application built with Streamlit and SQLAlchemy, featuring AI-powered motivational messages.

## Features

- Track daily habits
- View progress with charts and visualizations
- Get AI-generated motivational messages
- Store data persistently with SQLAlchemy database
- Clean and user-friendly interface

## Installation

1. Clone this repository
2. Create a virtual environment:
   ```
   python -m venv venv
   ```
3. Activate the virtual environment:
   - Windows: `venv\Scripts\activate`
   - Mac/Linux: `source venv/bin/activate`
4. Install required packages:
   ```
   pip install -r requirements.txt
   ```
5. Create `.streamlit/secrets.toml` file and add your API key:
   ```
   AIMLAPI_KEY = "your_api_key_here"
   ```

## Running the App

```
streamlit run main.py
```

Open your browser and go to `http://localhost:8501`

## Project Structure

```
habit_tracker/
├── main.py              # Main app file
├── app/
│   ├── config.py        # Configuration
│   ├── database.py      # Database models
│   ├── ai_integration.py # AI features
│   └── utils/
│       └── viz.py       # Visualizations
├── requirements.txt     # Dependencies
└── README.md           # This file
```

## Dependencies

- streamlit
- sqlalchemy
- plotly
- pandas
- openai

See `requirements.txt` for complete list.

## Usage

1. Add new habits you want to track
2. Mark habits as complete each day
3. View your progress in the analytics section
4. Get motivational messages powered by AI

## Configuration

You need an API key from aimlapi.com to use the AI features. Add it to your `.streamlit/secrets.toml` file.

## License

MIT License
