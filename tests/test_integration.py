from lib.diary import Diary
from lib.diary_entry import DiaryEntry

"""
Given I add two entries
I see them back in the list
"""

def test_adds_and_lists_diary_entries():
    diary = Diary()
    entry_1 = DiaryEntry("My title 1", "My Contents 1")
    entry_2 = DiaryEntry("My title 2", "My Contents 2")
    diary.add(entry_1)
    diary.add(entry_2)
    assert diary.all() == [entry_1, entry_2]

"""
Given I add two diary entries
And I call #count_words
I get the sum of all words in the diary entries
"""
def test_count_words_returns_countof_all_words_in_all_entry_contents():
    diary = Diary()
    entry_1 = DiaryEntry("My title 1", "One two")
    entry_2 = DiaryEntry("My title 2", "Three Four Five")
    diary.add(entry_1)
    diary.add(entry_2)
    assert diary.count_words() == 5

"""
Given I add two diary entries with a total length of 5
And I call #reading_time with wpm of 2
Then the total reading time should be 3
"""

def test_reading_time_returns_time_to_read_all_entries():
    diary = Diary()
    entry_1 = DiaryEntry("My title 1", "One two")
    entry_2 = DiaryEntry("My title 2", "Three Four Five")
    diary.add(entry_1)
    diary.add(entry_2)
    assert diary.reading_time(2) == 3

def test_find_best_entry_for_reading_time_returns_entry_that_fits_in_time():
    diary = Diary()
    entry_1 = DiaryEntry("My title 1", "One two three")
    entry_2 = DiaryEntry("My title 2", "One two Three Four Five six seven")
    diary.add(entry_1)
    diary.add(entry_2)
    assert diary.find_best_entry_for_reading_time(2, 3) == entry_1

def test_find_best_entry_for_reading_time_returns_entry_that_fits_in_time():
    diary = Diary()
    entry_1 = DiaryEntry("My title 1", "One two three")
    diary.add(entry_1)
    assert diary.find_best_entry_for_reading_time(2, 3) == entry_1

def test_find_best_entry_for_reading_time_returns_none_if_single_entry_doesnt_fit():
    diary = Diary()
    entry_1 = DiaryEntry("My title 1", "One two three four five six seven")
    diary.add(entry_1)
    assert diary.find_best_entry_for_reading_time(2, 3) == None

# def test_find_entries_for_reading_time_returns_the_longest_readable():
#     diary = Diary()
#     entry_1 = DiaryEntry("My title 1", "One two three")
#     entry_2 = DiaryEntry("My title 2", "One two Three Four Five six seven")
#     diary.add(entry_1)
#     diary.add(entry_2)
#     assert diary.find_best_entry_for_reading_time(2, 4) == entry_2