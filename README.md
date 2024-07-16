# Flask API for Time Difference Calculation
This project implements a Flask API that calculates the absolute difference in seconds between pairs of timestamps provided as input. It provides endpoints to handle multiple test cases and returns results in JSON format.

## Setup
Follow these steps to set up and run the Flask API locally:

### Prerequisites
* Python 3.x installed on your system.<br>
* Postman (for manual API testing).

### 1. Installation

```bash

git clone https://github.com/Dobby-Mphahlele/Problem-set-1
cd <project-directory>
``` 

### 2. Create and activate a virtual environment:
```
python -m venv venv
# On Windows: venv\Scripts\activate
# On macOS/Linux: source venv/bin/activate
```

### 3. Install dependencies:
```
pip install -r requirements.txt
```

## Running the Flask App
### 1. Run the Flask application:
```
python app.py
```
2. The Flask app should now be running on:
```
http://127.0.0.1:5000/calculate
```

# Usage
## Endpoint
The API provides a single endpoint for calculating time differences:
* Endpoint: /calculate
* HTTP Method: POST

## Input Format
The API expects input data in the following format:
```
T
timestamp1
timestamp2
...
```
Where:

* T is the number of test cases.
* Each subsequent line contains a timestamp in the format `Day Mon Year Hour:Minute:Second Timezone`.
Example:
```
2
Sun 10 May 2015 13:54:36 -0700
Sun 10 May 2015 13:54:36 -0000
Sat 02 May 2015 19:54:36 +0530
Fri 01 May 2015 13:54:36 -0000
```
## Testing
### Using Postman
1. Open Postman:
* Launch Postman on your computer.
2. Create a POST request:
* Set the request type to POST.
* Enter the URL: http://127.0.0.1:5000/calculate.
* Go to the Body tab, select raw, and paste the input data format mentioned above.
### Send the request:
* Click Send to execute the request.
* Postman will display the response from the API.
## Automated Testing with Python
A Python script (`test_api.py`) using the `requests` library can be used for automated testing:
```
import requests

# Define the URL of your Flask API endpoint
url = 'http://127.0.0.1:5000/calculate'

# Sample input data (number of test cases and pairs of timestamps)
input_data = """
2
Sun 10 May 2015 13:54:36 -0700
Sun 10 May 2015 13:54:36 -0000
Sat 02 May 2015 19:54:36 +0530
Fri 01 May 2015 13:54:36 -0000
"""

try:
    # Send a POST request to the API endpoint with the input data
    response = requests.post(url, data=input_data.encode('utf-8'))

    # Check if the request was successful (HTTP status code 200)
    if response.status_code == 200:
        # Print the JSON response from the API
        print(response.json())
    else:
        print(f"Error: Status code {response.status_code}")
        print(response.text)

except requests.exceptions.RequestException as e:
    print("Error:", e)

```
# Dockerized Flask Application
## This project contains a Dockerized Flask application that calculates the absolute difference in seconds between two timestamps.

### Table of Contents
Prerequisites
* Setup
* Clone the Repository
* Run the Docker Container
* Testing the Application
* Using Postman
* Using Python Script

# Prerequisites
## Before running this application, ensure you have the following installed on your machine:
* Docker
* Git
# Setup
## Clone the Repository
### Clone this repository to your local machine:
```
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```
## Run the Docker Container
1. Build the Docker image:
```
docker build -t my-python-app .
```
2. Create a Docker network (if not already created):
```
docker network create my_bridge_network
```
3. Run two instances of the Docker container (replace your-dockerhub-username with your Docker Hub username):
```
docker run -d --network my_bridge_network -p 5001:5000 --name node1 -e NODE_ID=node1 your-dockerhub-username/my-python-app
docker run -d --network my_bridge_network -p 5002:5000 --name node2 -e NODE_ID=node2 your-dockerhub-username/my-python-app
```
### Testing the Application
You can test the application using Postman or a Python script.

## Using Postman
1. Open Postman.

2. Set the request method to POST.

3. Set the URL to http://localhost:5001/calculate for node1 or http://localhost:5002/calculate for node2.

4. Set the body to raw and Text format.

5. Paste the sample input data in the body:
```
2
Sun 10 May 2015 13:54:36 -0700
Sun 10 May 2015 13:54:36 -0000
Sat 02 May 2015 19:54:36 +0530
Fri 01 May 2015 13:54:36 -0000
```
6. Send the request and check the response.

# Using Python Script
You can also test the application using a Python script:
```
import requests

# Define the URL of your Flask API endpoint (change port if needed)
url1 = 'http://localhost:5001/calculate'
url2 = 'http://localhost:5002/calculate'

# Sample input data (number of test cases and pairs of timestamps)
input_data = """
2
Sun 10 May 2015 13:54:36 -0700
Sun 10 May 2015 13:54:36 -0000
Sat 02 May 2015 19:54:36 +0530
Fri 01 May 2015 13:54:36 -0000
"""

try:
    # Send a POST request to the API endpoint with the input data for node1
    response1 = requests.post(url1, data=input_data.encode('utf-8'))
    if response1.status_code == 200:
        print('Response from node1:', response1.json())
    else:
        print(f"Error from node1: Status code {response1.status_code}")
        print(response1.text)

    # Send a POST request to the API endpoint with the input data for node2
    response2 = requests.post(url2, data=input_data.encode('utf-8'))
    if response2.status_code == 200:
        print('Response from node2:', response2.json())
    else:
        print(f"Error from node2: Status code {response2.status_code}")
        print(response2.text)

except requests.exceptions.RequestException as e:
    print("Error:", e)
``







