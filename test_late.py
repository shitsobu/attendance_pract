from attendance import is_late, LATE_THRESHOLD

def test_is_late():
    """Тест функции определения опоздания."""
    # Раннее время — не опоздание
    assert is_late("2026-09-30 09:00:00") == 'present'
    
    # Ровно порог — не опоздание
    assert is_late("2026-09-30 09:15:00") == 'present'
    
    # После порога — опоздание
    assert is_late("2026-09-30 09:16:00") == 'late'
    assert is_late("2026-09-30 10:30:00") == 'late'
    
    print(f"Все тесты пройдены! Порог опоздания: {LATE_THRESHOLD}")

if __name__ == "__main__":
    test_is_late()