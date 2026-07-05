import pytest
# מייבאים את הפונקציות שרוצים לבדוק מתוך קובץ האפליקציה app.py
# (נניח שיש לך שם פונקציה בשם add_numbers או פונקציה שמחזירה סטטוס)
from app import main_logic # שנה את השם לפונקציה אמיתית שקיימת אצלך ב-app.py

def test_success_case():
    """בדיקה של מקרה תקין"""
    result = main_logic(2, 3)
    assert result == 5  # assert בודק שהתוצאה שחזרה שווה למה שציפינו

def test_invalid_input():
    """בדיקה שהקוד מתמודד נכון עם קלט לא תקין או זורק שגיאה מתאימה"""
    with pytest.raises(TypeError):
        main_logic("string", 3)
