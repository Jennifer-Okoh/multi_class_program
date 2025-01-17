from lib.diary import Diary
import pytest
"""
Initially, has an empty list of entries
"""
def test_initially_has_empty_list_of_entries():
    diary = Diary()
    assert diary.all() == []

"""
Initially, word count is zero
"""

def test_initially_initially_word_count_zero():
    diary = Diary()
    assert diary.count_words() == 0

"""
Initially, #reading_time should raise an error
"""

def test_initially_reading_time_raises_error():
    diary = Diary()
    with pytest.raises(Exception) as err:
        diary.reading_time(2)
    assert str(err.value) == "No entries added yet"
