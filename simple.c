#include <Python.h>

static PyObject* noargs(PyObject* self, PyObject* args)
{
    Py_RETURN_NONE;
}

static PyObject* onearg(PyObject* self, PyObject* arg)
{
    Py_RETURN_NONE;
}

static PyObject* varargs(PyObject* self, PyObject* args)
{
    Py_RETURN_NONE;
}


static PyMethodDef SimpleMethods[] = {
    {"noargs", (PyCFunction)noargs, METH_NOARGS, ""},
    {"onearg", (PyCFunction)onearg, METH_O, ""},
    {"varargs", (PyCFunction)varargs, METH_VARARGS, ""},
    {NULL, NULL, 0, NULL}
};

PyMODINIT_FUNC
initsimple(void)
{
    (void) Py_InitModule("simple", SimpleMethods);
}
