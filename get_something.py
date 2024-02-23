import calendar
import datetime
import json
import os


# Функция для получения названия текущего дня недели
def get_day():
    return calendar.day_name[datetime.datetime.now().weekday()]


# Функция для получения абсолютного пути к файлу настроек
def get_path_settings():
    filename = "settings.json"
    current_directory = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(current_directory, filename)


# Функция для чтения настроек из файла
def get_settings():
    with open(get_path_settings(), "r", encoding="UTF-8") as file:
        return json.load(file)


# Функция для получения текущего урока
def get_current_lesson(settings, current_time):
    for lesson_number, lesson_time in settings["время_уроков"].items():
        start_time = datetime.datetime.strptime(lesson_time["Начало"], "%H:%M").time()
        end_time = datetime.datetime.strptime(lesson_time["Конец"], "%H:%M").time()
        if start_time <= current_time <= end_time:
            return lesson_number
    return None


# Функция для получения минут до ближайшего урока
def get_minutes_until_next_nearest_lesson(settings):
    current_time = datetime.datetime.now().time()
    for lesson_number, lesson_time in settings["время_уроков"].items():
        start_time = datetime.datetime.strptime(lesson_time["Начало"], "%H:%M").time()
        if current_time < start_time:
            difference = datetime.datetime.combine(datetime.date.today(), start_time) - datetime.datetime.combine(
                datetime.date.today(), current_time)
            return int(difference.seconds) + 1
    else:
        return 3600


# Функция для получения номера текущего урока
def get_number_lessons(settings):
    current_time = datetime.datetime.now().time()
    return get_current_lesson(settings, current_time)
