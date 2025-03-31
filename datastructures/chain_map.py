from collections import ChainMap

dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
dict3 = {'d': 5}

chain = ChainMap(dict1, dict2, dict3)

print(chain['a'])  
print(chain['b'])  
print(chain['c'])  
print(chain['d'])  

print(list(chain.keys()))    
print(list(chain.values()))  

dict4 = {'e': 6}
new_chain = chain.new_child(dict4)
print(new_chain['e'])  

print('e' in chain)    