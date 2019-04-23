# cpyext-benchmarks

In the following, `python` can refer either to CPython or PyPy.

To run the benchmarks:

```
$ python setup.py build_ext --inplace
$ python bench.py
```

It is also possible to run the benchmarks under valgrind/callgrind. You might
want to comment out the benchmarks you are not interested in, to save time and
not to clutter the profile data.  Please note that benchmarks are run for a
smaller number of iterations when you run them under valgrind.

```
$ python valgrind_build.py
$ ./callgrind python bench.py
```

Callgrind produces one or more file named `callgrind.out.PID`. To visualize
them, use `kcachegrind`.
