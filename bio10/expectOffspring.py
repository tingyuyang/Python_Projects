import math

parentDictionary = {'AA-AA':19962, 'AA-Aa':17373, 'AA-aa':19148, 'Aa-Aa':18108, 'Aa-aa':17918, 'aa-aa':16074}
prob = {'AA-AA':1, 'AA-Aa':1, 'Aa-Aa':.75, 'AA-aa':1, 'Aa-aa':.5, 'aa-aa':0}

kids = 0
for key in parentDictionary:
    kids += (2*(parentDictionary[key]*prob[key]))
    
print (kids)
