# 01bags
def findBag(w, v, c):
    dp = [ 0 for _ in range(c + 1)]
    for i in range(1, len(v) + 1):
        for j in range(c, w[i - 1] - 1, -1):
                dp[j] = max(dp[j], dp[j - w[i - 1]] + v[i - 1])
    return dp[-1]

# download in desktop
path = "C:\\Users\\Administrator\\Desktop\\Test-Data-of-01-knapsack-problem\\"
for i in range(10):
    pathin = path + 'beibao' + str(i) + '.in'
    pathout = path + 'beibao' + str(i) + '.out'
    w = []
    v = []
    result0 = -1
    with open(pathin, 'r') as fr:
        lines = fr.read().splitlines()
        for line in lines:
            line = line.split(' ')
            w.append(int(line[0]))
            v.append(int(line[1]))
        c = w[0]
        w = w[1:]
        v = v[1:]
        result0 = findBag(w, v, c)

    result2 = -2
    with open(pathout, 'r') as fr:
        lines = fr.read().splitlines()
        result2 = int(lines[0])
    
    # return true
    print(result0 == result2)