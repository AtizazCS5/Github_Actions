import random
def estimate_pi(n):
    total_points_circle = 0
    total_points_all = 0
    for _ in range(n):
        x = random.uniform(0,1)
        y = random.uniform(0,1)
        dist = (x**2) + (y**2)
        if dist <= 1:
            total_points_circle +=1
        total_points_all += 1
    return 4 * (total_points_circle / total_points_all )

#print(estimate_pi(1000000))

def linear_search(my_list, key):
    count = 0
    for _ in my_list:
        if _ == key:
            return ('{} found at index {}'.format(_, count))
        count +=1
    return ('{} not found in the given list')

def binary_search(my_list, key):
    left = 0
    right = len(my_list) + 1
    mid = (left+right)//2
    while (left <= right):
        if (key == my_list[mid]):
            return ('{} found at index {}'.format(_, count))
        elif ()
            
            
            

my_list = [88, 13, 70, 32, 96, 46, 52, 63, 25, 11, 79]
arr = [10, 13, 25, 32, 40, 46, 52, 63, 70, 75, 79, 81, 84, 88, 90, 93, 96, 99]
#print(linear_search(my_list, 80))
#print(binary_search(arr,88))
        
#print(total)
