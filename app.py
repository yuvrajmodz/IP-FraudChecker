from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/checkmyip', methods=['GET'])
def check_my_ip():
    # Get the IP address from query parameters if provided
    ip_address = request.args.get('address')
    
    # Base URL of the external API
    external_api_url = "http://103.235.106.139:5000/myip"
    
    # Prepare the request URL based on whether IP address is provided
    if ip_address:
        # Send request with the specified IP address
        url = f"{external_api_url}?address={ip_address}"
    else:
        # Send request without IP address to get the user's IP details
        url = external_api_url
    
    # Make a request to the external API
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad HTTP response status codes
    except requests.RequestException as e:
        # Return error message if the request fails
        return jsonify({"error": "Failed to fetch data from the external API", "details": str(e)}), 500

    # Parse the JSON response from the external API
    data = response.json()

    # Return the JSON response to the user
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
