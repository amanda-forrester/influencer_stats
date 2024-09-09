import pandas as pd

def analyze_data(input_file='data/influencer_data.csv', output_file='processed_data/processed_data.csv'):
    # Read the data from the CSV file
    df = pd.read_csv(input_file)
    
    # Ensure the data types are correct
    df['campaign_spend'] = pd.to_numeric(df['campaign_spend'], errors='coerce')
    df['conversions'] = pd.to_numeric(df['conversions'], errors='coerce')
    df['followers'] = pd.to_numeric(df['followers'], errors='coerce')
    df['engagement_rate'] = pd.to_numeric(df['engagement_rate'], errors='coerce')
    
    # Perform analysis
    summary = df.groupby(['name', 'platform']).agg({
        'campaign_spend': 'sum',
        'conversions': 'sum',
        'followers': 'sum',
        'engagement_rate': 'mean'
    }).reset_index()

    # Calculate additional metrics
    summary['conversion_rate'] = (summary['conversions'] / summary['campaign_spend']) * 100
    summary['cost_per_conversion'] = summary['campaign_spend'] / summary['conversions']
    summary['average_followers'] = summary['followers'] / summary.groupby('name')['name'].transform('count')
    
    # Save the processed data to a new CSV file
    summary.to_csv(output_file, index=False)
    print(f'Processed data saved to {output_file}')

if __name__ == "__main__":
    analyze_data()
