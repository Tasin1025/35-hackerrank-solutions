t = int(input().strip())

def solve(ws, x):
    memo = {}

    def backtrack(index):
        if index == len(x):
            return []

        if index in memo:
            return memo[index]

        for w in ws:
            if x.startswith(w, index):
                result = backtrack(index + len(w))
                if result is not None:
                    memo[index] = [w] + result
                    return memo[index]

        memo[index] = None
        return None

    answer = backtrack(0)
    return answer

for _ in range(t):
    n = int(input().strip())
    ws = input().strip().split()
    x = input().strip()
    
    answer = solve(ws, x)
    if answer is None:
        print("WRONG PASSWORD")
    else:
        print(" ".join(answer))
