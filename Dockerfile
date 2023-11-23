FROM python:3.9-slim-buster

# Set the working directory to /app
WORKDIR /app

RUN pip install uvicorn

# Copy the requirements file
COPY requirements.txt .

# Install dependencies
RUN pip install -r requirements.txt

# Copy the application code
COPY . .

# Expose port 8000
EXPOSE 8000

# Start the Uvicorn server
CMD ["uvicorn", "--host=0.0.0.0", "--port=8000", "pptai.asgi:application"]
