# handlers/text.py
from utils.formatted_response import initialize_user, send_responses

def register_text_handler(bot, user_messages, user_message_ids):
    @bot.message_handler(func=lambda message: True)
    def handle_message(message):
        user_id = message.from_user.id

        # Initialize user data
        initialize_user(user_id, user_messages, user_message_ids)

        # Skip command messages
        if message.text.startswith('/'):
            return

        # Save message ID
        user_message_ids[user_id].append(message.message_id)

        # Process and send AI responses
        send_responses(bot, message, user_id, user_messages, user_message_ids, message.text)
