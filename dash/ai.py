import io
import time

import random
import string

from django.core.files.base import ContentFile

from dash.models import GenerationHistory


def generate_random_file():
    # Generate random text
    random_text = ''.join(random.choices(string.ascii_letters + string.digits, k=10))

    # Create a BytesIO object
    file_in_memory = io.BytesIO(random_text.encode())

    return file_in_memory


def process_with_ai(generation_request: GenerationHistory):
    input_file = generation_request.document
    with open(input_file.path, 'r') as file:
        content = file.read()
        print(content)

        # Generating Random File to upload
        # Replace with actual generation logic
        file_in_memory = generate_random_file()
        time.sleep(10)

        content_file = ContentFile(file_in_memory.getvalue())
        generation_request.presentation.save('output_generation', content_file)

        generation_request.save()
