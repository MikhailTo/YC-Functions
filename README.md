# YC-Functions
Yandex Cloud Functions (Handlers) for save objects (dicts) in a json file and etc

work-test - Скрытый проект для упращения жизни себе и тем, с кем работаю. 

Инструкция (в наполнении), как создать подобное:
1. Создать Сервисный аккаунт (Service accaunt) ...
2. Создать Секрет (Lockbox) ...
3. Создать Облачную функцию (Cloud Functions) ...
4. Создать Ведро (Bucket) ...
3. Cоздать в корне Облачной функции (Cloud Functions) папку .aws c файлами config и credentials

config:
```
[default]
  region=AWS_DEFAULT_REGION
```

credintials:
```
[default]
  aws_access_key_id = AWS_ACCESS_KEY_ID
  aws_secret_access_key = AWS_SECRET_ACCESS_KEY
```

Где AWS_DEFAULT_REGION - Переменные окружения "ru-central1", 
а AWS_ACCESS_KEY_ID и AWS_SECRET_ACCESS_KEY - секреты ключей сервисного аккаунта.

Делалось все согласно Инструкций YC и документаций и т.д.
