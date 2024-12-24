# Курсовая работа «ТГ-чат-бот «Обучалка английскому языку»» по курсу «Базы данных»

## [База данных для бота](create_db.py)
## [Телеграм бот](main.py)

# Документация по использованию программы.

## Введение

***Этот Telegram-бот предназначен для помощи в изучении английского языка.
Он позволяет пользователям добавлять слова, удалять их, а также получать случайные слова для практики.***

## Команды

### /start или /cards
***Запускает бота.***

**Пример использования:**
```
/start
```

### /help
***Выводит список доступных команд и краткое описание их назначения.***

**Пример использования:**
```
/help
```

### /clear
***Очищает прогресс пользователя и удаляет все добавленные слова из базы данных. 
После выполнения этой команды все слова будут сброшены, и база данных будет возвращена в исходное состояние.***

**Пример использования:**
```
/clear
```

## Взаимодействие с ботом

### Добавление и удаление слов
***Пользователь может добавлять и удалять слова, используя соответствующие команды на панели***

### Получение случайного слова
***Бот предоставляет пользователю случайное слово из базы данных, которое будет отображено в формате:*** `target_word -> translate_word`.

### Получение других слов
***Бот получает из базы данных три других случайных слова для предоставления выбора вариантов ответа.***

### Состояния
***Бот хранит данные пользователей и их прогресс в базе данных PostgreSQL.
Это позволяет отслеживать, на каком этапе взаимодействия находится пользователь.***

