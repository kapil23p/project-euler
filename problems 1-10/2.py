def r(n):
    a,b=2,8
    res=0
    while a<n:
        res+=a
        a,b=b,(4*b)+a
    return res

if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())
        print(r(n))