# {{PROBLEM}} Multi-Class Planned Design Recipe

## 1. Describe the Problem

Use object-oriented design and test-driven development, backed up by your debugging and pairing skills, to develop the following program.

As a user
So that I can record my experiences
I want to keep a regular diary
-record
-experience
-keep
-diary

As a user
So that I can reflect on my experiences
I want to read my past diary entries
-reflect
read past entries

As a user
So that I can reflect on my experiences in my busy day
I want to select diary entries to read based on how much time I have and my reading speed

As a user
So that I can keep track of my tasks
I want to keep a todo list along with my diary

As a user
So that I can keep track of my contacts
I want to see a list of all of the mobile phone numbers in all my diary entries_

## 2. Design the Class System

_Consider diagramming out the classes and their relationships. Take care to
focus on the details you see as important, not everything. The diagram below
uses asciiflow.com but you could also use excalidraw.com, draw.io, or miro.com_

```
# Nouns
Diary
Diary entries
Experiences
Time
Reading speed
Todo list
Tasks
Phone numbers
List of phone numbers

# Verbs
Record
Keep
Reflect
Read
Select
Keep
See a list
Mark complete
List complete
List incomplete
Add
┌────────────────────────────┐
│ MusicPlayer                │
│                            │
│ - tracks                   │
│ - add(track)               │
│ - search_by_title(keyword) │
│   => [tracks...]           │
└───────────┬────────────────┘
            │
            │ owns a list of
            ▼
┌─────────────────────────┐
│ Track(title, artist)    │
│                         │
│ - title                 │
│ - artist                │
│ - format()              │
│   => "TITLE by ARTIST"  │
└─────────────────────────┘
```

_Also design the interface of each class in more detail._

```python
class Diary:
    def add(self, diary_entry)
        pass

    def all(self):
        pass

class DiaryEntry():
    def __init__(self, title, contents)

class TaskList():
    def add(self, task)

    def all_incomplete(self):
        pass

    def all_complete(self):
        pass

class Task():
    def __init__(self, title):
        pass

    def mark_complete(self):
        pass

class PhoneNumberExtractor():
    def __init__(self, diary):
        pass

    def extract(self):
        pass

class ReadableEntryFinder():
     def __init__(self, diary):
        pass

    def extract(self, wpm, minutes):
        pass



#     def __init__(self):
#         pass # No code here yet

#     def add(self, track):
#         # Parameters:
#         #   track: an instance of Track
#         # Side-effects:
#         #   Adds the track to the tracks property of the self object
#         pass # No code here yet

#     def search_by_title(self, keyword):
#         # Parameters:
#         #   keyword: string
#         # Returns:
#         #   A list of the Track objects that have titles that include the keyword
#         pass # No code here yet


# class Track:
#     # User-facing properties:
#     #   title: string
#     #   artist: string

#     def __init__(self, title, artist):
#         # Parameters:
#         #   title: string
#         #   artist: string
#         # Side-effects:
#         #   Sets the title and artist properties
#         pass # No code here yet

#     def format(self):
#         # Returns:
#         #   A string of the form "TITLE by ARTIST"
#         pass # No code here yet

```

## 3. Create Examples as Integration Tests

_Create examples of the classes being used together in different situations and
combinations that reflect the ways in which the system will be used._

```python
# EXAMPLE

"""
# Given a library
# When we add two tracks
# We see those tracks reflected in the tracks list
# """
diary = Diary()
entry_1 = DiaryEntry("My Title 1", My Contents 1")
entry_2 = DiaryEntry("My Title 2", My Contents 2")
entry_3 = DiaryEntry("My Title 3", My Contents 3") 
diary.add(entry_1)
diary.add(entry_2)
diary.add(entry_3)
diary.all() == [entry_1, entry_2, entry_3]

```

## 4. Create Examples as Unit Tests

_Create examples, where appropriate, of the behaviour of each relevant class at
a more granular level of detail._

```python
# EXAMPLE

"""
Given a track with a title and an artist
We see the title reflected in the title property
"""
#Diary

diary = Diary()
diary.all() == []

#DiaryEntry

```

_Encode each example as a test. You can add to the above list as you go._

## 5. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green,
refactor to implement the behaviour._
