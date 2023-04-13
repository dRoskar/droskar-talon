os: windows
mode: dictation
-
left <number_small> (word | words):
    edit.word_left()
    repeat(number_small - 1)
right <number_small> (word | words):
    edit.word_right()
    repeat(number_small - 1)