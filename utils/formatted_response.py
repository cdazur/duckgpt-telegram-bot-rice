# GPT response and formatting
import telebot
import re

from utils.ai import get_gpt_response

def escape_markdown(text):
    """Экранирует специальные символы для MarkdownV2."""
    escape_chars = r'_*[]()~`>#+-=|{}.!'
    return re.sub(f'([{re.escape(escape_chars)}])', r'\\\1', text)

# Инициализация, если необходимо
def initialize_user(user_id, user_messages, user_message_ids):
    if user_id not in user_messages:
        user_messages[user_id] = []
    if user_id not in user_message_ids:
        user_message_ids[user_id] = []

# General function to process and send responses
def send_responses(bot, message, user_id, user_messages, user_message_ids, content=None):
    # Initialize user data
    initialize_user(user_id, user_messages, user_message_ids)

    # Determine the content based on the message type
    if content is not None:
        # This is for photo or voice messages where we've extracted content
        user_content = content
    elif message.content_type == 'text':
        user_content = message.text
    else:
        # For any other type of message, we'll use a placeholder
        user_content = f"[{message.content_type.upper()} message]"

    print(f"User content: {user_content}")  # Debugging line

    # Add user message to the list
    user_messages[user_id].append({'role': 'user', 'content': user_content})

    # Set status "typing"
    bot.send_chat_action(message.chat.id, 'typing')

    # Get the response from GPT
    gpt_response = get_gpt_response(user_messages[user_id])

    print(f"GPT responses: {gpt_response}")

    if not gpt_response:
        bot.send_message(message.chat.id, "Sorry, I couldn't generate a response.")
        return

    # Filter out empty responses and join non-empty ones
    non_empty_responses = [response for response in gpt_response if response.strip()]
    if not non_empty_responses:
        bot.send_message(message.chat.id, "Sorry, I generated an empty response. Please try again.")
        return

    # Process each non-empty response and send separately
    for response in non_empty_responses:
        formatted_response = escape_markdown(response.strip())  # Escape special characters

        # Add the assistant's response to the user_messages list
        user_messages[user_id].append({'role': 'assistant', 'content': formatted_response})

        try:
            # Send the response in MarkdownV2 format
            sent_message = bot.send_message(message.chat.id, f"`{formatted_response}`", parse_mode="MarkdownV2")
            user_message_ids[user_id].append(sent_message.message_id)
        except telebot.apihelper.ApiTelegramException as e:
            print(f"Error sending message with MarkdownV2: {e}")
            # If MarkdownV2 fails, try sending without formatting
            try:
                sent_message = bot.send_message(message.chat.id, response)  # Send raw response without markdown
                user_message_ids[user_id].append(sent_message.message_id)
            except Exception as e:
                print(f"Error sending message without markdown: {e}")
