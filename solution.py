def quickSort(arr, start, end):
    if start >= end:
        return
    
    left, right = start, end

    pivot = arr[(start + end) // 2]

    while left <= right:
        while left <= right and arr[left] < pivot:
            left += 1
        while left <= right and arr[right] > pivot:
            right -= 1
        if left <= right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1
    
    quickSort(arr, start, right)
    quickSort(arr, left, end)
