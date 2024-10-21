# handlers/voice.py
import telebot
import os
import speech_recognition as sr
from pydub import AudioSegment
from utils.formatted_response import send_responses, initialize_user

# Добавьте путь к ffmpeg и ffprobe в системные переменные среды
os.environ['PATH'] = os.pathsep + os.environ['PATH']

def register_voice_handler(bot, user_messages, user_message_ids):
    @bot.message_handler(content_types=['voice'])
    def handle_voice(message):
        user_id = message.from_user.id

        # Скачивание голосового сообщения
        file_info = bot.get_file(message.voice.file_id)
        downloaded_file = bot.download_file(file_info.file_path)

        # Сохранение голосового сообщения как .ogg файл
        ogg_path = f"voice_{user_id}.ogg"
        wav_path = f"voice_{user_id}.wav"
        with open(ogg_path, 'wb') as new_file:
            new_file.write(downloaded_file)

        # Конвертация .ogg файла в .wav формат
        audio = AudioSegment.from_ogg(ogg_path)
        audio.export(wav_path, format='wav')

        recognizer = sr.Recognizer()
        audio_file = sr.AudioFile(wav_path)

        try:
            with audio_file as source:
                audio_data = recognizer.record(source)
                text = recognizer.recognize_google(audio_data, language='ru-RU')
        except sr.UnknownValueError:
            text = "Извините, не удалось распознать аудио."
        except sr.RequestError:
            text = "Ошибка при запросе к сервису распознавания."

        # Удаление временных файлов
        if os.path.exists(ogg_path) and os.path.exists(wav_path):
            os.remove(ogg_path)
            os.remove(wav_path)

        # Initialize user data
        initialize_user(user_id, user_messages, user_message_ids)

        # Сохранение ID сообщения
        user_message_ids[user_id].append(message.message_id)

        # Process and send AI responses based on extracted text
        send_responses(bot, message, user_id, user_messages, user_message_ids, text)
