# Данная библиотека помогает обрабатывать информацию
import constants

# Проверяет наличие значений множества в строке
def InSet(String: str, Set: set):
    for _ in Set:
        if _ in String:
            return True
    return False


# Меняет значения из множества в нужную строку
def ChangeFromSet(String: str, Set: set, Value: str = " "):
    for _ in Set:
        if _ in String:
            String = String.replace(_, Value)
    return String


# Убирает знаки препенания со строки
def RemovePunctuationMarks(String: str):
    Set = {'.', ',', '?', '!'}
    return ChangeFromSet(String, Set)

def SendDict(d):
    answer = ""
    for i, j in d.items():
        answer += f">{i}\n{j}\n\n"
    constants.send_message(answer)




# Requests should be a pointer to requests lib
def download_photo(i, attach, requests, config=None):
    if attach[i]['type'] == "photo":
        URL_TO_DOWNLOAD = max(attach[i]['photo']["sizes"], key=lambda x: x['height'])[
            "url"]
        response = requests.get(URL_TO_DOWNLOAD)
        # TODO: the path should be in config
        opened_file = open(
            f'{config.get_path()}/{i}.jpg',
            "wb")
        opened_file.write(response.content)
        opened_file.close()
