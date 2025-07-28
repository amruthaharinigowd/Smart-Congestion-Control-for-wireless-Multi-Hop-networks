import random
from catboost_predictor import run_ns2_with_dynamic_control

for i in range(1, 6):  # Run 5 simulations (change to 50 if needed)
    nodes = random.randint(10, 50)
    packet_size = random.randint(100, 1500)  # Random packet size (in bytes)

    # Random values for X, Y, and rate
    X_metric = random.uniform(100, 500)  # Example: X metric
    Y_metric = random.uniform(100, 500)  # Example: Y metric
    rate = random.randint(1,10)  # Example: Random rate (in Mb)

    print(f"\n🔁 Running simulation {i}\n\n")
    run_ns2_with_dynamic_control(nodes, packet_size, X_metric, Y_metric, rate)
    print(f"\n{i} th  simulation end...\n\n\n\n ")
