def powerSetRecursive(A):
    res = list()
    def generate(A, r, index):
        res.append(r.copy())
        for i, n in enumerate(A[index:]):
            generate(A, r+[n], index+i+1)
    generate(A, [], 0)
    return res


import math
  
def powerSetIterative(A): 
      
    ps_size = int(math.pow(2, len(A)))
    res = list()
    for n in range(ps_size): 
        res.append([])
        for i in range(len(A)):
            if(n & 1 << i > 0): 
                res[n].append(A[i])
    return res

# print(powerSetRecursive([1,2,3]))
print(powerSetIterative([1,2,3]))