from dash.models import GenerationHistory


def process_with_ai(generation_request: GenerationHistory):
    input_file = generation_request.document
    with open(input_file.path, 'r') as file:
        content = file.read()
        print(content)
