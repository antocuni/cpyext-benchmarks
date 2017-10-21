#include <Python.h>

/* module-level functions */

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

/* types */

typedef struct {
    PyObject_HEAD
} FooObject;

static PyTypeObject Foo_Type = {
    PyVarObject_HEAD_INIT(NULL, 0)
    "simple.Foo",              /* tp_name */
    sizeof(FooObject),         /* tp_basicsize */
    0,                         /* tp_itemsize */
    0,                         /* tp_dealloc */
    0,                         /* tp_print */
    0,                         /* tp_getattr */
    0,                         /* tp_setattr */
    0,                         /* tp_compare */
    0,                         /* tp_repr */
    0,                         /* tp_as_number */
    0,                         /* tp_as_sequence */
    0,                         /* tp_as_mapping */
    0,                         /* tp_hash */
    0,                         /* tp_call */
    0,                         /* tp_str */
    0,                         /* tp_getattro */
    0,                         /* tp_setattro */
    0,                         /* tp_as_buffer */
    Py_TPFLAGS_DEFAULT,        /* tp_flags */
    "Foo objects",             /* tp_doc */
    0,                         /* tp_traverse */
    0,                         /* tp_clear */
    0,                         /* tp_richcompare */
    0,                         /* tp_weaklistoffset */
    0,                         /* tp_iter */
    0,                         /* tp_iternext */
    SimpleMethods,             /* tp_methods, reuse the same functions */
};

PyMODINIT_FUNC
initsimple(void)
{
    PyObject* m;

    Foo_Type.tp_new = PyType_GenericNew;
    if (PyType_Ready(&Foo_Type) < 0)
        return;

    m = Py_InitModule("simple", SimpleMethods);
    Py_INCREF(&Foo_Type);
    PyModule_AddObject(m, "Foo", (PyObject *)&Foo_Type);
}
