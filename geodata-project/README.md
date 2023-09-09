# Geodata Project: Google Geocoding API & Data Visualization

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
6. Open `where.html` in a web browser to visualize the data on a Google Map.


## Usage
1. Populate the `where.data` file with university names (one per line) that you want to geocode and visualize.
2. Follow the "Getting Started" instructions to set up and run the project.
3. View the geocoded data on the Google Map visualization by opening `where.html` in a web browser.
4. Customize the project by modifying the Python scripts or HTML file as needed.


## Project Structure
The project structure is organized as follows:
* __geoload.py__: Python script for retrieving and geocoding university location data using the Google Geocoding API and storing it in an SQLite database. The program reads input lines from the where.data file, and for each line, it checks whether the information is already present in the database. If the location's data is not found in the database, the program uses the geocoding API to fetch the data and then stores it in the database.

Here is a sample run:
```
Found in database  University of Hong Kong, Illinois Institute of Technology, Bradley University
Found in database  Northeastern University
Resolving Monash University
Retrieving http://maps.googleapis.com/maps/api/geocode/json?sensor=false&address=Monash+University
Retrieved 2063 characters {    "results" : [  
{u'status': u'OK', u'results': ... }
```
__The geoload.py can be stopped at any time__, and there is a counter that you can use to limit the number of calls to the geocoding API for each run.
* __geodump.py__: Python script for exporting geocoded data from the database to a JavaScript file.
A run of the geodump.py program is as follows:
<img width="1337" alt="terminal_result" src="https://github.com/aleksandrajk/Python-Projects/assets/55165756/144456c1-4e18-4297-8859-35228019e710">

* __where.data__: Input file containing university names.
* __geodata.sqlite__: SQLite database to store geocoded location data. Once you have some data loaded into geodata.sqlite, you can visualize the data using the (geodump.py) program.  This program reads the database and writes tile file (where.js) with the location, latitude, and longitude in the form of executable JavaScript code. 
* __where.js__: a JavaScript list of lists that we have written to where.js by running geodump.py.
Here is the format of the where.js file:
```
myData = [
[40.6963857,-89.6160811, 'Bradley University, 1501 West Bradley Avenue, Peoria, IL 61625, USA'],
   ...
];
```
* __where.html__: HTML file for visualizing geocoded data on a Google Map. Simply open where.html in a browser to see the locations.  You can hover over each map pin to find the location that the gecoding API returned for the user-entered input. 
* __README.md__: This documentation file.


## Data Visualization: Result
<img width="1429" alt="geodata_result" src="https://github.com/aleksandrajk/Python-Projects/assets/55165756/11a9174b-7630-4f94-94ce-0e8f9b13d102">
<img width="1437" alt="geodata_result2" src="https://github.com/aleksandrajk/Python-Projects/assets/55165756/692b3606-ea46-4299-8b3f-f153c39755ac">


## API Key Usage Rules
You should obtain an API key from the Google Cloud Console and use it in your request. Here are the steps to obtain and use the API key:
1. Go to the [Google Cloud Console](https://console.cloud.google.com/).
2. Create a new project or select an existing project.
3. Enable the "Geocoding API" for your project. You can find the API in the "API & Services" > "Library" section of the console.
4. Create an API key. Navigate to "API & Services" > "Credentials," then click the "Create credentials" button and select "API Key."
5. Copy the generated API key.
6. Replace __'YOUR_API_KEY'__ with the actual API key you obtained from the Google Cloud Console.

### Note
__You should never include sensitive information, such as API keys or passwords, in your GitHub repositories or make them public. This is a security best practice to protect your credentials and prevent unauthorized access or misuse of your API key.__

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




