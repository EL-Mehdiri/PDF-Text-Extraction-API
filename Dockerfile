FROM ubuntu:22.04

RUN apt-get update && apt-get install -y \
    nodejs \
    npm \
    python3 \
    python3-pip \
    python3-venv

# Set the working directory
WORKDIR /usr/src/app

COPY package*.json ./
RUN npm install

COPY requirements.txt ./

RUN python3 -m venv /usr/src/app/myenv
RUN /usr/src/app/myenv/bin/pip install --no-cache-dir -r requirements.txt

COPY . .

# Expose the port for the app
EXPOSE 5100

CMD /bin/bash -c "source /usr/src/app/myenv/bin/activate && npm start"