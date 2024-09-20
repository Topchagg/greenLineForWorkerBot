data = {
    "name":"Захар Головіцький",
    "date":"17.09.2024",
    "start":"14:00",
    "end":"19:40",
    "approximatePrice":1350,
    "adres":"Осіння 39",
    "numberPhone": "096387827",
    "code":"1943",
    "customerName":"Софія Меднова"
}

def NewOrderMessage(data):
    message = ''
    message += "Доброго дня " + data['username'] + '\n\n'
    message += f"Ви отримали замовлення на " + data['date'] + '\n'
    message += f"Приблизний початок: " + data["start"] + '\n'
    message += f"Приблизний кінець: " + data["end"] + '\n'
    message += f"Приблизний заробіток: " + str(data["approximatePrice"]) + " грн" + '\n'
    message += f"Адреса: " + data["adres"] + '\n'
    message += f"Номер телефона замовника: " + data["numberPhone"] + '\n'

    return message




def sendCodeMessage(data):
    message = ''
    message += "Доброго дня " + data['username'] + '\n\n'
    message += "Не повідомляйте цей код нікому, він потрібен щоб ввійти в ваш аккаунт, якщо це не ви відправили запрос на отримання цього коду, тоді просто нічого не робіть" + "\n\n\n"
    message += "===================\n"
    message += "Код для входу у аккаунт: " + data["code"] + "\n"
    message += "===================\n"

    return message


def startMessage():
    message = ''
    message += "Доброго дня, для продовження потрібно ввести код який був вам відправленний на електронну пошту!"

    return message


def registrationTrueMessage(data):
    message = ''
    message += f"Чудово, " + data["username"] + "," + " ваш аккаунт було активовано, тепер ви можете ввійти на свій професійний аккаунт за допомогою логіну та паролю який було відправлено вам на електронну пошту"

    return message


def checkClosestTask(data):
    message = ''
    message += "Ось інформація щодо найближащого замовлення " + "\n\n\n"

    message += f"Ви отримали замовлення на " + data['date'] + '\n'
    message += f"Приблизний початок: " + data["start"]+ '\n'
    message += f"Приблизний кінець: " + data["end"]+ '\n'
    message += f"Приблизний заробіток: " + str(data["approximatePrice"]) + " грн" + '\n\n' 
    message += f"Адреса: " + data["adres"]+ '\n'
    message += f"Ім'я та Фамілія замовника: " + data["customerName"] + '\n'
    message += f"Номер телефона замовника: " + data["numberPhone"]+ '\n'

    return message

def changeAccountMessage(code):
    message = ''
    message += "Доброго дня, введіть цей код в чат бота з ішного аккаунту!" + '\n\n\n'
    message += "============="
    message += str(code)
    message += "============="

