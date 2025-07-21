FROM python:3.10-slim

# Set workdir
WORKDIR /app

# Copy files
COPY app.py .

# Install dependencies
RUN pip install flask flask-cors

# Run app
CMD ["python", "app.py"]
