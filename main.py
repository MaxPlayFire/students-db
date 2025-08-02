import sqlite3

conn = sqlite3.connect("university.db")
cursor = conn.cursor()

def add_student():
    name = input("Ім'я студента: ")
    age = int(input("Вік студента: "))
    major = input("Спеціальність: ")
    cursor.execute("INSERT INTO students (name, age, major) VALUES (?, ?, ?)", (name,  age, major))
    conn.commit()
    print("✔ Студент доданий.")

def add_course():
    name = input("Назва курсу: ")
    instructor = input("Викладач: ")
    cursor.execute("INSERT INTO courses (course_name, instructor) VALUES (?, ?)", (name,  instructor))
    conn.commit()
    print("✔ Курс доданий.")

def register_student_to_course():
    student_id = int(input("ID студента: "))
    course_id = int(input("ID курсу: "))
    cursor.execute("INSERT INTO student_course (student_id, course_id) VALUES (?, ?)", (student_id,  course_id))
    conn.commit()
    print("✔ Студент зареєстрований на курс.")

def list_students():
    cursor.execute("SELECT * FROM students")
    for row in cursor.fetchall():
        print(row)

def list_courses():
    cursor.execute("SELECT * FROM courses")
    for row in cursor.fetchall():
        print(row)

def students_in_course():
    course_id = int(input("ID курсу"))
    cursor.execute("""
        SELECT students.id, students.name FROM students           
        JOIN student_course ON students.id = student_course.student_id
        WHERE student_course.course_id = ?
""", (course_id,))
    students = cursor.fetchall()
    print(f"Сттуденти, зареєстроваі на курс {course_id}:")
    for student in students:
        print(f"{student[0]} - {student[1]}")
    
def main_menu():
    while True:
        print("\n📘 Меню:")
        print("1. Додати студента")
        print("2. Додати курс")
        print("3. Зареєструвати студента на курс")
        print("4. Показати всіх студентів")
        print("5. Показати всі курси")
        print("6. Показати студентів для конкретного курсу")
        print("0. Вихід")

        choice = input("Обери опцію: ")
        if choice == "1":
            add_student()
        elif choice == "2":
            add_course()
        elif choice == "3":
            register_student_to_course()
        elif choice == "4":
            list_students()
        elif choice == "5":
            list_courses()
        elif choice == "6":
            students_in_course()
        elif choice == "0":
            print("👋 Вихід...")
            break
        else:
            print("❗️ Невідома команда.")

    conn.close()

# Запуск меню
if __name__ == "__main__":
    main_menu()
