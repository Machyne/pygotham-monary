#!/usr/bin/env python
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt

from monary import Monary

m = Monary()
ages, = m.query('superuser', 'users', {}, ['Age'], ['int16'])
ages = ages.data[~ages.mask]

# the histogram of the data
n, bins, patches = plt.hist(ages, 80, normed=0, facecolor='blue', alpha=0.75)

plt.xlabel('Age')
plt.title('The age of Superuser members.')
plt.axis([0, 100, 0, 5000])
plt.grid(True)

plt.show()
