array = [-6, -20, 80, 60, 12, 111, 7, 77, 5, 65]

def bubble_sort():
    n = len(array)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if array[j] > array[j+1]:
               array[j], array[j+1] = array[j+1], array[j]
            print(array)
    return array

print(bubble_sort()) 













