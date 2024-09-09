import pandas as pd
import numpy as np
import random

def generate_mock_data(file_path='data/influencer_data.csv'):
    # Define mock data
    platforms = ['YouTube', 'Meta', 'TikTok']
    np.random.seed(42)
    
    data = {
        'influencer_id': [i for i in range(1, 301)],
        'name': [f'Influencer {i}' for i in range(1, 301)],
        'platform': [random.choice(platforms) for _ in range(300)],
        'followers': [random.randint(1000, 1000000) for _ in range(300)],
        'engagement_rate': [round(random.uniform(0.01, 0.10), 2) for _ in range(300)],
        'campaign_spend': [round(random.uniform(1000, 100000), 2) for _ in range(300)],
        'conversions': [random.randint(0, 500) for _ in range(300)],
    }
    
    df = pd.DataFrame(data)
    df.to_csv(file_path, index=False)
    print(f'Mock data generated and saved to {file_path}')

if __name__ == "__main__":
    generate_mock_data()
