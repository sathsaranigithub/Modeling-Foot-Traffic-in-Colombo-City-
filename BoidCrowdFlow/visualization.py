import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import time  # For adding delays between frames

def preprocess_data():
    df = pd.read_csv('crowd_data.csv')

    # Check for the 'density' column
    if 'density' not in df.columns:
        # Compute density based on grid cells (if the x and y positions exist)
        df['grid_x'] = df['x'] // 50  # Divide x by 50 to create grid zones
        df['grid_y'] = df['y'] // 50  # Divide y by 50 to create grid zones
        df['density'] = df.groupby(['grid_x', 'grid_y'])['x'].transform('count')
        
    return df

def visualize_data():
    # Load and preprocess the data
    df = preprocess_data()

    # 1. Line Graph (Time Series Plot)
    plt.figure(figsize=(8, 6))
    plt.plot(df['time'], df['density'], label='Crowd Density', color='blue')
    plt.title('Crowd Density Over Time')
    plt.xlabel('Time')
    plt.ylabel('Density')
    plt.legend()
    plt.show()
    time.sleep(2)  # Pause for 2 seconds to show the graph

    # 2. Scatter Plot (Agent Distribution in the City)
    plt.clf()  # Clear the previous plot
    plt.scatter(df['x'], df['y'], c=df['density'], cmap='Blues', s=10)
    plt.colorbar(label='Density')
    plt.title('Agent Distribution in the City')
    plt.xlabel('X Position')
    plt.ylabel('Y Position')
    plt.show()
    time.sleep(2)

    # 3. Bar Chart (Average Crowd Density by Hour)
    plt.clf()
    density_by_hour = df.groupby('time')['density'].mean()
    density_by_hour.plot(kind='bar', color='orange')
    plt.title("Average Crowd Density by Hour")
    plt.xlabel("Hour of the Day")
    plt.ylabel("Average Density")
    plt.show()
    time.sleep(2)

    # 4. Stacked Area Chart (Crowd Density in Different Zones Over Time)
    plt.clf()
    zone_density = df.groupby(['time', 'grid_x'])['density'].sum().unstack().fillna(0)
    zone_density.plot.area(stacked=True)
    plt.title("Crowd Density in Different Zones Over Time")
    plt.xlabel("Time")
    plt.ylabel("Density")
    plt.show()
    time.sleep(2)

    # 5. Histogram (Distribution of Agent Speeds)
    plt.clf()
    plt.hist(df['vx'], bins=20, color='green', edgecolor='black')
    plt.title('Distribution of Agent Speeds (X Direction)')
    plt.xlabel('Speed')
    plt.ylabel('Frequency')
    plt.show()
    time.sleep(2)

    # 6. Cluster Map (Feature Correlation Heatmap)
    plt.clf()
    correlation_matrix = df[['x', 'y', 'vx', 'vy', 'density']].corr()
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f')
    plt.title("Feature Correlation Heatmap")
    plt.show()
    time.sleep(2)

def visualize_predictions():
    # Assuming predictions have been stored in a separate file or as part of the `df`
    df = preprocess_data()

    # 1. Line Graph (Predicted Crowd Density Over Time)
    plt.figure(figsize=(8, 6))
    plt.plot(df['time'], df['density'], label='Predicted Crowd Density', color='red')
    plt.title('Predicted Crowd Density Over Time')
    plt.xlabel('Time')
    plt.ylabel('Density')
    plt.legend()
    plt.show()
    time.sleep(2)

    # 2. Scatter Plot (Predicted Agent Distribution in the City)
    plt.clf()
    plt.scatter(df['x'], df['y'], c=df['density'], cmap='Reds', s=10)
    plt.colorbar(label='Density')
    plt.title('Predicted Agent Distribution in the City')
    plt.xlabel('X Position')
    plt.ylabel('Y Position')
    plt.show()
    time.sleep(2)

    

    # 3. Bar Chart (Predicted Average Crowd Density by Hour)
    plt.clf()
    density_by_hour = df.groupby('time')['density'].mean()
    density_by_hour.plot(kind='bar', color='red')
    plt.title("Predicted Average Crowd Density by Hour")
    plt.xlabel("Hour of the Day")
    plt.ylabel("Average Density")
    plt.show()
    time.sleep(2)

    # 4. Stacked Area Chart (Predicted Crowd Density in Different Zones)
    plt.clf()
    zone_density = df.groupby(['time', 'grid_x'])['density'].sum().unstack().fillna(0)
    zone_density.plot.area(stacked=True)
    plt.title("Predicted Crowd Density in Different Zones Over Time")
    plt.xlabel("Time")
    plt.ylabel("Density")
    plt.show()
    time.sleep(2)

    # 5. Histogram (Predicted Distribution of Agent Speeds)
    plt.clf()
    plt.hist(df['vx'], bins=20, color='purple', edgecolor='black')
    plt.title('Predicted Distribution of Agent Speeds (X Direction)')
    plt.xlabel('Speed')
    plt.ylabel('Frequency')
    plt.show()
    time.sleep(2)

    # 6. Cluster Map (Predicted Feature Correlation Heatmap)
    plt.clf()
    correlation_matrix = df[['x', 'y', 'vx', 'vy', 'density']].corr()
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f')
    plt.title("Predicted Feature Correlation Heatmap")
    plt.show()
    time.sleep(2)

def visualize_data_and_predictions():
    # First, visualize the data
    #visualize_data()

    # Then, visualize the predictions
    visualize_predictions()

if __name__ == "__main__":
    visualize_data_and_predictions()
