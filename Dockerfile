FROM python:3.10.10-slim-buster

WORKDIR /app

# Copy only required files and directories
COPY requirements.txt app.py main.py /app/
COPY e_commerce /app/e_commerce
COPY templates /app/templates

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port Flask app runs on
EXPOSE 8000

# Run the Flask application
CMD ["python", "app.py"]
