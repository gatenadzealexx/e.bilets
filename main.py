"""Вариант 4 - Сервис резервирования билетов:
Функционал:
• Разработка схемы базы данных для мероприятий, мест и билетов
• Простые операции, такие как добавление/удаление/редактирование
событий/мест, вывод информации о событии/месте по названию
• Сложные операции, такие как поиск события по месту, поиск
события/курса/whatever по частичному совпадению названия
• Функционал для бронирования и отмены билетов"""
import db

def print_menu():
    print("Выберите нужную комманду: ")
    print("0.Выход")
    print("1.Список мероприятий и дат проведения")
    print("2.Количество свободных билетов")
    print("3.Показать детальную информацию по названию мероприятия (дата проведения, кол-во свободных билетов")
    print("4.Добавить мероприятие")
    print("5.Поиск мероприятия по названию")
    print("6.Бронирование билета")
    print("7.Отмена бронирования")

def app():
        db.init_db()
        print("Таблицы успешно созданы!")
        print("Вас приветствует онлайн-афиша")
        while True:
            print_menu()
            cmd = int(input("Введите номер команды: "))
            if cmd==0:
                print("До свидания!!!")
                break

            elif cmd==1:
                print("=" * 20)
                print("Список мероприятий :")
                events = db.get_all_eventes()
                for event in events:
                    print(f"ID: {event[0]} - Название: {event[1]} Дата :{event[2]}.")
                print("=" * 20)

            elif cmd==2:
                print("=" * 20)
                print("Список мест :")
                bilets = db.get_all_bilets()
                for bilet in bilets:
                    print(f"ID: {bilet[0]} - Номер билета: {bilet[1]} , {bilet[2]}.")
                print("=" * 20)

            elif cmd==3:
                print("=" * 20)
                events_bilets = db.get_events_full_info()
                event_info = events_bilets
                print(event_info)
                print("=" * 20)

            elif cmd==4:
                print("=" * 20)
                print("Добавление нового мероприятия:")
                name_event = input("Введи название мероприятия: ")
                try:
                    db.create_events(name_event)
                    print("Мероприятие успешно создано!")
                except Exception as e:
                    print(f"Что-то пошло не так! {e}")
                print("=" * 20)

            elif cmd==5:
                print("=" * 20)
                query = input("Введите название или часть название мероприятия: ")
                events = db.search_events(query)
                for event in events:
                    print(f"ID: {event[0]} - Название: {event[1]} Дата: {event[2]}.")
                print("=" * 20)

            elif cmd==6:
                print("=" * 20)
                print("Бронирование билета:")
                bilet_id = int(input("Введи номер билета: "))
                try:
                    db.create_bilets(bilet_id)
                    print("Билет забронирован!")
                except Exception as e:
                    print(f"Что-то пошло не так! {e}")
                print("=" * 20)
            elif cmd==7:
                print("=" * 20)
                print("Отмена бронирования:")
                bilets = int(input("Введи номер билета: "))
                try:
                    db.delite_bilets(bilets)
                    print("Бронь отменена")
                except Exception as e:
                    print(f"Что-то пошло не так! {e}")
                print("=" * 20)
            else:
                print("Вы ввели несуществующую комманду, попробуйте ещё раз!!!")


app()


