if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())
        t1,t2=0,0
        for i in range(1,n+1):
            t1+=i
            t2+=(i**2)
        print((t1**2)-t2)
