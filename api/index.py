# Ensure Flask and requests are installed
# You can install them using:
# pip install flask requests

from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)

# Root endpoint
@app.route('/')
def home():
    return jsonify({
        "status": "active",
        "message": "Welcome to the Terabox Downloader API",
        "creator": "Created by nano (t.me/genxnano)",
        "endpoints": {
            "/download": {
                "method": "POST",
                "description": "Download Terabox link",
                "required_body": {
                    "url": "The URL of the Terabox link to download"
                }
            },
            "/docs": {
                "method": "GET",
                "description": "API Documentation"
            }
        }
    })

# Download endpoint
@app.route('/download', methods=['POST'])
def download():
    try:
        # Get JSON data from request
        data = request.get_json()
        if not data or 'url' not in data:
            return jsonify({
                "status": "error",
                "message": "URL is required in request body"
            }), 400

        # Extract Terabox link from the JSON request
        terabox_link = data['url']

        # API endpoint for TeraBox downloader
        api_url = "https://ytshorts.savetube.me/api/v1/terabox-downloader"
        
        # Request payload
        payload = {"url": terabox_link}
        headers = {
            "Content-Type": "application/json",
            "Accept": "application/json"
        }

        # Send POST request to the ytshort API
        response = requests.post(api_url, json=payload, headers=headers)

        # Check if the response was successful
        if response.status_code == 200:
            try:
                # Parse the JSON response
                data = response.json()
                video_data = data['response'][0]
                
                # Prepare output data
                output_data = {
                    "status": "success",
                    "data": {
                        "title": video_data['title'],
                        "thumbnail": video_data['thumbnail'],
                        "resolutions": {
                            "Fast Download": video_data['resolutions'].get('Fast Download'),
                            "HD Video": video_data['resolutions'].get('HD Video')
                        }
                    }
                }
                
                return jsonify(output_data)
            
            except (KeyError, IndexError) as e:
                return jsonify({
                    "status": "error",
                    "message": f"Error parsing response: {str(e)}"
                }), 500
        
        else:
            return jsonify({
                "status": "error",
                "message": f"Downloader API returned status code: {response.status_code}"
            }), response.status_code

    except Exception as e:
        return jsonify({
            "status": "error",
            "message": f"Internal server error: {str(e)}"
        }), 500

# Documentation endpoint
@app.route('/docs')
def docs():
    with open('docs.md', 'r') as file:
        docs = file.read()
    return docs

# Debug mode
app.debug = True

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)