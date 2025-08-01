#define PY_SSIZE_T_CLEAN
#include <Python.h>
#include <stdio.h>

int my_tracefunc(PyObject *obj, PyFrameObject *frame, int what, PyObject *arg) {
    switch (what) {
        case PyTrace_CALL:
            printf("Function call\n");
            break;
        case PyTrace_LINE:
            printf("Line executed\n");
            break;
        case PyTrace_RETURN:
            printf("Function return\n");
            break;
        default:
            break;
    }
    return 0;
}

static PyObject* start_tracing(PyObject *self, PyObject *args) {
    PyEval_SetTrace(my_tracefunc, NULL);
    Py_RETURN_NONE;
}

static PyObject* stop_tracing(PyObject *self, PyObject *args) {
    PyEval_SetTrace(NULL, NULL);
    Py_RETURN_NONE;
}

static PyMethodDef Methods[] = {
    {"start_tracing", start_tracing, METH_NOARGS, "Start tracing"},
    {"stop_tracing", stop_tracing, METH_NOARGS, "Stop tracing"},
    {NULL, NULL, 0, NULL}
};

static struct PyModuleDef moduledef = {
    PyModuleDef_HEAD_INIT,
    "mytrace",
    NULL,
    -1,
    Methods
};

PyMODINIT_FUNC PyInit_mytrace(void) {
    return PyModule_Create(&moduledef);
}