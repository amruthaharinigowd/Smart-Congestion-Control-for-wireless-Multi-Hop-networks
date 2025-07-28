import random
import joblib
import subprocess
import pandas as pd

# Load CatBoost model
model = joblib.load("catboost_congestion_model.pkl")

def run_ns2_with_dynamic_control(nodes, packet_size, X_metric, Y_metric, rate):
   
    df = pd.DataFrame([[nodes, packet_size, X_metric, Y_metric, rate]],columns=["Nodes", "PacketSize", "X", "Y", "Rate"])

  
    prediction = model.predict(df)[0]
    print(f"Starting Predicted Congestion: {prediction}\n")
   
    while prediction==1 and rate>0:
        rate-=1
        df = pd.DataFrame([[nodes, packet_size, X_metric, Y_metric, rate]],columns=["Nodes", "PacketSize", "X", "Y", "Rate"])
        prediction = model.predict(df)[0]
        print(f"Predicted Congestion: {prediction}, Adjusted Rate: {rate}")
    print(f"\nSince there is no congestion at {rate}Mb \nSimulating With : {rate}Mb\n")
   
    cmd = f"ns congestion.tcl {nodes} {X_metric} {Y_metric} {packet_size} {rate}Mb"
    subprocess.run(cmd, shell=True)

