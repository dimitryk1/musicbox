import os
import requests
from flask import Flask, jsonify
from aws_xray_sdk.core import xray_recorder
from aws_xray_sdk.ext.flask.middleware import XRayMiddleware

# Configure X-Ray recorder
#xray_recorder.configure(service='rock')

# Initialize Flask application
app = Flask(__name__)

# Initialize X-Ray middleware
#XRayMiddleware(app, xray_recorder)

# Get the port from environment variable or use default value 9000
port = int(os.environ.get("PORT", 9000))

# Get the rock service host from environment variable
hosts={
  "rock": os.environ.get("ROCK_HOST", "localhost:9003"),
  "opera": os.environ.get("OPERA_HOST", "localhost:9002"),
  "flamenco": os.environ.get("FLAMENCO_HOST", "localhost:9001")
 }

def run_app(app_name):
    try:
        # Make a request to the service
        app_url = f"http://{hosts[app_name]}"
        print(f"Received {app_name} request, calling {app_url}")
        response = requests.get(app_url)
        # Return the same response from the rock service
        return jsonify({"artists": response.text})
    except requests.exceptions.RequestException as e:
        # Handle any errors that occur during the request
        return jsonify({"debug1": f"Received {app_name} request, calling {app_url}","error": f"Failed to connect to rock service: {str(e)}"}), 500

@app.route('/ping', methods=['GET'])
def ping():
    print("Received ping request")
    return {"message": "ping successful"}

@app.route('/rock', methods=['GET'])
def rock():
    return run_app("rock")
@app.route('/opera', methods=['GET'])
def opera():
    return run_app("opera")
@app.route('/flamenco', methods=['GET'])
def flamenco():
    return run_app("flamenco")
        
if __name__ == '__main__':
    print(f"Starting server on port {port}")
    for app_name in hosts.keys():
       print(f"{app_name} service host: {hosts[app_name]}")
    app.run(host='0.0.0.0', port=port)