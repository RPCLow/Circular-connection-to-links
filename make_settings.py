import json


def make_settings(language):
    if language.lower() == 'en':
        print('Hello! This is a customizable script that automatically connects you to Zoom class links.')
        print('All you need to do is activate the script during class time to be redirected to the link.')
        input('Press Enter to continue: ')

        num_lessons_per_day = int(input('How many lessons do you have per day? Enter a number: '))

        while True:
            num_days_per_week = int(input('How many days do you attend school per week? Enter a number: '))
            if num_days_per_week <= 7:
                break
            print('There are 7 days in a week, how can you attend school so many times in a week?')

        lesson_times = {}
        for i in range(1, num_lessons_per_day + 1):
            while True:
                lesson_start_end_time = input(
                    f'Write the start and end time for lesson {i}. (Example 9:00 9:45): ').split()
                if len(lesson_start_end_time) == 2:
                    lesson_times[str(i)] = {'Start': lesson_start_end_time[0], 'End': lesson_start_end_time[1]}
                    break
                print('Incorrect time format, please try again.')

        weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        schedule = {}
        lessons = set()
        for i in range(num_days_per_week):
            print(f'Write the schedule for lessons for {weekdays[i]}.')
            daily_schedule = {}
            for j in range(1, num_lessons_per_day + 1):
                lesson_name = input(f'Write the name of lesson {j}: ')
                lessons.add(lesson_name)
                daily_schedule[str(j)] = lesson_name
            schedule[weekdays[i]] = daily_schedule

        lesson_links = {}
        for lesson in lessons:
            link = input(f'Enter the link for the {lesson} lesson: ')
            lesson_links[lesson] = link if link else None
        lesson_links['Otherwise'] = input('Enter the link that will open if the link is not found: ')

        settings = {
            'lesson_times': lesson_times,
            'schedule': schedule,
            'lesson_links': lesson_links
        }
        with open('settings.json', 'w', encoding='UTF-8') as json_file:
            json.dump(settings, json_file, ensure_ascii=False, indent=2)

        print('All set! Congratulations on successful setup!')

    elif language.lower() == 'ru':
        print('Привет! Это настраиваемый скрипт, который сам подключает тебя к учебным ссылкам Zoom.')
        print('От тебя лишь требуется активировать скрипт в период урока, чтобы скрипт перенес тебя по ссылке.')
        input('Нажмите клавишу Enter для продолжения: ')

        num_lessons_per_day = int(input('Сколько уроков у вас в день? Введите число: '))

        while True:
            num_days_per_week = int(input('Сколько дней в неделю вы учитесь? Введите число: '))
            if num_days_per_week <= 7:
                break
            print('В неделе 7 дней, как ты можешь учиться так много раз в неделю?')

        lesson_times = {}
        for i in range(1, num_lessons_per_day + 1):
            while True:
                lesson_start_end_time = input(
                    f'Напишите через пробел время начало и конца {i} урока. (Пример 9:00 9:45): ').split()
                if len(lesson_start_end_time) == 2:
                    lesson_times[str(i)] = {'Начало': lesson_start_end_time[0], 'Конец': lesson_start_end_time[1]}
                    break
                print('Некорректный формат времени, попробуйте еще раз.')

        weekdays = ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресенье']
        schedule = {}
        lessons = set()
        for i in range(num_days_per_week):
            print(f'Напишите расписание для уроков для {weekdays[i]}.')
            daily_schedule = {}
            for j in range(1, num_lessons_per_day + 1):
                lesson_name = input(f'Напишите название {j} урока: ')
                lessons.add(lesson_name)
                daily_schedule[str(j)] = lesson_name
            schedule[weekdays[i]] = daily_schedule

        lesson_links = {}
        for lesson in lessons:
            link = input(f'Введите ссылку на предмет {lesson}: ')
            lesson_links[lesson] = link if link else None
        lesson_links['Иначе'] = input('Введите ссылку, которая будет открываться если ссылка не будет найдена: ')

        settings = {
            'lesson_times': lesson_times,
            'schedule': schedule,
            'lesson_links': lesson_links
        }
        with open('settings.json', 'w', encoding='UTF-8') as json_file:
            json.dump(settings, json_file, ensure_ascii=False, indent=2)

        print('Все готово! Поздравляю с успешной настройкой!')

    else:
        print('Unsupported language. Please choose either EN or RU.')
