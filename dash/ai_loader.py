import os

def get_ai_func():
    loadai=os.environ.get("LOADAI","False")=="True"
    if loadai:
        from .ai import process_with_ai
        return process_with_ai

    return lambda x : x
