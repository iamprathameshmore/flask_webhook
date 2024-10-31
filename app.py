from flask import Flask, request, jsonify

app = Flask(__name__)

print('run the server on 5000')
# Define the endpoint for the root URL
@app.route('/', methods=['GET'])
def get():
    print('run the server on 5000')
    return jsonify({"msg": "hello from server 5000"})

# Define the endpoint for the webhook
@app.route('/webhook', methods=['POST'])
def webhook():
    try:
        data = request.json  # Get JSON payload
        print("Received webhook data:", data)

        # Extract message from data (assuming there's a 'message' field)
        message = data.get('message', 'No message received')

        # Send a success response
        return jsonify({'status': 'success', 'data_received': data}), 200
    except Exception as e:
        return jsonify({'status': 'failure', 'error': str(e)}), 400

if __name__ == '__main__':
    # Run the Flask app on the default port (5000)
    app.run(port=5000)
