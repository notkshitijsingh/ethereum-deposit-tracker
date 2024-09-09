# Ethereum Deposit Tracker
 The objective is to develop a robust and efficient Ethereum Deposit Tracker to monitor and record ETH deposits on the Beacon Deposit Contract.

This can be run as a Python instance or be deployed on Docker.

**Please note that this is not the final version of this tracker and there are plans to add Grafana and Telegram integration.**

## Run on Local Machine
Download the ZIP of the source code from the Code section or the latest release from the [Releases](https://github.com/notkshitijsingh/ethereum-deposit-tracker/releases) section. Extract the contents into a folder of your choice and then open your terminal in the main folder and run the following command:
```
python tracker.py
```
And you're done! You'll be able to view the real-time logs of your tracker in the same terminal that you ran the command above in and the results will also be reflected in the _deposits.db_ and _tracker.log_ files

## Setup (Docker Desktop)
Download the ZIP of the source code from the Code section or the latest release from the [Releases](https://github.com/notkshitijsingh/ethereum-deposit-tracker/releases) section. Extract the contents into a folder of your choice and then open your terminal in the main folder and run the following command:
```
docker build -t ethereum-deposit-tracker .
```
You can change the name `ethereum-deposit-tracker` for any other name you wish to use for your docker build.

After the Docker is done building an image, run the following command:
```
docker run -d ethereum-deposit-tracker
```

And you're done! You'll be able to view the real-time logs of your tracker from the container in your Docker dashboard.

![SUBMITTED AS ASSIGNMENT](https://img.shields.io/badge/SUBMITTED%20AS%20ASSIGNMENT-LUGANODES%20HIRING%20PROCESS-green?style=flat)