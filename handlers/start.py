# handlers/start.py
def register_start_handler(bot, user_message_ids):
    @bot.message_handler(commands=['start'])
    def send_welcome(message):
        user_id = message.from_user.id

        # Инициализация списка сообщений и их идентификаторов для нового пользователя
        if user_id not in user_message_ids:
            user_message_ids[user_id] = []

        bot_message = bot.send_message(
            message.chat.id,
            """
            <b>Бот поможет вам в игре знакомств, делая беседу притягательной.</b>
            
            <b>Удобный и полезный:</b>
            🖼️ Загружайте скрины
            🗣️ Присылайте голосовые 
            📋 Кликните что бы скопировать
            🍚 Три варианта ответа
            
            <b>🦾 Команда</b> 
            /new - для очистки истории сообщений
        """, parse_mode="html"
        )
        user_message_ids[user_id].append(bot_message.message_id)
        user_message_ids[user_id].append(message.message_id)
        # user_message_ids[user_id].extend(bot_message.message_id, message.message_id)