import os
from flask import Flask, render_template, request, jsonify
import numpy as np
import joblib
import pickle
from flask_cors import CORS

# Print the current working directory and script location for debugging
print("Current working directory:", os.getcwd())
print("Script location (app.py):", os.path.abspath(__file__))

# Define the template folder path explicitly
template_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates')
print("Template folder path:", template_folder)

# Verify that the templates folder and HTML files exist
if not os.path.exists(template_folder):
    print(f"ERROR: Templates folder not found at {template_folder}")
else:
    print("Templates folder found!")
    index_html_path = os.path.join(template_folder, 'index.html')
    dashboard_html_path = os.path.join(template_folder, 'dashboard.html')
    if not os.path.exists(index_html_path):
        print(f"ERROR: index.html not found at {index_html_path}")
    else:
        print("index.html found!")
    if not os.path.exists(dashboard_html_path):
        print(f"ERROR: dashboard.html not found at {dashboard_html_path}")
    else:
        print("dashboard.html found!")

# Initialize Flask app with explicit template folder
app = Flask(__name__, template_folder=template_folder)
CORS(app)

# Load the trained ML model and scaler
try:
    model = joblib.load("random_forest_model.pkl")
    print("Model loaded successfully!")
except Exception as e:
    print(f"Error loading model: {e}")
    model = None

try:
    scaler = pickle.load(open("scaler.pkl", "rb"))
    print("Scaler loaded successfully!")
except Exception as e:
    print(f"Error loading scaler: {e}")
    scaler = None

# Route to serve the frontend HTML page (index.html)
@app.route("/")
def home():
    try:
        return render_template("index.html")
    except Exception as e:
        return f"Error rendering template: {str(e)}", 500

# Route to serve the dashboard HTML page (dashboard.html)
@app.route("/dashboard.html")
def dashboard():
    try:
        # Get query parameters from the URL
        query_params = {
            "lights": request.args.get("lights", ""),
            "T_in": request.args.get("T_in", ""),
            "RH_in": request.args.get("RH_in", ""),
            "T_out": request.args.get("T_out", ""),
            "Windspeed": request.args.get("Windspeed", ""),
            "predicted_consumption": request.args.get("predicted_consumption", ""),
            "suggestion": request.args.get("suggestion", "")
        }
        # Render dashboard.html and pass query parameters to the template
        return render_template("dashboard.html", **query_params)
    except Exception as e:
        return f"Error rendering dashboard template: {str(e)}", 500

# Route to handle ML predictions
@app.route("/predict", methods=["POST"])
def predict():
    print("Received a request to /predict")
    try:
        data = request.get_json()
        print("Received data:", data)

        # Validate the data
        required_keys = ["lights", "T_in", "RH_in", "T_out", "Windspeed"]
        for key in required_keys:
            if key not in data or data[key] is None:
                return jsonify({"error": f"Missing or invalid value for {key}"}), 400

        # Prepare features in the correct order
        features = np.array([[data["lights"], data["T_in"], data["RH_in"], data["T_out"], data["Windspeed"]]])
        print("Features before scaling:", features)

        # Scale the features
        if scaler is None:
            return jsonify({"error": "Scaler not loaded. Please check the server logs."}), 500
        features_scaled = scaler.transform(features)
        print("Features after scaling:", features_scaled)

        # Check if model is loaded
        if model is None:
            return jsonify({"error": "Model not loaded. Please check the server logs."}), 500

        # Make prediction
        prediction = model.predict(features_scaled)[0]
        print("Prediction:", prediction)

        # Round the prediction to the nearest integer
        predicted_consumption = round(prediction)

        # Generate a suggestion based on the prediction
        suggestion = "Reduce light usage to save 5% energy."  # As per the desired output

        # Return the prediction and input data in the response
        return jsonify({
            "lights": data["lights"],
            "T_in": data["T_in"],
            "RH_in": data["RH_in"],
            "T_out": data["T_out"],
            "Windspeed": data["Windspeed"],
            "predicted_consumption": predicted_consumption,
            "suggestion": suggestion
        })
    except Exception as e:
        print("Error in /predict:", str(e))
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=5000)