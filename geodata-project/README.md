# Geodata Project: Google Geocoding API & Data Visualization

## Overview
This project demonstrates how to utilize the Google Geocoding API to clean up user-entered geographic locations, particularly university names, and then visualize the geocoded data on a Google Map.

## Prerequisites
Before running or contributing to this project, ensure that you have the following prerequisites:
* Python 3.x installed [(https://www.python.org/downloads/)](https://www.python.org/downloads/)
* A Google Cloud Platform account to obtain an API key [(https://cloud.google.com/)](https://cloud.google.com/)
* Internet access to make requests to the Google Geocoding API
* SQLite database support (usually included with Python)


## Getting Started
1. Clone the repository to your local machine.
2. Create a Google Cloud Platform project (if you don't have one) and obtain an API key for the Google Geocoding API. Follow the instructions provided by Google.
3. Set up your API key:
* Replace __'YOUR_API_KEY'__ in `geoload.py` with your actual API key.
4. Run the `geoload.py` script to populate the SQLite database with geocoded university location data.
5. Run the `geodump.py` script to export the data to a JavaScript file for visualization.
6. Open where.html in a web browser to visualize the data on a Google Map.


## Project Structure
The project structure is organized as follows:
* __geoload.py__: Python script for retrieving and geocoding university location data using the Google Geocoding API and storing it in an SQLite database.
* __geodump.py__: Python script for exporting geocoded data from the database to a JavaScript file.
* __where.data__: Input file containing university names.
* __geodata.sqlite__: SQLite database to store geocoded location data.
* __where.js__: a JavaScript list of lists that we have written to where,js by running geodump.py.
* __where.html__: HTML file for visualizing geocoded data on a Google Map.
* __README.md__: This documentation file.


## Usage
1. Populate the `where.data` file with university names (one per line) that you want to geocode and visualize.
2. Follow the "Getting Started" instructions to set up and run the project.
3. View the geocoded data on the Google Map visualization by opening `where.html` in a web browser.
4. Customize the project by modifying the Python scripts or HTML file as needed.


## API Key Usage Rules
You should obtain an API key from the Google Cloud Console and use it in your request. Here are the steps to obtain and use the API key:
1. Go to the [Google Cloud Console](https://console.cloud.google.com/).
2. Create a new project or select an existing project.
3. Enable the "Geocoding API" for your project. You can find the API in the "API & Services" > "Library" section of the console.
4. Create an API key. Navigate to "API & Services" > "Credentials," then click the "Create credentials" button and select "API Key."
5. Copy the generated API key.
6. Replace __'YOUR_API_KEY'__ with the actual API key you obtained from the Google Cloud Console.

### Note
You should never include sensitive information, such as API keys or passwords, in your GitHub repositories or make them public. This is a security best practice to protect your credentials and prevent unauthorized access or misuse of your API key.

Instead, you should store your API key securely and use environment variables or configuration files to manage it. Here's a general guideline for how to handle API keys in a more secure way:
1. __Store the API Key Locally__: Keep your API key in a local configuration file that is not tracked by version control. Create a separate configuration file (e.g., config.py or .env) where you store your API key.
2. __Use Environment Variables__: You can set environment variables to store sensitive information like API keys. Most programming languages and frameworks provide ways to access environment variables in your code.
3. __Access API Keys in Your Code__: Modify your code to read the API key from the environment variable or the configuration file. For example, in Python, you can use the os module to access environment variables.

Here's an example of how to access an API key stored in an environment variable in Python:
```
import os

api_key = os.environ.get("API_KEY")
```

1. __Add the Configuration File to .gitignore__: Make sure to add the configuration file that contains your API key to your .gitignore file so that it is not accidentally committed to your repository.
2. __Document API Key Setup__: In your project's README or documentation, explain how users can set up their own API keys if they want to use your code.

By following these practices, you can keep your API key private and secure while still sharing your code on GitHub. Never hardcode or expose API keys in your public repositories.




