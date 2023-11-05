import time
import tracemalloc

def counting_sort(array):
    tracemalloc.start()
    begin = time.time()
    
    size = len(array)
    output = [0] * size

    # Find the maximum element in the array
    max_element = max(array)

    # Initialize count array
    count = [0] * (max_element + 1)

    # Store the count of each element in count array
    for i in range(size):
        count[array[i]] += 1

    # Store the cumulative count
    for i in range(1, max_element + 1):
        count[i] += count[i - 1]

    # Find the index of each element of the original array in count array
    # Place the elements in the output array
    i = size - 1
    while i >= 0:
        output[count[array[i]] - 1] = array[i]
        count[array[i]] -= 1
        i -= 1

    # Copy the sorted elements into the original array
    for i in range(size):
        array[i] = output[i]
    
    end = time.time()
    difference = (end - begin) * 1_000
    print(f"Total runtime of the counting sort program is {difference:.1f} ms")

    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    print(f"Memory usage BCIS: {peak / (1024 * 1024):.1f} MB")