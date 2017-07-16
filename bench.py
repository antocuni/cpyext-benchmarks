import time
import simple

N = 10000000

def main():
    a = time.time()
    for i in xrange(N):
        simple.noargs()
    b = time.time()
    print '%.2f secs' % (b-a)

main()
