# handlers/photo.py
import os
from PIL import Image
import pytesseract
from utils.formatted_response import send_responses, initialize_user

# Укажите путь к исполняемому файлу tesseract
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
pytesseract.pytesseract.tesseract_cmd = '/usr/bin/tesseract'

def register_photo_handler(bot, user_messages, user_message_ids):
    @bot.message_handler(content_types=['photo'])
    def handle_photo(message):
        user_id = message.from_user.id

        # Initialize user data
        initialize_user(user_id, user_messages, user_message_ids)

        # Получение файла изображения
        file_info = bot.get_file(message.photo[-1].file_id)
        downloaded_file = bot.download_file(file_info.file_path)

        # Сохранение изображения
        photo_path = f"photo_{user_id}.jpg"
        with open(photo_path, 'wb') as new_file:
            new_file.write(downloaded_file)

        # Открытие изображения и распознавание текста
        image = Image.open(photo_path)
        text = pytesseract.image_to_string(image, lang='rus')

        print(f"OCR extracted text: {text}")

        # Удаление временного файла
        if os.path.exists(photo_path):
            os.remove(photo_path)

        # Сохранение ID сообщения
        user_message_ids[user_id].append(message.message_id)

        # Убедитесь, что текст не пустой
        if not text.strip():
            context = "Не удалось распознать текст на изображении."

        # Process and send AI responses based on extracted text
        send_responses(bot, message, user_id, user_messages, user_message_ids, text)