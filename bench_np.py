from util import Timer
import numpy as np

N = 10000000

def bench_getitem():
    myarray = np.zeros(10)
    with Timer('getitem'):
        total = 0
        for i in xrange(N/10):
            myarray[5]

def bench_mean():
    myarray = np.array([12.34])
    with Timer('np.mean'):
        for i in xrange(N/100):
            np.mean(myarray)

bench_getitem()
bench_mean()
