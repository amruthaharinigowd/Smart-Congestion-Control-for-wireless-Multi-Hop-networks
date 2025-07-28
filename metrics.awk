BEGIN {
    sent = 0; received = 0; loss = 0;
    delay_sum = 0; count_delay = 0;
    jitter_sum = 0; count_jitter = 0;
    last_recv_time = 0;
    throughput = 0;
}

{
    event = $1;
    time = $2;
    pkt_size = $6;

    if (event == "s") {
        sent++;
        seqno[$7] = time;
    }

    if (event == "r") {
        received++;
        if (seqno[$7] != "") {
            delay_sum += (time - seqno[$7]);
            count_delay++;
        }

        if (last_recv_time > 0) {
            jitter_sum += (time - last_recv_time);
            count_jitter++;
        }
        last_recv_time = time;
    }
}

END {
    loss = sent - received;
    avg_delay = (count_delay > 0) ? delay_sum / count_delay : 0;
    avg_jitter = (count_jitter > 0) ? jitter_sum / count_jitter : 0;
    throughput = (received > 0) ? (received * 512 * 8) / time : 0;

    printf "%d,%d,%d,%.2f,%.6f,%.2f,%.6f\n", sent, received, loss,(sent>0? (received/sent)*100:0), avg_delay, throughput, avg_jitter;
}


