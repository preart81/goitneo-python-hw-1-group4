from datetime import datetime, timedelta
from collections import defaultdict


def get_birthdays_per_week(users: []):
    """
    Функція отримує на вхід список users і виводить у консоль (за допомогою print) список користувачів, яких потрібно привітати по днях на наступному тижні.
    Наприклад:

    {"name": "Bill Gates", "birthday": datetime(1955, 10, 28)}

    Дні тижня сортуються
    """
    today = datetime.today().date()
    # today = datetime(2023, 12, 5).date()  # перевіримо як працює в понеділок 4-12-2023

    # if today is Monday - move the start_date 2 days earlier to check the weekend
    start_day = today - timedelta(days=2) if today.weekday() == 0 else today

    # debug
    # print(
    #     f"today = {today.strftime('%a %d.%m.%Y')}, start_day = {start_day.strftime('%a %d.%m.%Y')}"
    # )

    birthdays_week = defaultdict(list)
    weekdays = [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday",
    ]

    for u in users:
        name: str = u["name"]
        birthday: datetime = u["birthday"].date()
        birthday_this_year = birthday.replace(year=start_day.year)
        if birthday_this_year < start_day:
            birthday_this_year = birthday_this_year.replace(
                year=birthday_this_year.year + 1
            )

        delta_days = (birthday_this_year - start_day).days

        if delta_days < 7:
            # debug
            # print(name, birthday, birthday_this_year.strftime("%A"))

            if birthday_this_year.weekday() < 5:  # skip Sun, Sat
                birthdays_week[birthday_this_year.weekday()].append(name)
            else:
                birthdays_week[0].append(name)  # move Sun, Sat to Mon

    start_week_day = 0
    # Згідно умови Тиждень починається з понеділка, тому по замовчуванню сортуємо з Понеділка
    # Але зручніше відсортувати дні так, щоб першим був сьогоднішній день тижня, а останнім - вчорашній
    # для цього потрібно задати
    # start_week_day = start_day.weekday()
    birthdays_week = dict(
        sorted(
            birthdays_week.items(),
            key=lambda key: (key[0] < start_week_day) * 7 + key[0] - start_week_day,
        )
    )

    for u in birthdays_week:
        print(f"{weekdays[u]}: {', '.join(birthdays_week[u])}")
    return
