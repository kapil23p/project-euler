if __name__ == '__main__':
    t = int(input().strip())
    l=[2,3,5,7,11,13,17,19,23,29,31,37]
    for t_itr in range(t):
        n = int(input().strip())
        res=1
        for i in range(len(l)):
            v=l[i]
            while v<=n:
                v*=l[i]
            v/=l[i]
            res*=(v if v<=n else 1)
        print(int(res))
