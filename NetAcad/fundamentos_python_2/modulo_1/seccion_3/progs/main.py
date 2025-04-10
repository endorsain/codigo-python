from helper import addModules

addModules(__file__, 'modules')

import module

print(module.__counter)
zeroes = [0 for i in range(5)]
ones = [1 for i in range(5)]
print(module.suml(zeroes))
print(module.prodl(ones))
print(module.__counter)


