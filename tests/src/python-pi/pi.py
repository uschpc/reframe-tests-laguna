# Estimate pi in parallel using multiple cores

import random
import multiprocessing
from multiprocessing import Pool
import time

# Calculate the number of points in the unit circle out of n points
def monte_carlo_pi_part(n):
    count = 0

    for i in range(n):
        x = random.random()
        y = random.random()

        # If within the unit circle
        if (x * x) + (y * y) <= 1:
            count = count + 1

    return count

if __name__=='__main__':
    cores = multiprocessing.cpu_count()

    start = time.time()

    # Number of points to use for the pi estimation
    n = 5000000000

    # Create iterable list
    # Each worker process gets (n / cores) number of points
    part_count = [n // cores] * cores

    # Create the worker pool
    pool = Pool(processes = cores)

    # Parallel map
    count = pool.map(monte_carlo_pi_part, part_count)

    est = 4 * (sum(count) / (n * 1.0))

    end = time.time()

    elapsed = end - start

    print("Estimate of pi:", est)
    print("Elapsed time:", elapsed)
