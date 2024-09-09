from flask import Flask, jsonify, send_from_directory
import pandas as pd

app = Flask(__name__, static_url_path='', static_folder='static')  # Define static folder

# Route to serve the main HTML file
@app.route('/')
def index():
    # Serve index.html from the 'static' directory
    return send_from_directory(app.static_folder, 'index.html')

# Endpoint to provide data for the chart
@app.route('/data')
def get_data():
    # Read from the processed data file instead of the raw data
    df = pd.read_csv('processed_data/processed_data.csv')
    
    # Prepare the data to send to the frontend
    df_processed = df[['name', 'platform', 'engagement_rate', 'campaign_spend', 'conversions', 'followers']].copy()  # Include 'followers' since it's needed in the chart
    
    # Convert to a dictionary to send as JSON
    data = df_processed.to_dict(orient='records')
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
