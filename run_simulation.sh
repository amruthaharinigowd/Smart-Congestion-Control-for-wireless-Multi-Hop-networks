#!/bin/bash

OUTPUT_FILE="network_metrics.csv"

# Add CSV Headers
echo "Nodes,X,Y,PacketSize,Rate,PacketsSent,PacketsReceived,PacketLoss,PacketDeliveryRatio,AvgDelay,Throughput,AvgJitter" > $OUTPUT_FILE

for i in {1..50}  # Run 50 simulations
do
    echo "${i} th Iteration start"
    NODES=$((RANDOM % 45 + 6))        # Random nodes between 10 and 50
    X=$((RANDOM % 200 + 400))          # Random X from 400 to 600
    Y=$((RANDOM % 200 + 400))          # Random Y from 400 to 600
    PACKET_SIZE=$((RANDOM % 512 + 512)) # Random Packet Size between 512 to 1024
    RATE=$((RANDOM % 10 + 1))Mb         # Random rate between 1Mb and 10Mb

    # Run NS-2 simulation
    ns congestion.tcl $NODES $X $Y $PACKET_SIZE $RATE
    

    # Extract metrics using AWK and append to CSV
    awk -f metrics.awk congestion.tr | awk -v n=$NODES -v x=$X -v y=$Y -v p=$PACKET_SIZE -v r=$RATE '{
        printf "%s,%s,%s,%s,%s,", n, x, y, p, r; print $0
    }' >> $OUTPUT_FILE
    echo "Running: ns congestion.tcl $NODES $X $Y $PACKET_SIZE $RATE"
    echo "${i} th Iteration end"
done

