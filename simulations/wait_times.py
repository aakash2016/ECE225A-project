import numpy as np

# def mean_wait_time(num_patients, service_rate, arrival_rate_min, arrival_rate_max):
#     # Simulate patient arrivals with uniform distribution
#     # inter_arrival_times = np.random.uniform(1 / arrival_rate_max, 1 / arrival_rate_min, num_patients)
#     inter_arrival_times = np.random.uniform(arrival_rate_min, arrival_rate_max, num_patients)
#     arrival_times = np.cumsum(inter_arrival_times)
#
#     # Simulate service times (exponentially distributed)
#     service_times = np.random.exponential(1 / service_rate, num_patients)
#
#     # Calculate waiting times (waiting time = service time + arrival time offset)
#     start_times = arrival_times
#     finish_times = start_times + service_times
#     # return np.mean(finish_times - arrival_times)
#     return np.mean(finish_times)

import numpy as np

def mean_wait_time(num_patients, service_rate, arrival_rate_min, arrival_rate_max):
    # Simulate patient arrivals with uniform distribution
    inter_arrival_times = np.random.uniform(arrival_rate_min, arrival_rate_max, num_patients)
    arrival_times = np.cumsum(inter_arrival_times)

    # Simulate service times (exponentially distributed)
    service_times = np.random.exponential(1 / service_rate, num_patients)

    # Initialize service start times and wait times
    service_start_times = np.zeros(num_patients)
    wait_times = np.zeros(num_patients)

    # First patient starts service upon arrival
    service_start_times[0] = arrival_times[0]

    # Compute wait times iteratively for each patient
    for i in range(1, num_patients):
        service_start_times[i] = max(arrival_times[i], service_start_times[i - 1] + service_times[i - 1])
        wait_times[i] = service_start_times[i] - arrival_times[i]

    # Return mean wait time
    return np.mean(wait_times)