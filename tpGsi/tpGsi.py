import os
import json
from flask import Flask, request, jsonify, send_file
from datetime import datetime

app = Flask(__name__)

# Path to the JSON file
JSON_FILE = "data.json"

@app.route('/')
def welcome():
    return '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Welcome</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background-color: #fdf6e3;
                color: #333;
                text-align: center;
                padding: 50px;
            }
            h1 {
                color: #ff6f61;
            }
            p {
                font-size: 18px;
                line-height: 1.5;
            }
            .container {
                max-width: 600px;
                margin: 0 auto;
                padding: 20px;
                background: #fff;
                border-radius: 10px;
                box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            }
            button {
                font-size: 16px;
                padding: 10px 20px;
                margin: 10px;
                color: #fff;
                background-color: #ff6f61;
                border: none;
                border-radius: 5px;
                cursor: pointer;
            }
            button:hover {
                background-color: #e65b50;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Welcome to Our Warm and Fuzzy Page!</h1>
            <p>We're so happy you're here! Grab a cup of coffee, relax, and enjoy your stay.</p>
            <p>Click the buttons below to create or update a JSON file.</p>
            <form action="/create-json" method="post">
                <button type="submit">Create JSON File</button>
            </form>
            <form action="/save-datetime" method="post">
                <button type="submit">Save Current Date and Time</button>
            </form>
            <form action="/print-dates" method="get">
                <button type="submit">Print Dates</button>
            </form>
        </div>
    </body>
    </html>
    '''

@app.route('/create-json', methods=['POST'])
def create_json():
    # Create an empty JSON file if it doesn't exist
    if not os.path.exists(JSON_FILE):
        with open(JSON_FILE, 'w') as file:
            json.dump({}, file)
        return '<p>JSON file created successfully! <a href="/">Go back</a></p>'
    else:
        return '<p>JSON file already exists! <a href="/">Go back</a></p>'

@app.route('/save-datetime', methods=['POST'])
def save_datetime():
    # Save the current date and time to the JSON file
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    # Load existing data if the file exists
    if os.path.exists(JSON_FILE):
        with open(JSON_FILE, 'r') as file:
            data = json.load(file)
    else:
        data = {}

    # If the key 'dates' doesn't exist, create it as an empty list
    if 'dates' not in data:
        data['dates'] = []
    
    # Append the current date and time to the list
    data['dates'].append(current_time)
    
    # Save the data back to the file
    with open(JSON_FILE, 'w') as file:
        json.dump(data, file, indent=4)
    
    return '<p>Current date and time saved successfully! <a href="/">Go back</a></p>'

@app.route('/print-dates', methods=['GET'])
def print_dates():
    # Retrieve the data from the JSON file
    if os.path.exists(JSON_FILE):
        with open(JSON_FILE, 'r') as file:
            data = json.load(file)
        
        # Extract all date-related entries
        dates = data.get('dates', [])
        
        # Return the dates in the JSON response
        return jsonify(dates)
    else:
        return '<p>No data file found. Please create or save the datetime first. <a href="/">Go back</a></p>'

if __name__ == '__main__':
    # Use the PORT environment variable provided by Render or default to 5000
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
