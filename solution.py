from math import sqrt, ceil

def oneToNPrime(num):
    arr = [True] * (num + 1)
    arr[:2] = [False, False]
    
    for i in range(2, ceil(sqrt(num))):
        if not arr[i]:
            continue
        j = i * 2
        while j <= num:
            if arr[j]:
                arr[j] = False
            j += i

    cnt = str(arr).count("True")
    return cnt

print(oneToNPrime(1000))