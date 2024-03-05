import os.path
import time
import webbrowser
from get_something import *
from playsound import playsound
from make_settings import make_settings


# Функция ожидания
def wait_until_next_lesson_start(settings):
    for i in range(get_minutes_until_next_nearest_lesson(settings)):
        hours = get_minutes_until_next_nearest_lesson(settings) // 3600
        minutes = (get_minutes_until_next_nearest_lesson(settings) - (hours * 3600)) // 60
        seconds = get_minutes_until_next_nearest_lesson(settings) - hours * 3600 - minutes * 60
        print(f'До следующего урока {hours} часов, {minutes} минут, {seconds} секунд.')
        time.sleep(1)


# Функция, которая проверяет, есть ли файл в директории
def is_settings_in_directory():
    file_settings = 'settings.json'
    return os.path.exists(file_settings)


# Функция, которая проигрывает музыку
def play_sound(name_music):
    playsound(get_path() + '\\' + name_music)


# Функция для подключения к уроку
def connection_to_lessons(settings):
    day_of_week = get_day()
    number_of_lessons = get_number_lessons(settings)
    if number_of_lessons:
        current_lessons = settings['расписание'][day_of_week][number_of_lessons]
        if settings['ссылка_на_уроки'][current_lessons]:
            link_to_lessons = settings['ссылка_на_уроки'][current_lessons]
        else:
            link_to_lessons = settings['ссылка_на_уроки']['Иначе']
        webbrowser.open_new_tab(link_to_lessons)
        if link_to_lessons == settings['ссылка_на_уроки']['Иначе']:
            playsound('dj_arbuz.mp3')
    wait_until_next_lesson_start(settings)


def main():
    if is_settings_in_directory():
        settings = get_settings()
        while True:
            connection_to_lessons(settings)
    else:
        language_choice = input('Choose language (EN/RU): ')
        make_settings(language_choice)


if __name__ == "__main__":
    main()
