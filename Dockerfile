RUN mkdir -p /usr/src/app

#Copy Source
COPY . /usr/src/app/

#Change to working directory
WORKDIR /usr/src/app

#install apt dependencies if any
RUN if [ -f /usr/src/app/apt_requirements.txt ]; then apt-get update && \
    apt-get install -y $(cat ./apt_requirements.txt) && \
    apt-get clean && apt-get autoremove ; fi

# Install dependenciemes
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
