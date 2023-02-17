def bin_search(arr=[], high=0, low=0, num=0):
    mid = int((high + low) / 2)
    if high <= low:
        return -1
    if num > arr[mid]:
        low = mid + 1
        return bin_search(arr, high, low, num)
    if num < arr[mid]:
        high = mid - 1
        return bin_search(arr, high, low, num)
    if num == arr[mid]:
        return mid


# arr = []
# fib cach tao list phu
def fib(arr, n):
    if n == 0:
        arr.append(0)
        return 0
    if n == 1:
        arr.append(1)
        return 1
    arr.append(fib(arr, n - 2) + fib(arr, n - 1))
    return arr[n]


# fib cach recurse k dung list phu
def fib2(n, a, b):
    if n == 0:
        return 0
    if n == 1:
        arr.append(1)
        return 1


# fib dung for
def fib3():
    a = b = 1
    for i in range(10):
        a, b = a + b, a

    arr = []
    print(fib(arr, 5))


# arr = [1,2,3,4,5]
# num = 0
# print(bin_search(arr, 4, 0, num))

def reverse_string(s=""):
    if len(s) == 0:
        return s
    else:
        return reverse_string(s[1:]) + s[0]


# def partition(arr, start, end):
#     pivot = arr[end]
#     i = start - 1
#     for j in range(start, end):
#         if arr[j] < pivot:
#             i+=1
#             tmp = arr[i]
#             arr[i] = arr[j]
#             arr[j] = tmp
#     i+=1
#     tmp = arr[i]
#     arr[i] = arr[end]
#     arr[end] = tmp
#
#     return i
# def quick_sort(arr, start, end):
#     if end <= start:
#         return
#     pivot = partition(arr, start, end)
#     quick_sort(arr, start, pivot-1)
#     quick_sort(arr, pivot+1, end)


def partition(arr, start, end):
    pivot = arr[end]
    i = start - 1
    for j in range(start, end):
        if arr[j] < pivot:
            i += 1
            tmp = arr[i]
            arr[i] = arr[j]
            arr[j] = tmp
    i += 1
    tmp = arr[i]
    arr[i] = arr[end]
    arr[end] = tmp
    return i


def sort(arr, start, end):
    if end <= start:
        return
    pivot = partition(arr, start, end)
    sort(arr, start, pivot - 1)
    sort(arr, pivot + 1, end)





arr = [9, 8, 5, 4, 3, 2, 1]
sort(arr, 0, len(arr) - 1)
print(arr)

s = "hello"
print(reverse_string(s))
