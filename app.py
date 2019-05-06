import ray
import time
import os
from multiprocessing import cpu_count

import multiprocessing

def regular_method():
    time.sleep(sleep)
    return 1

@ray.remote
def ray_method():
    time.sleep(sleep)
    return 1

def run_regular_method():
    start = time.time()
    results = [regular_method() for i in range(executions)]
    end = time.time()
    return results, end - start

def run_ray_method():
    ray.init()
    start = time.time()
    results = ray.get([ray_method.remote() for i in range(executions)])
    end = time.time()
    return results, end - start

def run_apply_async_regular_method():
    pool = multiprocessing.Pool(number_of_cpus)
    start = time.time()
    result_objects = [pool.apply_async(regular_method) for i in range(executions)]
    results = [r.get() for r in result_objects]
    pool.close()
    pool.join()
    end = time.time()
    return results, end - start

def print_result(method_type, results, elapsed_time):
    print('\n**************************************')
    print(f'{method_type} method elapsed time: {elapsed_time}')
    print(f'results: {results}')
    print('**************************************\n')

if __name__ == "__main__":
    print('Reading environment variables...')
    number_of_cpus = cpu_count()
    sleep = int(os.environ.get('SLEEP', 2))
    executions = int(os.environ.get('EXECUTIONS', number_of_cpus))

    print('\n**********************')
    print(f'Utilizing {number_of_cpus} cores')
    print(f'sleep time: {sleep}')
    print(f'executions: {executions}')
    print('**********************\n')
    
    results, elapsed_time = run_regular_method()
    print_result('regular', results, elapsed_time)

    results, elapsed_time = run_ray_method()
    print_result('ray', results, elapsed_time)

    results, elapsed_time = run_apply_async_regular_method()
    print_result('apply_async', results, elapsed_time)
