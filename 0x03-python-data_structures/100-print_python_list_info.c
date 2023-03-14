#include <Python.h>
#include <object.h>
#include <listobject.h>

/**
 * @create: create a C function
 * @print: use the C function created to print some basic info about python lists
 */
void print_python_list_info(PyObject *p)
{
	long int size = PyList_Size(p);
	int i;
	PyListObject *obj = (PyListObject *)p;

	printf("[*] Size of the Python List = %li\n", size);
	printf("[*] Allocated = %li\n", obj->allocated);
	
	for (i = 0; i < size; i++)
		printf("Element %i: %s\n", i, Py_Type(obj->ob_item[i])->tp_name);
}
