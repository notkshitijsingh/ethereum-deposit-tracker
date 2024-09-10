# Ethereum Deposit Tracker
 The objective is to develop a robust and efficient Ethereum Deposit Tracker to monitor and record ETH deposits on the Beacon Deposit Contract.

This can be run as a Python instance or be deployed on Docker.

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

## Telegram Bot Notifications Setup
For setting up notifications for the Telegram bot [`@grays_eth_bot`](https://web.telegram.org/k/#@grays_eth_bot), you will need the chat ID of your Telegram account where you need the notifications. You can add these in the list of chat IDs in the file `chat_id.txt` in a new line. Here is a tutorial on how to get your chat ID on Telegram:
1. Search for `@RawDataBot` on Telegram or [click here](https://web.telegram.org/k/#@RawDataBot) to be lead to it.
2. Click on the `Start` button or type `/start` in the chat and click on send.
3. You will get a JSON object with some data on it the `id` under the `chat` section is your chat ID. It would look like this:
```
 "chat": {
            "id": your-chat-id,
            "first_name": "Kshitij",
            "last_name": "Singh",
            "username": "notkshitijsingh",
            "type": "private"
        },
```

![SUBMITTED AS ASSIGNMENT](https://img.shields.io/badge/SUBMITTED%20AS%20ASSIGNMENT-LUGANODES%20HIRING%20PROCESS-green?style=flat)