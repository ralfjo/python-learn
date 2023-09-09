# how to debug?
# 1. Explain the problem
# 2. Produce the bug again to see what went wrong
# 3. Evaluate the line by line
# 4. Check the underline portion
# 5. Use print()
# 6. Fix the error

def cumulative_sum(num):
    total = 0
    for i in range(1,num):
        # print(i)
        total += i
    return total

print(cumulative_sum(10))