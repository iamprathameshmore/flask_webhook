
# Webhook with Flask and Docker

## Introduction

This project demonstrates how to create a webhook using Flask, a lightweight Python web framework. The webhook can receive data via HTTP POST requests and respond accordingly. Additionally, we will deploy the application using Python Alpine in a Docker container for a lightweight and efficient deployment.

## Table of Contents
- [Learning Objectives](#learning-objectives)
- [Technologies Used](#technologies-used)
- [Setup Instructions](#setup-instructions)
- [Flask Webhook Implementation](#flask-webhook-implementation)
- [Docker Deployment](#docker-deployment)
- [Usage](#usage)
- [Conclusion](#conclusion)

## Learning Objectives

Through this project, I aimed to learn:
- How to set up a Flask application to handle webhooks.
- How to process incoming JSON data in a Flask app.
- How to deploy a Python application using Alpine Linux in a Docker container.
- The advantages of using Docker for deployment.

## Technologies Used
- **Python**: The programming language used for the backend.
- **Flask**: A micro web framework for Python.
- **Docker**: A platform for developing, shipping, and running applications in containers.
- **Python Alpine**: A minimal Docker image for running Python applications.

## Setup Instructions

1. **Clone the Repository**:
   Clone this repository to your local machine:
   ```shell
   git clone https://github.com/iamprathameshmore/flask_webhook
   cd flask_webhook
   ```

2. **Install Dependencies**:
   Create a `requirements.txt` file with the following content:
   ```python
   pip install Flask
   ```

3. **Create the Flask Application**:
   Create a file named `app.py` and add the following code:
   ```python
   from flask import Flask, request, jsonify

   application = Flask(__name__)

   @application.route('/', methods=['GET'])
   def get():
       return jsonify({"msg": "hello from server 5000"})

   @application.route('/webhook', methods=['POST'])
   def webhook():
       try:
           data = request.json
           print("Received webhook data:", data)
           message = data.get('message', 'No message received')
           return jsonify({'status': 'success', 'data_received': data}), 200
       except Exception as e:
           return jsonify({'status': 'failure', 'error': str(e)}), 400

   if __name__ == '__main__':
       application.run(port=5000)
   ```

4. **Create a Dockerfile**:
   Create a `Dockerfile` in the project root with the following content:
   ```Dockerfile
   FROM python:3.12-alpine

   ENV PYTHONDONTWRITEBYTECODE 1
   ENV PYTHONUNBUFFERED 1

   WORKDIR /app

   COPY requirements.txt .
   RUN pip install --no-cache-dir -r requirements.txt

   COPY . .

   EXPOSE 5000

   CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "app:application"]
   ```

## Docker Deployment

1. **Build the Docker Image**:
   Run the following command to build the Docker image:
   ```bash
   docker build -t flask-gunicorn-app .
   ```

2. **Run the Docker Container**:
   Start the Docker container with the following command:
   ```bash
   docker run -p 5000:5000 flask-gunicorn-app
   ```

## Usage

1. **Access the GET Endpoint**:
   Open your browser or use Postman to visit `http://localhost:5000/`. You should see a JSON response:
   ```json
   {"msg": "hello from server 5000"}
   ```

2. **Test the Webhook**:
   Use Postman to send a POST request to `http://localhost:5000/webhook` with a JSON body, such as:
   ```json
   {
       "message": "Hello from Postman!"
   }
   ```

   You should receive a response confirming the data received.

## Conclusion

In this project, I successfully learned how to create a webhook using Flask and how to deploy it using Docker with a Python Alpine image. The combination of Flask for handling web requests and Docker for deployment makes it a powerful solution for creating scalable web applications.
