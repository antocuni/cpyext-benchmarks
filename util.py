from __future__ import absolute_import, division, print_function
import time
import _valgrind

class Timer(object):

    def __init__(self, name):
        self.name = name
        self.start = None
        self.stop = None

    def __enter__(self):
        _valgrind.lib.callgrind_start()
        self.start = time.time()

    def __exit__(self, etype, evalue, tb):
        self.stop = time.time()
        _valgrind.lib.callgrind_stop()
        name = self.name.ljust(25)
        print('%s: %.2f secs' % (name, self.stop-self.start))
