from typing import Final
from telegram import Update, InputFile
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext
import validators
import yt_dlp as youtube_dl  # Using yt-dlp for downloading media

TOKEN: Final = 'replace this with your API key'
bot_username: Final = 'replace this your bot username'
returbasd;

async def start_command(update: Update, context: CallbackContext):
    await update.message.reply_text('Hello! I am a video/audio downloader bot.')


def handle_response(text: str) -> str:
    processed: str = text.lower()
    if 'hi' in processed:
        return 'Hey there...!'
    elif 'hey' in processed:
        return 'Hey there..!'
    return 'Sorry, I did not understand that.'


def is_valid_url(url: str) -> bool:
    """Check if the given URL is in a valid format."""
    return validators.url(url)


def download_media(url: str, output_dir: str = './downloads') -> str:
    """Download video or audio from the given URL."""
    ydl_opts = {
        'outtmpl': f'{output_dir}/%(title)s.%(ext)s',
        'format': 'bestaudio/best',  # Download the best audio format
        'noplaylist': True,  # Avoid downloading playlists
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(url, download=True)
        filename = f"{output_dir}/{info_dict['title']}.{info_dict['ext']}"
    return filename


async def handle_message(update: Update, context: CallbackContext):
    message_type: str = update.message.chat.type
    text: str = update.message.text
    print(f'user({update.message.chat.id}) in {message_type}: "{text}"')

    if message_type == 'group':
        if bot_username in text:
            new_text: str = text.replace(bot_username, '').strip()
            response: str = handle_response(new_text)
        else:
            return
    else:
        if is_valid_url(text):
            # Download the media
            try:
                file_path = download_media(text)
                with open(file_path, 'rb') as file:
                    await update.message.reply_document(InputFile(file, filename=file_path))
                response = 'Your media has been downloaded and sent.'
            except Exception as e:
                response = f'An error occurred: {e}'
        else:
            response: str = handle_response(text)

    print('Bot:', response)
    await update.message.reply_text(response)


async def error(update: Update, context: CallbackContext):
    print(f'Update {update} caused an error: {context.error}')


if __name__ == '__main__':
    print('Starting bot...')
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(MessageHandler(filters.ALL, handle_message))
    app.add_error_handler(error)

    print('Polling...')
    app.run_polling(poll_interval=3)
