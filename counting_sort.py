import time

def counting_sort(array):
    begin = time.time()
    size = len(array)
    output = [0] * size
    max_element = max(array)
    count = [0] * (max_element + 1)

    for i in range(size):
        count[array[i]] += 1

    for i in range(1, max_element + 1):
        count[i] += count[i - 1]

    i = size - 1
    while i >= 0:
        output[count[array[i]] - 1] = array[i]
        count[array[i]] -= 1
        i -= 1

    for i in range(size):
        array[i] = output[i]
    
    end = time.time()
    difference = (end - begin) * 1_000
    print(f"Total runtime of the counting sort program is {difference:.1f} ms")