Telegram bot that generates "rizz" replies using the Duck.ai GPT-4o-mini free API:

# Rice Bot

The Rice Bot is a Telegram bot that generates "rizz" replies using the Duck.ai GPT-4o-mini free API. The bot can also extract text from uploaded photos using OCR and transcribe voice messages using FFmpeg, then use that text as input to the GPT-4o-mini API.

## Features

- Generate "rizz" replies using the Duck.ai GPT-4o-mini free API
- Extract text from uploaded photos using OCR
- Transcribe voice messages using FFmpeg and use the text as input to the GPT-4o-mini API
- Replies are sent in three separate messages as options

## Requirements

- Python 3.x
- Telegram Bot API token
- FFmpeg (for voice message transcription)
- Tesseract (for screenshot text recognition)
- Python libraries:
  - `pyTelegramBotAPI`
  - `duckduckgo-search`
  - `python-dotenv`
  - `SpeechRecognition`
  - `pydub`
  - `Pillow`
  - `pytesseract`
  - `ffmpeg-python`

## Installation

1. Clone the repository:
```
git clone https://github.com/cdazur/duckgpt-telegram-bot-rice.git
```

2. Install the required Python libraries:
```
pip install -r requirements.txt
```

3. Set the environment variables:
```
.env TELEGRAM_TOKEN=YOUR_BOT_TOKEN
```

4. Run the bot:
```
python main.py
```

## Usage

1. Start a conversation with the Rice Bot on Telegram [@RiceRiceBabyBot](https://t.me/ricericebabybot)
2. Send a message to the bot, and it will generate three "rizz" reply options.
3. To use the OCR or voice message transcription features, send a photo or voice message to the bot, and it will extract the text and use it as input to the GPT-4o-mini API.

## Contributing

If you find any issues or have suggestions for improvements, feel free to open an issue or submit a pull request [@magnetiser](https://t.me/magnetiser)
