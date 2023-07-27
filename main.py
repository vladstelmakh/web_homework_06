import sqlite3
from faker import Faker
def read_sql_query_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()
fake = Faker()

# Создание базы данных и подключение к ней
conn = sqlite3.connect('university.db')
cursor = conn.cursor()


main_1 = read_sql_query_file('main_1.sql')
main_2 = read_sql_query_file('main_2.sql')
main_3 = read_sql_query_file('main_3.sql')
main_4 = read_sql_query_file('main_4.sql')
main_5 = read_sql_query_file('main_5.sql')

# Создание таблиц
cursor.execute(main_1)

cursor.execute(main_2)

cursor.execute(main_3)

cursor.execute(main_4)

cursor.execute(main_5)

# Функции для заполнения таблиц
def fill_students_table(num_students):
    for _ in range(num_students):
        name = fake.name()
        group_id = fake.random_int(1, 3)
        cursor.execute('INSERT INTO students (name, group_id) VALUES (?, ?)', (name, group_id))

def fill_groups_table():
    groups = ['Group A', 'Group B', 'Group C']
    for group_name in groups:
        cursor.execute('INSERT INTO groups (name) VALUES (?)', (group_name,))

def fill_teachers_table(num_teachers):
    for _ in range(num_teachers):
        name = fake.name()
        cursor.execute('INSERT INTO teachers (name) VALUES (?)', (name,))

def fill_subjects_table(num_subjects):
    for _ in range(num_subjects):
        name = fake.job()
        teacher_id = fake.random_int(1, 3)
        cursor.execute('INSERT INTO subjects (name, teacher_id) VALUES (?, ?)', (name, teacher_id))

def fill_grades_table(num_grades):
    for _ in range(num_grades):
        student_id = fake.random_int(1, 30)
        subject_id = fake.random_int(1, 8)
        grade = fake.random_int(1, 10)
        date = fake.date_this_decade()
        cursor.execute('INSERT INTO grades (student_id, subject_id, grade, date) VALUES (?, ?, ?, ?)', (student_id, subject_id, grade, date))

# Заполнение таблиц случайными данными
fill_groups_table()
fill_teachers_table(3)
fill_subjects_table(8)
fill_students_table(50)
fill_grades_table(1000)

# Функции для выполнения запросов

def query_1():
    query_1_sql = read_sql_query_file('query_1.sql')
    # Найти 5 студентов с наибольшим средним баллом по всем предметам.
    cursor.execute(query_1_sql)
    result = cursor.fetchall()
    print("Студенты с наибольшим средним баллом:")
    for row in result:
        print(f"ID: {row[0]}, Имя: {row[1]}, Средний балл: {row[2]}")

def query_2():
    query_2_sql = read_sql_query_file('query_2.sql')
    # Найти студента с наивысшим средним баллом по определенному предмету.
    subject_id = int(input("Введите ID предмета: "))
    cursor.execute(query_2_sql, (subject_id,))
    result = cursor.fetchone()
    if result:
        print(f"Студент с наивысшим средним баллом по предмету (ID {subject_id}):")
        print(f"ID: {result[0]}, Имя: {result[1]}, Средний балл: {result[2]}")
    else:
        print(f"Студентов с оценками по предмету (ID {subject_id}) не найдено.")

def query_3():
    query_3_sql = read_sql_query_file('query_3.sql')
    # Найти средний балл в группах по определенному предмету.
    subject_id = int(input("Введите ID предмета: "))
    cursor.execute(query_3_sql, (subject_id,))
    result = cursor.fetchall()
    if result:
        print(f"Средний балл в группах по предмету (ID {subject_id}):")
        for row in result:
            print(f"Группа: {row[0]}, Средний балл: {row[1]}")
    else:
        print(f"Студентов с оценками по предмету (ID {subject_id}) не найдено.")

def query_4():
    query_4_sql = read_sql_query_file('query_4.sql')
    # Найти средний балл на потоке (по всей таблице оценок).
    cursor.execute(query_4_sql)
    result = cursor.fetchone()
    if result[0]:
        print(f"Средний балл на потоке: {result[0]}")
    else:
        print("Оценок в базе данных нет.")

def query_5():
    query_5_sql = read_sql_query_file('query_5.sql')
    # Найти какие курсы читает определенный преподаватель.
    teacher_id = int(input("Введите ID преподавателя: "))
    cursor.execute(query_5_sql, (teacher_id,))
    result = cursor.fetchall()
    if result:
        print(f"Преподаватель (ID {teacher_id}) читает следующие курсы:")
        for row in result:
            print(f"Предмет: {row[0]}")
    else:
        print(f"Преподавателя с ID {teacher_id} не существует или он не читает ни одного курса.")

