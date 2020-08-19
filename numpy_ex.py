import numpy as np

mid_scores = np.array([10, 20, 30])
final_scores = np.array([70, 80, 90])

total = mid_scores + final_scores
print(total)

import numpy as np

heights = np.array([1.83, 1.76, 1.69, 1.85, 1.77, 1.73])
weights = np.array([86, 74, 59, 96, 80, 68])

BMI = (weights / (heights * heights))
BMI = (weights / heights ** 2)

print(BMI)

import numpy as np

y = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

ny = np.array(y)
ny

import numpy as np

np.arange(5)
np.arange(1, 6)
np.arange(1, 10, 2)

np.linspace(0, 10, 100)

np.logspace(0, 5, 10)

y = np.arange(12)
y.reshape(3,4)
y.reshape(6,-1)

np.random.seed(100)
np.random.rand(5)

np.random.randn(5)
np.random.randn(5, 4)
m = 10; sigma = 2
m + sigma*np.random.randn(5)


import numpy as np
import matplotlib.pyplot as plt

m = 10
sigma = 2
x1 = np.random.randn(10000)
x2 = m + sigma * np.random.randn(10000)

plt.figure(figsize=(10,6))
plt.hist(x1, bins=20, alpha=0.4)
plt.hist(x2, bins=20, alpha=0.4)
plt.show()