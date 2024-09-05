bubble_sort = lambda arr: [
    (arr[i], arr[i+1], arr[i], arr[i+1])
    for _ in range(len(arr))
    for i in range(len(arr) - 1)
    if arr[i] > arr[i + 1] and arr[i], arr[i + 1] == arr[i + 1], arr[i]
]
user_input = input("Enter numbers separated by spaces: ")
array = list(map(int, user_input.split()))
bubble_sort(array)
print("Sorted array:", array)
