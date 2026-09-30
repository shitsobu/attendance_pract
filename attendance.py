import csv
import os
from datetime import datetime

DATA_FILE = 'attendance.csv'

def init_csv():
    """Создает файл с заголовками, если его еще нет."""
    if not os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(['ID', 'Student Name', 'Login Time', 'Logout Time', 'Duration'])

def register_login(student_name):
    """Регистрирует вход студента."""
    init_csv()
    record_id = datetime.now().strftime("%Y%m%d%H%M%S")
    login_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    with open(DATA_FILE, 'a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow([record_id, student_name, login_time, '', ''])
    
    print(f"Вход {student_name} зарегистрирован в {login_time}")
    return record_id

def register_logout(record_id):
    """Регистрирует выход студента по ID записи."""
    rows = []
    found = False
    
    with open(DATA_FILE, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        for row in reader:
            if row[0] == record_id:
                row[3] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                found = True
            rows.append(row)
    
    if found:
        with open(DATA_FILE, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerows(rows)
        print(f"Выход зарегистрирован для записи {record_id}")
    else:
        print(f"Запись {record_id} не найдена")

def show_attendance():
    """Выводит все записи из файла."""
    if not os.path.exists(DATA_FILE):
        print("Файл с данными еще не создан.\n")
        return
        
    with open(DATA_FILE, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        print("-" * 60)
        for row in reader:
            print(" | ".join(row))
        print("-" * 60 + "\n")

if __name__ == "__main__":
    print("=== Система учета посещений ===")
    while True:
        print("1. Зарегистрировать вход")
        print("2. Зарегистрировать выход")
        print("3. Показать все записи")
        print("0. Выход")
        
        choice = input("Выберите действие: ")
        
        if choice == '1':
            name = input("Введите имя студента: ")
            register_login(name)
        elif choice == '2':
            record_id = input("Введите ID записи: ")
            register_logout(record_id)
        elif choice == '3':
            show_attendance()
        elif choice == '0':
            print("Завершение работы.")
            break
        else:
            print("Неверный выбор, попробуйте снова.\n")