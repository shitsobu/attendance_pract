from attendance import is_late, LATE_MINUTES, LESSON_START

def test_is_late():
    """Тест функции определения опоздания."""
    # До начала занятия — не опоздание
    assert is_late("2026-09-30 08:55:00") == 'present'
    
    # Ровно начало занятия — не опоздание
    assert is_late("2026-09-30 09:00:00") == 'present'
    
    # В пределах LATE_MINUTES — не опоздание
    assert is_late("2026-09-30 09:09:00") == 'present'
    assert is_late("2026-09-30 09:10:00") == 'present'
    
    # Тест точной границы: 09:10:00 — ещё не опоздание, 09:10:01 — уже опоздание
    assert is_late("2026-09-30 09:10:00") == 'present'  # граница снизу
    assert is_late("2026-09-30 09:10:01") == 'late'    # граница сверху
    
    # После LATE_MINUTES — опоздание
    assert is_late("2026-09-30 09:11:00") == 'late'
    assert is_late("2026-09-30 10:30:00") == 'late'
    
    print(f"Все тесты пройдены! Допустимое опоздание: {LATE_MINUTES} минут после {LESSON_START}")

if __name__ == "__main__":
    test_is_late()