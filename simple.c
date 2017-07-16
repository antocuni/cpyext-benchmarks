#include <Python.h>

static PyObject* noargs(PyObject* self, PyObject* args)
{
    Py_RETURN_NONE;
}

static PyMethodDef SimpleMethods[] = {
    {"noargs", (PyCFunction)noargs, METH_NOARGS, ""},
    {NULL, NULL, 0, NULL}
};

PyMODINIT_FUNC
initsimple(void)
{
    (void) Py_InitModule("simple", SimpleMethods);
}
