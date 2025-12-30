import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import numpy as np

def train_crowd_predictor():
    # Load the crowd data
    df = pd.read_csv('crowd_data.csv')

    # Feature engineering: create a grid for the city (x, y to grid_x, grid_y)
    df['grid_x'] = df['x'] // 50
    df['grid_y'] = df['y'] // 50

    # Calculate density: number of agents in each grid
    df['density'] = df.groupby(['grid_x', 'grid_y'])['id'].transform('count')

    # Features: hour of the day, grid_x, and grid_y
    df['hour'] = df['time'] // 60  # Convert time to hours
    X = df[['hour', 'grid_x', 'grid_y']]
    y = df['density']

    # Split data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Initialize and train the model
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    # Make predictions on the test set
    predictions = model.predict(X_test)

    # Evaluate the model
    r2 = r2_score(y_test, predictions)
    mae = mean_absolute_error(y_test, predictions)
    rmse = np.sqrt(mean_squared_error(y_test, predictions))

    # Print the evaluation metrics
    print(f"Model Evaluation Metrics:")
    print(f"R^2 Score: {r2:.4f}")
    print(f"Mean Absolute Error (MAE): {mae:.4f}")
    print(f"Root Mean Squared Error (RMSE): {rmse:.4f}")

    # Optionally, print the first 5 predictions vs actual values for reference
    #comparison = pd.DataFrame({'Actual': y_test, 'Predicted': predictions})
    #print("\nFirst 5 predictions vs actual values:")
    #print(comparison.head())

if __name__ == "__main__":
    train_crowd_predictor()
