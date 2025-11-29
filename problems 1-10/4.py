is_palindromic = lambda n: str(n)==str(n)[::-1]

dd = sorted([i * j for i in range(101, 1000) 
             for j in range(121, 1000, (1 if i % 11 == 0 else 11)) 
             if (p:= i * j) >= 101101 and is_palindromic(p)],
    reverse=True)

for _ in range(int(input())):
    K = int(input())
    q = min(dd, key=lambda x:x>=K)
    print(q)    
