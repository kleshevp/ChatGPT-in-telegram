import telebot
import openai

bot = telebot.TeleBot('6040861692:AAHinu_RidoDgidgNIkOeo-Fp8fA7D_0xNU')
openai.api_key = "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"
messages = {}  # Словарь для сохранения сообщений по user_id
users = [..., ..., ..., ...] #Пользователи с доступом


@bot.message_handler(content_types=["text"])
def ping(message):
    if message.from_user.id in users:
        if "/clear_story" == message.text:
            user_id = message.from_user.id
            if user_id in messages:
                messages[user_id] = []  # Очищаем историю сообщений пользователя
                bot.reply_to(message, "История чата очищена.")
            else:
                bot.reply_to(message, "История чата пуста.")
        elif message.reply_to_message and message.reply_to_message.from_user.id == 6040861692 or message.chat.id == message.from_user.id:
            user_id = message.from_user.id
            if len(messages[user_id]) >= 4096:
                bot.reply_to(message, "Количество символов превышает 4096. Очистите историю сообщений с помощью команды /clear_story")
            else:
                user_id = message.from_user.id
                smart = bot.reply_to(message, "Я думаю...")
                user_id = message.from_user.id
                if user_id not in messages:
                    messages[user_id] = []

                # Сохраняем сообщение пользователя в словаре
                messages[user_id].append({"role": "user", "content": message.text})

                completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages[user_id])
                bot.reply_to(message, completion.choices[0].message.content)
                messages[user_id].append({"role": "assistant", "content": completion.choices[0].message.content})
                bot.delete_message(message.chat.id, smart.message_id)
        else:
            pass

bot.polling(none_stop=True)
