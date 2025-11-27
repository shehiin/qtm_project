def solve_scheduling(machines, total_time):
    n = len(machines)
    S = total_time
    
    dp = [[0 for _ in range(S + 1)] for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        benefit_table = machines[i - 1]
        max_alloc = len(benefit_table) - 1
        
        for s in range(S + 1):
            best = 0
            for x in range(min(s, max_alloc) + 1):
                value = benefit_table[x] + dp[i - 1][s - x]
                if value > best:
                    best = value
            dp[i][s] = best
    
    allocations = [0] * n
    remaining = S
    
    for i in range(n, 0, -1):
        benefit_table = machines[i - 1]
        max_alloc = len(benefit_table) - 1
        target = dp[i][remaining]
        
        for x in range(min(remaining, max_alloc) + 1):
            if benefit_table[x] + dp[i - 1][remaining - x] == target:
                allocations[i - 1] = x
                remaining -= x
                break
    
    max_benefit = dp[n][S]
    
    return allocations, max_benefit

