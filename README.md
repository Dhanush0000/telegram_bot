# YouTube Video Downloader Telegram Bot

Welcome to the **YouTube Video Downloader Telegram Bot**! This bot allows you to easily download any YouTube video using its URL directly from Telegram. Built using Python, this project utilizes the `python-telegram-bot` library to interact with Telegram and the `pytube` library to download videos from YouTube.

This README will guide you through setting up the bot, using it, and contributing to the project.

## Table of Contents

1. [Features](#features)
2. [Getting Started](#getting-started)
3. [Requirements](#requirements)
4. [Setup and Configuration](#setup-and-configuration)
5. [Usage](#usage)
6. [License](#license)
7. [Contributing](#contributing)

---

## Features

- **Download Videos**: Download YouTube videos in different qualities.
- **URL Input**: Simply send a YouTube video URL to the bot to get the download link.
- **Multiple Quality Options**: Get multiple quality options for the video based on what is available.
- **User-Friendly**: Easy-to-use interface with Telegram's chat system.

---

## Getting Started

These instructions will help you get a copy of the bot up and running on your local machine for development and testing purposes.

### Requirements

- Python 3.x
- `python-telegram-bot` library
- `pytube` library
- A Telegram Bot Token (you can create one by chatting with the [BotFather](https://core.telegram.org/bots#botfather)).

---

## Setup and Configuration

### Step 1: Install Dependencies

First, you need to install the necessary Python libraries. Open a terminal and run the following command:

```bash
pip install python-telegram-bot pytube
```

### Step 2: Set Up Telegram Bot

1. **Create a new bot** on Telegram by chatting with [BotFather](https://core.telegram.org/bots#botfather).
2. After creating the bot, you will get a **Bot Token**. Copy this token as it will be needed to authenticate the bot.

### Step 3: Configure the Bot

1. Clone this repository to your local machine or download the project files.
   
   ```bash
   git clone https://github.com/your-username/youtube-video-downloader-bot.git
   ```

2. Open the `bot.py` file and replace the following line with your own Telegram Bot Token:

   ```python
   TOKEN = 'YOUR_BOT_TOKEN'
   ```

---

## Usage

### Step 1: Running the Bot

Once you’ve set up the bot, you can start it by running the following command in the terminal:

```bash
python bot.py
```

The bot will start listening for incoming messages on Telegram.

### Step 2: Interacting with the Bot

1. Open Telegram and search for your bot by its username.
2. Start a conversation with the bot.
3. Send the YouTube video URL you want to download.
4. The bot will respond with a message containing the available video download options.
5. Select the quality and download the video.

---

## License

This project is open source and available under the [MIT License](LICENSE).

---

## Contributing

Feel free to contribute to this project by submitting bug fixes, enhancements, or new features. To contribute:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Implement your changes.
4. Test the changes locally.
5. Submit a pull request.

---

Thank you for using the **YouTube Video Downloader Telegram Bot**! Happy downloading! 🎥📲
