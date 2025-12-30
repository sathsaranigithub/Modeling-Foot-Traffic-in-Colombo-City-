import numpy as np
import pandas as pd
from main import Boid

NUM_AGENTS = 100
SIMULATION_TIME = 200

def collect_data():
    boids = [Boid(np.random.rand() * 800, np.random.rand() * 600) for _ in range(NUM_AGENTS)]
    data = []

    for t in range(SIMULATION_TIME):
        for boid in boids:
            data.append({
                "time": t,
                "id": boids.index(boid),
                "x": boid.position[0],
                "y": boid.position[1],
                "vx": boid.velocity[0],
                "vy": boid.velocity[1]
            })

        for boid in boids:
            boid.flock(boids)
            boid.update()

    df = pd.DataFrame(data)
    df.to_csv("crowd_data.csv", index=False)
    print("Data collection complete.")

if __name__ == "__main__":
    collect_data()
