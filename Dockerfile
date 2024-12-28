FROM ubuntu:latest
LABEL authors="arisu"

ENTRYPOINT ["top", "-b"]


# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /code

# Copy the requirements file into the container
COPY requirements.txt /code/

# Install any dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container
COPY . /code/

# Expose port 8000 for the Django development server
EXPOSE 8000

# Run the command to start your Django app
CMD ["sh", "-c", "python manage.py makemigrations && python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]
