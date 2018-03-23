from util import Timer
import simple

N = 10000000
def bench_module():
    with Timer('simple.noargs'):
        for i in xrange(N):
            simple.noargs()

    with Timer('simple.onearg(None)'):
        for i in xrange(N):
            simple.onearg(None)

    with Timer('simple.onearg(i)'):
        for i in xrange(N):
            simple.onearg(i)

    with Timer('simple.varargs'):
        for i in xrange(N):
            simple.varargs(None, None)

    with Timer('simple.allocate_int'):
        for i in xrange(N):
            simple.allocate_int()

    with Timer('simple.allocate_tuple'):
        for i in xrange(N):
            simple.allocate_tuple()

def bench_type():
    obj = simple.Foo()
    with Timer('Foo().noargs'):
        for i in xrange(N):
            obj.noargs()

    with Timer('Foo().onearg(None)'):
        for i in xrange(N):
            obj.onearg(None)

    with Timer('Foo().onearg(i)'):
        for i in xrange(N):
            obj.onearg(i)

    with Timer('Foo().varargs'):
        for i in xrange(N):
            obj.varargs(None, None)

    with Timer('len(Foo())'):
        for i in xrange(N):
            len(obj)

    with Timer('Foo()[0]'):
        for i in xrange(N):
            obj[0]

bench_module()
print
bench_type()
