# time taken by program

import time

# Record the start time
start_time = time.time()

# Your Python program or code here
def factorial(n):
    if n==0 or n==1:
        return 1
    else :
        return n * factorial(n-1)

# n = int(input('Enter a number : '))
result = factorial(100)

print('Factorial : ', result)   # 93326215443944152681699238856266700490715968264381621468592963895217599993229915608941463976156518286253697920827223758251185210916864000000000000000000000000

# Record the end time
end_time = time.time()

# Calculate the elapsed time
elapsed_time = end_time - start_time

# Print the elapsed time
print(f"Time taken: {elapsed_time} seconds")
