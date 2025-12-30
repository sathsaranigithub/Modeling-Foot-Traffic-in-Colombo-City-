# Modeling Foot Traffic in Colombo City During Peak Hours for Smart City Planning

## 📌 Abstract
This research focuses on modeling and predicting pedestrian foot traffic in Colombo, Sri Lanka, during peak hours to support smart city planning initiatives. Using OpenStreetMap (OSM) data, a 2D representation of Colombo city was created, and pedestrian movement was simulated under peak and off-peak conditions. An agent-based modeling approach was combined with machine learning techniques, specifically a Random Forest Regressor, to predict crowd densities. The results provide valuable insights into pedestrian dynamics, helping urban planners optimize infrastructure for improved mobility and public safety.

---

## 🎯 Objectives
- Simulate pedestrian movement patterns in Colombo city  
- Analyze foot traffic behavior during peak hours  
- Predict crowd density using machine learning  
- Identify congestion hotspots for smart city planning  

---

## 🧠 Methodology

### Data Collection
- OpenStreetMap (OSM) data accessed via the MapTiler API  
- City map extraction and processing using `osmnx`  
- Creation of a 2D grid-based map of Colombo city  

### Agent-Based Simulation
- Pedestrians modeled as autonomous agents  
- Movement behaviors:
  - **Pathfinding (A\*)** for goal-directed movement  
  - **Random walk** for natural pedestrian behavior  
- Peak-hour conditions simulated with higher agent density and reduced movement speed  
- Real-time visualization implemented using `Pygame`  

### Machine Learning Model
- **Random Forest Regressor** used for crowd density prediction  
- Features:
  - Grid-based pedestrian density  
  - Agent speed  
  - Movement patterns  
- Evaluation metrics:
  - R² Score  
  - Mean Absolute Error (MAE)  
  - Root Mean Squared Error (RMSE)  

---

## 📊 Results
- High accuracy in predicting pedestrian crowd density  
- Identification of congestion hotspots near transport hubs and commercial areas  
- Multiple visualizations generated:
  - Predicted crowd density over time  
  - Spatial distribution of pedestrians  
  - Hourly average crowd density  
  - Zone-based congestion analysis  
  - Agent speed distribution  
  - Feature correlation heatmaps  

---

## 🛠 Technologies Used
- Python  
- OpenStreetMap (OSM)  
- osmnx  
- Pygame  
- scikit-learn  
- Matplotlib  
- Seaborn  

---

## 🌍 Applications
- Smart city planning and urban mobility optimization  
- Pedestrian safety and congestion management  
- Infrastructure development and policy decision-making  

---

## 📄 Keywords
Smart City Planning, Foot Traffic Simulation, Agent-Based Modeling, Machine Learning, Crowd Density
