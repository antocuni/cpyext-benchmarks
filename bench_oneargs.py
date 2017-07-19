import time
import simple

N = 10000000
X=100

def main():
    a = time.time()
    for i in xrange(N):
        simple.onearg(None)
    b = time.time()
    print 'onearg(None): %.2f secs' % (b-a)
    #
    a = time.time()
    for i in xrange(N):
        simple.onearg(1)
    b = time.time()
    print 'onearg(1)   : %.2f secs' % (b-a)
    
    a = time.time()
    for i in xrange(N):
        simple.onearg(i)
    b = time.time()
    print 'onearg(i)   : %.2f secs' % (b-a)
    #
    a = time.time()
    for i in xrange(N):
        simple.onearg(i%2)
    b = time.time()
    print 'onearg(i%%2) : %.2f secs' % (b-a)
    #
    a = time.time()
    for i in xrange(N):
        simple.onearg(X)
    b = time.time()
    print 'onearg(X)   : %.2f secs' % (b-a)
    #
    a = time.time()
    for i in xrange(N):
        simple.onearg((1,))
    b = time.time()
    print 'onearg((1,)): %.2f secs' % (b-a)
    #
    a = time.time()
    for i in xrange(N):
        simple.onearg((X,))
    b = time.time()
    print 'onearg((X,)): %.2f secs' % (b-a)
    #
    a = time.time()
    for i in xrange(N):
        simple.onearg((i,))
    b = time.time()
    print 'onearg((i,)): %.2f secs' % (b-a)


main()
