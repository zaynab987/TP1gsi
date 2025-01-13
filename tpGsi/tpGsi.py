import os
from flask import Flask

app = Flask(__name__)

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
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Welcome to Our Warm and Fuzzy Page!</h1>
            <p>We're so happy you're here! Grab a cup of coffee, relax, and enjoy your stay.</p>
            <p>Feel free to explore and make yourself at home.</p>
        </div>
    </body>
    </html>
    '''

if __name__ == '__main__':
    # Use the PORT environment variable provided by Render or default to 5000
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
