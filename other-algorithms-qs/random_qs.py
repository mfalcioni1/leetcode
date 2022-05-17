def aprox_median(numbers, left, right):

    median_idx = len(numbers) // 2
    pivot = numbers[right]
    limit = left
    for j in range(left, right):
        if numbers[j] <= pivot:
            numbers[limit], numbers[j] = numbers[j], numbers[limit]
            limit += 1
    numbers[limit], numbers[right] = numbers[right], numbers[limit]

    if limit == median_idx:
        return numbers[limit]
    elif limit <= median_idx:
        return aprox_median(numbers, left + 1, limit)
    else:
        return aprox_median(numbers, left, limit - 1)

lst = [1, 2, 13, 14, 15, 18, 20]
aprox_median(lst, 0, len(lst) - 1)

def mystery(lst):
    i = 0
    for num in lst:
        lst[i] = lst[i] + num
        i += 1
    return lst

mystery([1,2,3,4])

# Threading 

from threading import Thread
import time

x = 0
def increment():
    global x
    time.sleep(.001)  # Wait 0.001 seconds.
    x = x + 1

for i in range(100):
    t = Thread(target=increment)  # Create a thread to execute increment.
    t.start()  # Start thread execution.

print(x) # output will be less than or equal to 100 every time.