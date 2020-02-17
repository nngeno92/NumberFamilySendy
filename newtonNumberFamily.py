import numpy as np
def calculate_total_photos(even, odd):
    total = 0
    m = min(odd, even)
    combination_sums = calculate_combination_sums(m)
    if even > odd:
        total += (combination_sums[odd]*(even-odd))
    elif odd > even:
        total += (combination_sums[even]*(odd-even))
        
    total += combination_sums[m]
    total += np.sum(combination_sums[0:m])*2
    return total
           
    
def calculate_combination_sums(n):
    combinations = np.eye(n+1)
    combinations[0,:] = [1]*(n+1)
    for j in range(1, n+1, 1):
        for i in range(1,j+1):
            combinations[i,j] = combinations[i,j-1] + combinations[i-1,j-1]
    combinations[0,0] = 0
    return np.sum(combinations[1:, :], axis=0)
