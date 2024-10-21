# utils/ai.py
from duckduckgo_search import DDGS

def get_gpt_response(messages):

    prompt = f"Создайте остроумный, привлекающий внимание простой текст, чтобы произвести впечатление на нового друга. Как будто ты пишешь другу SMS. Ответ менее 75 символов. Предоставьте 3 вариантов без нумерации. DO NOT USE HYPHEN: {messages[-1]['content']}"
    
    try:
        results = DDGS().chat(prompt, model='gpt-4o-mini')
        # return results

        # Разделяем результаты на отдельные строки
        options = results.strip().split('\n')
        return options

    except Exception as e:
        return f"Ошибка запроса: {str(e)}"
