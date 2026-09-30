import csv
import os
from datetime import datetime

DATA_FILE = 'attendance.csv'
LATE_THRESHOLD = "09:15"  # Время, после которого посещение считается опозданием

def init_csv():
    """Создает файл с заголовками, если его еще нет."""
    if not os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(['ID', 'Student Name', 'Login Time', 'Logout Time', 'Duration', 'Status'])

def is_late(login_time_str):
    """Определяет, является ли время входа опозданием.
    
    Args:
        login_time_str: строка времени в формате '%Y-%m-%d %H:%M:%S'
    
    Returns:
        'late' если время позже LATE_THRESHOLD, иначе 'present'
    """
    try:
        login_dt = datetime.strptime(login_time_str, "%Y-%m-%d %H:%M:%S")
        threshold_dt = datetime.strptime(LATE_THRESHOLD, "%H:%M").replace(
            year=login_dt.year, month=login_dt.month, day=login_dt.day
        )
        return 'late' if login_dt > threshold_dt else 'present'
    except ValueError:
        return 'present'

def register_login(student_name):
    """Регистрирует вход студента."""
    init_csv()
    record_id = datetime.now().strftime("%Y%m%d%H%M%S")
    login_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    status = is_late(login_time)
    
    with open(DATA_FILE, 'a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow([record_id, student_name, login_time, '', '', status])
    
    print(f"Вход {student_name} зарегистрирован в {login_time} (статус: {status})")
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

def calculate_duration(record_id):
    """Рассчитывает длительность посещения в минутах."""
    with open(DATA_FILE, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        for row in reader:
            if row[0] == record_id:
                if not row[3]:
                    print(f"Выход еще не зарегистрирован для записи {record_id}")
                    return None
                    
                login_time = datetime.strptime(row[2], "%Y-%m-%d %H:%M:%S")
                logout_time = datetime.strptime(row[3], "%Y-%m-%d %H:%M:%S")
                duration = int((logout_time - login_time).total_seconds() / 60)
                
                rows = []
                with open(DATA_FILE, 'r', encoding='utf-8') as f2:
                    reader2 = csv.reader(f2)
                    for r in reader2:
                        if r[0] == record_id:
                            r[4] = str(duration)
                        rows.append(r)
                
                with open(DATA_FILE, 'w', newline='', encoding='utf-8') as f2:
                    writer = csv.writer(f2)
                    writer.writerows(rows)
                
                print(f"Длительность посещения: {duration} минут")
                return duration
    
    print(f"Запись {record_id} не найдена")
    return None

def show_attendance():
    """Выводит все записи из файла."""
    if not os.path.exists(DATA_FILE):
        print("Файл с данными еще не создан.\n")
        return
        
    with open(DATA_FILE, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        print("-" * 80)
        for row in reader:
            print(" | ".join(row))
        print("-" * 80 + "\n")

if __name__ == "__main__":
    print("=== Система учета посещений ===")
    while True:
        print("1. Зарегистрировать вход")
        print("2. Зарегистрировать выход")
        print("3. Рассчитать длительность")
        print("4. Показать все записи")
        print("0. Выход")
        
        choice = input("Выберите действие: ")
        
        if choice == '1':
            name = input("Введите имя студента: ")
            register_login(name)
        elif choice == '2':
            record_id = input("Введите ID записи: ")
            register_logout(record_id)
        elif choice == '3':
            record_id = input("Введите ID записи: ")
            calculate_duration(record_id)
        elif choice == '4':
            show_attendance()
        elif choice == '0':
            print("Завершение работы.")
            break
        else:
            print("Неверный выбор, попробуйте снова.\n")