from numpy import arange
from timeit import Timer

Nelements = 100000
Ntimeits = 10000

n = arange(Nelements)
l = list(range(Nelements))
d = [{"key": x} for x in range(Nelements)]

t_numpy = Timer("n.mean()", "from __main__ import n")
t_list = Timer("sum(l)/len(l)", "from __main__ import l")
t_dict = Timer("sum(i['key'] for i in d)/len(d)", "from __main__ import d")

print("numpy: %.3e" % (t_numpy.timeit(Ntimeits)/Ntimeits,))
print("list:  %.3e" % (t_list.timeit(Ntimeits)/Ntimeits,))
print("dict:  %.3e" % (t_dict.timeit(Ntimeits)/Ntimeits,))
