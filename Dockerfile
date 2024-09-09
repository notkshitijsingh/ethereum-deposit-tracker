# use an official python runtime as a parent image
FROM python:3.9-slim

# set the working directory in the container
WORKDIR /ethereum-deposit-tracker

# copy the current directory contents into the container at /ethereum-deposit-tracker
COPY . /ethereum-deposit-tracker

# install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# expose port 80 (if needed for future extensions)
EXPOSE 80

# run tracker.py when the container launches
CMD ["python", "tracker.py"]