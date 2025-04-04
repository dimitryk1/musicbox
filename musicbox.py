import os
import requests
from flask import Flask, jsonify

# Initialize Flask application
app = Flask(__name__)

# Get the port from environment variable or use default value 9000
port = int(os.environ.get("PORT", 9000))

# Get the rock service host from environment variable
rock_host = os.environ.get("ROCK_HOST", "localhost:9003")
opera_host = os.environ.get("OPERA_HOST", "localhost:9002")
flamenco_host = os.environ.get("FLAMENCO_HOST", "localhost:9001")

@app.route('/ping', methods=['GET'])
def ping():
    print("Received ping request")
    return {"message": "ping successful"}

@app.route('/rock', methods=['GET'])
def rock():
    try:
        # Make a request to the rock service
        rock_url = f"http://{rock_host}"
        print(f"Received rock request, calling {rock_url}")
        response = requests.get(rock_url)
        
        # Return the same response from the rock service
        return response.json()
    except requests.exceptions.RequestException as e:
        # Handle any errors that occur during the request
        return jsonify({"error": f"Failed to connect to rock service: {str(e)}"}), 500

@app.route('/opera', methods=['GET'])
def opera():
    try:
        # Make a request to the opera service
        opera_url = f"http://{opera_host}"
        print(f"Received opera request, calling {opera_url}")
        response = requests.get(opera_url)
        
        # Return the same response from the opera service
        return response.json()
    except requests.exceptions.RequestException as e:
        # Handle any errors that occur during the request
        return jsonify({"error": f"Failed to connect to opera service: {str(e)}"}), 500

@app.route('/flamenco', methods=['GET'])
def flamenco():
    try:
        # Make a request to the flamenco service
        flamenco_url = f"http://{flamenco_host}"
        print(f"Received flamenco request, calling {flamenco_url}")
        response = requests.get(flamenco_url)
        
        # Return the same response from the flamenco service
        return response.json()
    except requests.exceptions.RequestException as e:
        # Handle any errors that occur during the request
        return jsonify({"error": f"Failed to connect to flamenco service: {str(e)}"}), 500
        
if __name__ == '__main__':
    print(f"Starting server on port {port}")
    print(f"Rock service host: {rock_host}")
    print(f"Opera service host: {opera_host}")
    print(f"Flamenco service host: {flamenco_host}")
    app.run(host='0.0.0.0', port=port)