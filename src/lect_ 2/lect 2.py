def binarySearch(arr, l, r, x):
    if r >= l:
        mid = l + (r - l) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binarySearch(arr, l, mid-1, x)
        else:
            return binarySearch(arr, mid +1 , r, x)
    else:
        return -1
# Driver Code
arr = [2, 3, 4, 10, 40]
x = 10

# Function call
result = binarySearch(arr, 0, len(arr) - 1, x)

if result != -1:
    print(result)
else:
    print("Element is not present in array")

offset = 0


def tower_of_hanoi(n, from_rod, to_rod,mid_rod ):
    if n == 1:
        print(f"Chuyen dia 1 tu coc {from_rod} den coc {to_rod}")
        return
    tower_of_hanoi(n-1, from_rod, mid_rod, to_rod)
    print(f"Chuyen dia {n} tu coc {from_rod} den coc {to_rod}")
    tower_of_hanoi(n-1, mid_rod, to_rod, from_rod)

N = 3

# A, C, B are the name of rods
tower_of_hanoi(N, 'A', 'C', 'B')