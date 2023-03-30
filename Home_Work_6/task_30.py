def list_arr(a, d, n):
    res = []
    for i in range(n):
        res.append(a + i * d)
    return res

a = int(input())
d = int(input())
n = int(input())
print(list_arr(a, d, n))
