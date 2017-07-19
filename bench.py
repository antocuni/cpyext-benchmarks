import time
import simple
from pypytools.jitview import JitView

N = 10000000

def main():
    a = time.time()
    for i in xrange(N):
        simple.noargs()
    b = time.time()
    print 'noargs : %.2f secs' % (b-a)
    #
    a = time.time()
    for i in xrange(N):
        simple.onearg(None)
    b = time.time()
    print 'onearg : %.2f secs' % (b-a)
    #
    a = time.time()
    for i in xrange(N):
        simple.varargs(None, None)
    b = time.time()
    print 'varargs: %.2f secs' % (b-a)

main()
