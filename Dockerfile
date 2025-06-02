FROM python:3.10.10-slim-buster

WORKDIR /app

# Copy only what's needed, explicitly
COPY requirements.txt app.py main.py /app/
COPY artifacts /app/artifacts

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

CMD ["python", "app.py"]

