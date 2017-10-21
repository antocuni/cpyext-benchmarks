import time
import simple
#from pypytools.jitview import JitView

N = 10000000

def bench(name, obj):
    a = time.time()
    for i in xrange(N):
        obj.noargs()
    b = time.time()
    print '%s.noargs      : %.2f secs' % (name, b-a)
    #
    a = time.time()
    for i in xrange(N):
        obj.onearg(None)
    b = time.time()
    print '%s.onearg(None): %.2f secs' % (name, b-a)
    #
    a = time.time()
    for i in xrange(N):
        obj.onearg(i)
    b = time.time()
    print '%s.onearg(i)   : %.2f secs' % (name, b-a)
    #
    a = time.time()
    for i in xrange(N):
        obj.varargs(None, None)
    b = time.time()
    print '%s.varargs     : %.2f secs' % (name, b-a)


bench('simple', simple)
print
bench(' Foo()', simple.Foo())
