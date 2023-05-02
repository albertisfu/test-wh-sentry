

FROM python:3.10-slim

# Set environment variables
ENV PYTHONUNBUFFERED=1

# Set the working directory
WORKDIR /app

# Copy requirements.txt and install dependencies
COPY test_w_sentry/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY test_w_sentry .

# Expose the port the app runs on
EXPOSE 8081

# Run the application
CMD ["gunicorn", "--bind", "0.0.0.0:8081", "test_w_sentry.wsgi:application"]