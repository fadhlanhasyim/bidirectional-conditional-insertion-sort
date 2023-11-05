import math
import time

def bcis(arr):
    begin = time.time()
    N = len(arr) - 1
    SL = 0
    SR = N

    while SL < SR:
        swap(arr, SR, SL + (SR - SL) // 2)

        if arr[SL] == arr[SR]:
            if is_equal(arr, SL, SR) == -1:
                return

        if arr[SL] > arr[SR]:
            swap(arr, SL, SR)

        if (SR - SL) >= 100:
            for i in range(SL + 1, math.floor(math.sqrt(SR - SL) + 1)):
                if arr[SR] < arr[i]:
                    swap(arr, SR, i)
                elif arr[SL] > arr[i]:
                    swap(arr, SL, i)
        else:
            i = SL + 1

        lc = arr[SL]
        rc = arr[SR]
        while i < SR:
            curr = arr[i]
            if curr >= rc:
                arr[i] = arr[SR - 1]
                ins_right(arr, curr, SR, N)
                SR -= 1
            elif curr <= lc:
                arr[i] = arr[SL + 1]
                ins_left(arr, curr, SL, 0)
                SL += 1
                i += 1
            else:
                i += 1
        SL += 1
        SR -= 1
    
    end = time.time()
    difference = (end - begin) * 1_000
    print(f"Total runtime of the BCIS program is {difference:.1f} ms")

def is_equal(arr, SL, SR):
    for k in range(SL + 1, SR):
        if arr[k] != arr[SL]:
            swap(arr, k, SL)
            return k
    return -1

def ins_right(arr, curr, SR, R):
    j = SR
    while j <= R and curr > arr[j]:
        arr[j - 1] = arr[j]
        j += 1
    arr[j - 1] = curr

def ins_left(arr, curr, SL, L):
    j = SL
    while j >= L and curr < arr[j]:
        arr[j + 1] = arr[j]
        j -= 1
    arr[j + 1] = curr

def swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp
