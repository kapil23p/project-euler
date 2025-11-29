def s(n, k):
    p = (n-1) // k
    return k * p * (p + 1) // 2

if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())
        print(s(n,3)+s(n,5)-s(n,15))