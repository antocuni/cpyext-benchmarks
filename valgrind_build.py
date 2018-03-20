from cffi import FFI
ffibuilder = FFI()

ffibuilder.cdef("""
    void callgrind_start(void);
    void callgrind_stop(void);
""")


ffibuilder.set_source("_valgrind", """
#include <valgrind/callgrind.h>
void callgrind_start(void) {
  CALLGRIND_START_INSTRUMENTATION;
}

void callgrind_stop(void) {
  CALLGRIND_STOP_INSTRUMENTATION;
  CALLGRIND_DUMP_STATS;
}
""",
    libraries=[])

if __name__ == "__main__":
    ffibuilder.compile(verbose=True)
