import time

def concatenate_with_plus(n):
    result = ""
    for i in range(n):
        result += str(i)
    return result

def concatenate_with_join(n):
    result = ''.join(str(i) for i in range(n))
    return result
    
def concatenate_with_fstrings(n):
    result = ''.join(f'{i}' for i in range(n))
    return result

start_time = time.time()
print(concatenate_with_plus(10000000))
end_time = time.time()

start_time1 = time.time()
print(concatenate_with_join(10000000))
end_time1 = time.time()

start_time2 = time.time()
print(concatenate_with_fstrings(10000000))
end_time2 = time.time()

print(f"plus->Using '+': {end_time - start_time} seconds")
print(f"join->Using '+': {end_time1 - start_time1} seconds")
print(f"fstr->Using '+': {end_time2 - start_time2} seconds")