# Workout Tracker

## Overview

This Python application leverages the power of the Nutritionix API for natural language processing (NLP) to interpret exercise descriptions input by the user. It then logs exercise data, including type, duration, and calories burned, into a Google Sheet for easy tracking and visualization.

## Output


https://github.com/sarvesh-2109/Workout-Tracker/assets/113255836/0a242365-dab4-42a0-8e1f-9f2e27e9d2b9



## Features

- Natural Language Processing: Understands plain English input to identify exercise activities.
- Integration with Nutritionix API: Fetches detailed exercise data including duration and calorie count.
- Google Sheets Logging: Automatically logs each exercise session with date, time, duration, and calories burned.
- Environment Variables: Ensures security by storing sensitive information like API keys and access tokens.

## Prerequisites

- Python 3
- Requests library
- An account and API key from Nutritionix
- Access to Google Sheets API and a setup Google Sheet
- pytz library for timezone adjustments

## Setup and Installation

1. Clone this repository to your local machine.
   ```bash
   git clone https://github.com/yourusername/exercise-tracker.git
   ```
2. Install the required Python packages.
   ```bash
   pip install requests pytz
   ```
3. Obtain your API keys from Nutritionix and set up your Google Sheet.
4. Store your API keys, App ID, and Google Sheet access token as environment variables for `APP_ID`, `API_KEY`, `TOKEN`, `NUTRITIONIX_ENDPOINT`, and `SHEETY_ENDPOINT`.

## Configuration

Set up your environment variables:
- `APP_ID`: Your Nutritionix App ID.
- `API_KEY`: Your Nutritionix API key.
- `TOKEN`: Your authorization token for Google Sheets API.
- `NUTRITIONIX_ENDPOINT`: Endpoint URL for the Nutritionix API.
- `SHEETY_ENDPOINT`: Endpoint URL for your Google Sheets API.

## Usage

Run the script and follow the prompt to input your exercise activity in plain English:

```bash
python exercise_tracker.py
```

The application will process your input, fetch the relevant exercise data from Nutritionix, and log the details in your configured Google Sheet.

## Disclaimer

This project uses third-party APIs and services. Ensure you comply with their terms of use. Keep your API keys and tokens secure and do not expose them publicly.

## Contribution

Feel free to fork this project, submit pull requests, or suggest new features. Contributions are welcome!
