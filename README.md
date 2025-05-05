# ⚡ Wattsmart – AI-Powered Energy Efficiency Dashboard

> "What if you could reduce your electricity bill, cut carbon emissions, and help the planet—all with one smart dashboard?"

# 🧠 Overview

Wattsmart is a machine learning-based web application that predicts energy consumption and recommends actionable energy-saving tips in real-time. Designed for sustainability-conscious users, it merges AI, data visualization, and user-centric design to empower individuals and businesses to optimize their energy use.

---

# 🌍 Problem It Solves

Every day, millions of watts are wasted due to unnoticed or inefficient energy habits—leading to higher electricity bills and worsening climate change.

Wattsmart addresses this by:
- Predicting energy usage before it spikes
- Visualizing consumption patterns
- Giving intelligent tips like:
  - “Turn off idle lights to reduce your carbon footprint”
  - “Unplug devices when not in use to lower your bill”

---

# 🚀 Key Features

- 📊 Live Dashboard – Track your energy consumption interactively
- 🔮 ML-Based Predictions – Uses a trained Random Forest model to forecast usage
- 🌱 Smart Suggestions – Personalized energy-saving tips
- 💻 Responsive UI  – Built with HTML, CSS, and Bootstrap for clean visuals
- 🧠 Extendable Backend – Python + Flask architecture that’s easy to scale
- 🔐 Secure & Lightweight – Suitable for personal and enterprise deployment

---

# 🧪 Tech Stack

- **Frontend**: HTML, CSS, Bootstrap
- **Backend**: Python, Flask
- **ML Model**: Scikit-learn (RandomForestRegressor)
- **Deployment-Ready**: Modular structure for easy deployment (Heroku/Render compatible)

---

## 📽️ Demo Video

(https://www.youtube.com/watch?v=urEdBIb8chk)

---

## 🚀 Features
- 🔍 Predicts energy consumption using a trained Random Forest model
- 📊 Interactive dashboard with consumption stats
- 🌱 Energy-saving tips
- 🛠 Built with Flask (backend) and Bootstrap (frontend)
- 🔐 Can be extended with user login system
- 📈 Potential for data visualization using Chart.js or similar

To run this project, you’ll need the following requirements: Python 3.8 or higher, a web browser (e.g., Chrome, Firefox), and Jupyter Notebook for training the model. The Python dependencies listed in `requirements.txt` are `flask==2.0.1`, `flask-cors==3.0.10`, `numpy==1.23.0`, `joblib==1.1.0`, `scikit-learn==1.0.2`, `pandas==1.4.3`, and `jupyter==1.0.0`. You also need a dataset file named `energy_data.csv` with columns `lights` (W), `T_in` (°C), `RH_in` (%), `T_out` (°C), `Windspeed` (m/s), and `Appliances` (Wh). Hardware-wise, a computer with at least 4GB RAM and 1GB free disk space is required.

## How to Run the Project:
1. 🔁 Clone the Repository
  ```bash
git clone https://github.com/Myladhanyasri/Wattsmart.git
cd Wattsmart
2. 🌐 Create a virtual environment
 ```bash
python -m venv venv
venv\Scripts\activate

3. 📦 Install dependencies
 ```bash
pip install -r requirements.txt

4. 🚀 Run the Flask server
 ```bash
cd Backend/ml_model
python app.py

5. 🌐 Launch the frontend
  ```bash
  Go to the Frontend/ folder
  Open index.html in your browser

✅ Now your dashboard should be running with ML-powered predictions!

An example usage would be entering the following values on the form: 
Lights Usage as 1 W, Indoor Temperature as 12°C, Indoor Humidity as 22%, Outdoor Temperature as 23°C, and Wind Speed as 22 m/s.
After clicking "Predict Appliance Lights Usage," the dashboard will display the predicted energy usage
 (e.g., ~60 Wh, depending on your model), potential savings (e.g., ~3 Wh),
and a tip like "Reduce light usage to save 5% energy." This project is licensed under the MIT License, and you can find more details in the `LICENSE` file.
