from util import Timer
import numpy as np

N = 100000

def bench():
    myarray = np.zeros(10)
    with Timer('getitem'):
        total = 0
        for i in xrange(N):
            total += myarray[5]

bench()
