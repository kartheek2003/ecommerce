FROM python:3.10.10-slim-buster

WORKDIR /app

# Copy everything including app.py, requirements.txt, etc.
COPY . /app

# (Optional, if artifacts are gitignored or excluded from build context)
COPY artifacts /app/artifacts

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

CMD ["python", "app.py"]
