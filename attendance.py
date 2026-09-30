import csv
import os
from datetime import datetime

DATA_FILE = 'attendance.csv'

def init_csv():
    """Создает файл с заголовками, если его еще нет."""
    if not os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(['ID', 'Student Name', 'Date', 'Status'])

def add_attendance(student_name, status):
    """Добавляет новую запись о посещении."""
    init_csv()
    record_id = datetime.now().strftime("%Y%m%d%H%M%S")
    date = datetime.now().strftime("%Y-%m-%d %H:%M")
    
    with open(DATA_FILE, 'a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow([record_id, student_name, date, status])
    print(f"Запись для {student_name} успешно добавлена.\n")

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
        print("1. Добавить посещение")
        print("2. Показать все записи")
        print("0. Выход")
        
        choice = input("Выберите действие: ")
        
        if choice == '1':
            name = input("Введите имя студента: ")
            status = input("Введите статус (present/absent/late): ")
            add_attendance(name, status)
        elif choice == '2':
            show_attendance()
        elif choice == '0':
            print("Завершение работы.")
            break
        else:
            print("Неверный выбор, попробуйте снова.\n")