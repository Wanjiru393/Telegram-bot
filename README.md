# Telegram Bot

This is a simple Python-based Telegram bot that uses the Telegram API to respond to user messages with random pictures.

## Requirements

- Python 3.x
- `requests` library
- `python-telegram-bot` library

## Installation

1. Clone the repository to your local machine.
2. Install the required libraries by running `pip install -r requirements.txt`.
3. Create a new bot and get its API token from the [Telegram BotFather](https://t.me/botfather).
4. Replace the `token` value in the `updater` object with your API token.
5. Run the bot script by executing `python bot.py`.

## Usage

Once the bot is running, you can start a chat with it in Telegram and send it a message to get a random picture. To get a random static image, type "Static Image" and to get a random picture, type "Random Picture".

## Contributing

Pull requests and bug reports are welcome. Please make sure to follow the existing code style and include tests for any new features.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
