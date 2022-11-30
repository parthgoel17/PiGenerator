# starts with 314...
# generates digits including 3.
def Pi(digits):
    lis=[]
    q, r, t, k, n, l = 1, 0, 1, 1, 3, 3
    while digits!=len(lis):
        if 4*q+r-t < n*t:
            lis.append(n)
            nr = 10*(r-n*t)
            n  = ((10*(3*q+r))//t)-10*n
            q *= 10
            r  = nr
        else:
            nr = (2*q+r)*l
            nn = (q*(7*k)+2+(r*l))//(t*l)
            q *= k
            t *= l
            l += 2
            k += 1
            n  = nn
            r  = nr
    return lis
            