def query_6():
    query_6_sql = read_sql_query_file('query_6.sql')
    # Найти список студентов в определенной группе.
    group_id = int(input("Введите ID группы: "))
    cursor.execute(query_6_sql, (group_id,))
    result = cursor.fetchall()
    if result:
        print(f"Список студентов в группе (ID {group_id}):")
        for row in result:
            print(f"ID: {row[0]}, Имя: {row[1]}")
    else:
        print(f"Группы с ID {group_id} не существует или в ней нет студентов.")

def query_7():
    query_7_sql = read_sql_query_file('query_7.sql')
    # Найти оценки студентов в отдельной группе по определенному предмету.
    group_id = int(input("Введите ID группы: "))
    subject_id = int(input("Введите ID предмета: "))
    cursor.execute(query_7_sql, (group_id, subject_id))
    result = cursor.fetchall()
    if result:
        print(f"Оценки студентов в группе (ID {group_id}) по предмету (ID {subject_id}):")
        for row in result:
            print(f"ID студента: {row[0]}, Имя студента: {row[1]}, Оценка: {row[2]}, Дата: {row[3]}")
    else:
        print(f"Оценок студентов в группе (ID {group_id}) по предмету (ID {subject_id}) не найдено.")

def query_8():
    query_8_sql = read_sql_query_file('query_8.sql')
    # Найти средний балл, который ставит определенный преподаватель по своим предметам.
    teacher_id = int(input("Введите ID преподавателя: "))
    cursor.execute(query_8_sql, (teacher_id,))
    result = cursor.fetchone()
    if result:
        print(f"Средний балл, который ставит преподаватель (ID {teacher_id}) по своим предметам: {result[2]}")
    else:
        print(f"Преподавателя с ID {teacher_id} не существует или он не преподает ни одного предмета.")

def query_9():
    query_9_sql = read_sql_query_file('query_9.sql')
    # Найти список курсов, которые посещает определенный студент.
    student_id = int(input("Введите ID студента: "))
    cursor.execute(query_9_sql, (student_id,))
    result = cursor.fetchall()
    if result:
        print(f"Студент (ID {student_id}) посещает следующие курсы:")
        for row in result:
            print(f"Предмет: {row[0]}")
    else:
        print(f"Студента с ID {student_id} не существует или он не посещает ни одного курса.")

def query_10():
    query_10_sql = read_sql_query_file('query_10.sql')
    # Список курсов, которые определенному студенту читает определенный преподаватель.
    student_id = int(input("Введите ID студента: "))
    teacher_id = int(input("Введите ID преподавателя: "))
    cursor.execute(query_10_sql, (student_id, teacher_id))
    result = cursor.fetchall()
    if result:
        print(f"Студент (ID {student_id}) посещает курсы, которые читает преподаватель (ID {teacher_id}):")
        for row in result:
            print(f"Предмет: {row[0]}")
    else:
        print(f"Студента с ID {student_id} или преподавателя с ID {teacher_id} не существует, либо студент не посещает курсы преподавателя.")

# Функция для отображения меню выбора
def show_menu():
    print("Выберите номер запроса для выполнения:")
    print("1. Найти 5 студентов с наибольшим средним баллом по всем предметам.")
    print("2. Найти студента с наивысшим средним баллом по определенному предмету.")
    print("3. Найти средний балл в группах по определенному предмету.")
    print("4. Найти средний балл на потоке (по всей таблице оценок).")
    print("5. Найти какие курсы читает определенный преподаватель.")
    print("6. Найти список студентов в определенной группе.")
    print("7. Найти оценки студентов в отдельной группе по определенному предмету.")
    print("8. Найти средний балл, который ставит определенный преподаватель по своим предметам.")
    print("9. Найти список курсов, которые посещает определенный студент.")
    print("10. Список курсов, которые определенному студенту читает определенный преподаватель.")
    print("0. Выход")

if __name__ == "__main__":
    while True:
        show_menu()
        choice = int(input("Введите номер запроса (0-10): "))

        if choice == 0:
            break
        elif choice == 1:
            query_1()
        elif choice == 2:
            query_2()
        elif choice == 3:
            query_3()
        elif choice == 4:
            query_4()
        elif choice == 5:
            query_5()
        elif choice == 6:
            query_6()
        elif choice == 7:
            query_7()
        elif choice == 8:
            query_8()
        elif choice == 9:
            query_9()
        elif choice == 10:
            query_10()
        else:
            print("Неверный выбор. Попробуйте снова.")

# Сохранение изменений и закрытие соединения
conn.commit()
conn.close()
