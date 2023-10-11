FROM python:3.10

# Set PYTHONUNBUFFERED to ensure unbuffered output
ENV PYTHONUNBUFFERED=1

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY requirements.txt ./

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# # Make port 8000 available to the world outside this container
# EXPOSE 8000

# # Define the command to run your application
# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]