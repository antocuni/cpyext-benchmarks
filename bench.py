from util import Timer
import simple

N = 10000000
def bench(name, obj):
    with Timer('%s.noargs' % name):
        for i in xrange(N):
            obj.noargs()
    #
    with Timer('%s.onearg(None)' % name):
        for i in xrange(N):
            obj.onearg(None)
    #
    with Timer('%s.onearg(i)' % name):
        for i in xrange(N):
            obj.onearg(i)
    #
    with Timer('%s.varargs' % name):
        for i in xrange(N):
            obj.varargs(None, None)


bench('simple', simple)
print
bench(' Foo()', simple.Foo())
