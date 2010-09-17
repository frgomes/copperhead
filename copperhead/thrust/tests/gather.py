#
#  Copyright 2008-2010 NVIDIA Corporation
#  Copyright 2009-2010 University of California
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
#

import autopath

from copperhead import *
import numpy as np
from copperhead import thrust



i = CuArray(np.array([0, 2, 4, 6, 8, 1, 3, 5, 7, 9], dtype=np.int32))
x = CuArray(np.array([0, 1, 0, 1, 0, 1, 0, 1, 0, 1], dtype=np.int32))
g = thrust.gather(x, i)
print(g)

i = CuArray(np.array([0, 2, 4, 6, 8, 1, 3, 5, 7, 9], dtype=np.int32))
x = CuArray(np.array([0, 1, 0, 1, 0, 1, 0, 1, 0, 1], dtype=np.float32))
g = thrust.gather(x, i)
print(g)



