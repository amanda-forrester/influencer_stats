# influencer_stats

## Overview

This project provides a web-based data visualization tool for influencer campaign data. It visualizes various metrics related to influencer campaigns, such as total campaign spend, conversions, and ROI, using interactive charts created with `Chart.js` and styled with `Bootstrap`. The backend is implemented in Python, which serves the data to the front-end.

## Features

- **Summary Statistics**: Displays key metrics including total campaign spend, total conversions, average conversion rate, and the most common platform.
- **Top 5 Influencers by Conversions**: A horizontal bar chart showing the top 5 influencers based on their conversions.
- **Top 5 Influencers by ROI**: A vertical bar chart displaying the top 5 influencers based on their return on investment (ROI).
- **Engagement Rate vs. Conversions**: A scatter plot visualizing the relationship between engagement rate and conversions.

## Technologies Used

- **HTML/CSS**: For structuring and styling the web page.
- **JavaScript**: For fetching data, processing it, and rendering charts.
- **Chart.js**: A JavaScript library for creating interactive charts.
- **Bootstrap**: A framework for responsive design.
- **Python**: Used for serving the data to the front-end. Ensure that your backend Python script is set up to provide the data at the `/data` endpoint.

## Setup and Installation

1. **Clone the repository**

    ```bash
    git clone https://github.com/your-username/influencer-data-visualization.git
    cd influencer-data-visualization
    ```

2. **Serve the HTML file**

    You can use any static file server to serve the `index.html` file. For example, using Python’s built-in HTTP server:

    ```bash
    python -m http.server
    ```

    Alternatively, you can use tools like `Live Server` in Visual Studio Code.

3. **Ensure Data Availability**

    Ensure that the `/data` endpoint is available and returns the influencer data in JSON format. You can modify the `fetchData` function in `index.html` if your data source differs.

4. **Python Backend**

    If you need a Python script to serve the data, make sure to set up a simple Python server using frameworks like Flask or FastAPI to handle the `/data` endpoint. Adjust the URL in `fetchData` accordingly.

## Data Format

The expected data format is a JSON array where each item has the following fields:

- `name`: Name of the influencer
- `platform`: Social media platform (e.g., 'YouTube', 'Meta', 'TikTok')
- `campaign_spend`: Total spend for the campaign
- `conversions`: Number of conversions
- `followers`: Number of followers
- `engagement_rate`: Engagement rate as a decimal (e.g., 0.05 for 5%)
- `conversion_rate`: Conversion rate as a decimal
- `cost_per_conversion`: Cost per conversion
- `average_followers`: Average number of followers

## Usage

1. Open the `index.html` file in a web browser to view the visualizations.
2. The page will display summary statistics and charts for the top 5 influencers based on conversions and ROI.
3. The scatter plot will show the relationship between engagement rate and conversions.

## Contributing

Feel free to submit issues or pull requests if you find bugs or have suggestions for improvements. Contributions are welcome!

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- **Chart.js**: For providing an easy-to-use charting library.
- **Bootstrap**: For responsive design features.
- **Python**: For the backend implementation and data serving.
