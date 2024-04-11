
class DiaryEntry:
    # Public Properties:
    #   title: a string
    #   contents: a string

    def __init__(self, title, contents):
        self.title = title
        self.contents = contents

    def count_words(self):
        return len(self.contents.split())

    def reading_time(self, wpm):
        pass

    def reading_chunk(self, wpm, minutes):
        
        pass
