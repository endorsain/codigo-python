import os
from helper import addModules

addModules(__file__, os.path.join('packages', 'extra.zip'))

import extra.good.best.sigma as sig
import extra.good.alpha as alp
import extra.iota as io

print(sig.funS())
print(alp.funA())