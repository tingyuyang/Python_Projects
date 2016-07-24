def mendelInhe(a, b, c):
    total = a + b + c
    temp = total - 1
    aa = 1*((a/total)*((a-1)/temp)) 
    ab = 1*((a/total)*(b/temp)) 
    ac = 1*((a/total)*(c/temp))
    ba = 1*((b/total)*(a/temp))
    bb = 0.75*((b/total)*((b-1)/temp))
    bc = 0.5*((b/total)*(c/temp))
    ca = 1*((c/total)*(a/temp))
    cb = 0.5*((c/total)*(b/temp)) 
    cc = 0*((c/total)*((c-1)/temp))
    probs = aa + ab + ac + ba + bb + bc + ca + cb + cc
    return probs
