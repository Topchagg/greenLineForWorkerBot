
# Если в конце From - это ты получаешь от сервака т.е get запрос
# Если в конце To - это ты отправляешь на сервак т.е get params/post


# Приписка params - означает, что ты получаешь данные в url строке, и получитье её нужно через params т.е  
# someurl?status=True&code=698322 здесь параметры это status:True и code=698322

# Приписка data - означает, что внутри объекта запроса будет dictionary с данными {} key,value

# Это работает в обе стороны, т.е где написано парамс значит отправляешь ввиде параметров
# Где написано data - отправляешь с помощью data {}

# С помощью postman можешь отправлять mockData чтоб проверить каким образом отрабатывает твой тг бот

MockFSendAuthorizathionCodeFrom = { # Получаешь GET от сервера (Другой клиент вызывает это)  params
    "code": 512963,
    "chatID":51296382710222
}

MockCreateCodeToResetTo = { # Отправляешь GET http://127.0.0.1:8000/create-code-to-reset/ params
    "chatID": 51296382710222
}

MockChangeTgAccountTo = { # Отправляешь PATCH http://127.0.0.1:8000/change-tg-account/ data
    "code": 512963,
    "newChatID":512963827102221
}



# 
MockGetClosestTaskTo = { # Отправляешь GET http://127.0.0.1:8000/get-closest-task/ params
    "chatID": 51296382710222,
    "currentDate": "YYYY:MM:DD",
    "currentTime": "HH:MM"
}

MockGetClosestTaskFrom = { # http://127.0.0.1:8000/get-closest-task/ Возвращает  data
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