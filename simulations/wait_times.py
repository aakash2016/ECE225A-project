import numpy as np

def mean_wait_time(num_patients, service_rate, arrival_rate_min, arrival_rate_max):
    # Simulate patient arrivals with uniform distribution
    inter_arrival_times = np.random.uniform(1 / arrival_rate_max, 1 / arrival_rate_min, num_patients)
    arrival_times = np.cumsum(inter_arrival_times)

    # Simulate service times (exponentially distributed)
    service_times = np.random.exponential(1 / service_rate, num_patients)

    # Calculate waiting times (waiting time = service time + arrival time offset)
    start_times = arrival_times
    finish_times = start_times + service_times
    return np.mean(finish_times - arrival_times)
