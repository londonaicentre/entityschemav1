import os
import inspect

"""
prompt.py - functions to construct prompt from schema and txt
"""

def get_schema_code():
    from entityschemav1 import entityschemav1
    return inspect.getsource(entityschemav1)

def load_prompt_template(filename):
    current_dir = os.path.dirname(__file__)
    template_path = os.path.join(current_dir, 'prompts', filename)
    with open(template_path, 'r') as f:
        return f.read()

def create_system_prompt(filename='infer_prompt.txt'):
    template = load_prompt_template(filename)
    schema = get_schema_code()
    return template.replace('{SCHEMA}', schema)
