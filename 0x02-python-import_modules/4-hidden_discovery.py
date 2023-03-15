#!/usr/bin/python3
import dis
import types
def print_module_name():
    with open('hidden_4.pyc', 'rb') as f:
        code = f.read()
        module = types.ModuleType('hidden_4')
        module.__file__ = 'hidden_4.pyc'
        code_object = compile(code, 'hidden_4.pyc', 'exec')
        exec(code_objecf, module.__dict__)
        for instr in dis.get_instructions(code_object):
            if instr.opname == 'STORE_NAME' and not instr.argval.startswitch('__'):
                print(instr.argv)
    print_module_names()
