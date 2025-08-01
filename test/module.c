#include <Python.h>

static PyObject* example_add(PyObject* self, PyObject* args) {
    int a, b;
    if (!PyArg_ParseTuple(args, "ii", &a, &b)) {
        return NULL;  
    }
    int result = a + b;
    return PyLong_FromLong(result);
}

static PyMethodDef ExampleMethods[] = {
    {"add", example_add, METH_VARARGS, "Add two integers"},
    {NULL, NULL, 0, NULL} 
};

static struct PyModuleDef examplemodule = {
    PyModuleDef_HEAD_INIT,
    "example", 
    "Example module that adds two integers", 
    -1,
    ExampleMethods
};

PyMODINIT_FUNC PyInit_example(void) {
    return PyModule_Create(&examplemodule);
}
