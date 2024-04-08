# Video alternative: https://youtu.be/qDWyR0XpJtQ&t=1295s

from lib.helpers import check_that_these_are_equal

# Now it's your turn.

# Note that the exercise will be (a little) less challenging
# than the example.

# Write a function that takes a list of words and returns a
# report of all the words that are longer than 10 characters
# but don't contain a hyphen. If those words are longer than
# 15 characters, then they should be shortened to 15
# characters and have an ellipsis (...) added to the end.

# For example, if the input is:
# [
#   'hello',
#   'nonbiological',
#   'Kay',
#   'this-is-a-long-word',
#   'antidisestablishmentarianism'
# ]
# then the output should be:
# "These words are quite long: nonbiological, antidisestablis..."

# @TASK: Complete this exercise.

print("")
print("Function: report_long_words")

def report_long_words(words):
  long_words = get_long_words(words)
  no_hyphen_long_words = remove_hyphens(long_words)
  shortened_long_words = shorten_long_words(no_hyphen_long_words)
  return f"These words are quite long: {', '.join(shortened_long_words)}"

def get_long_words(words):
  long_words = []
  for word in words:
    if len(word) > 10: 
      long_words.append(word)
  return long_words

def remove_hyphens(long_words):
  no_hyphen_long_words = []
  for word in long_words:
    if "-" not in word:
      no_hyphen_long_words.append(word)
  return no_hyphen_long_words

def shorten_long_words(no_hyphen_long_words):
  shortened_long_words = []
  for word in no_hyphen_long_words:
    if len(word) > 15:
      shortened_long_words.append(word[0:15] + "...")
    else: 
      shortened_long_words.append(word)
  return shortened_long_words

# check_that_these_are_equal(
#   get_long_words([
#     'hello',
#     'nonbiological',
#     'Kay',
#     'this-is-a-long-word',
#     'antidisestablishmentarianism'
#   ]),
#   ["nonbiological", "this-is-a-long-word", "antidisestablishmentarianism"]
# )

# check_that_these_are_equal(
#   remove_hyphens([
#     'nonbiological',
#     'this-is-a-long-word',
#     'antidisestablishmentarianism'
#   ]),
#   ["nonbiological", "antidisestablishmentarianism"]
# )

# check_that_these_are_equal(
#   shorten_long_words([
#     'nonbiological',
#     'antidisestablishmentarianism'
#   ]),
#   ["nonbiological", "antidisestablis..."]
# )

check_that_these_are_equal(
  report_long_words([
    'hello',
    'nonbiological',
    'Kay',
    'this-is-a-long-word',
    'antidisestablishmentarianism'
  ]),
  "These words are quite long: nonbiological, antidisestablis..."
)

check_that_these_are_equal(
  report_long_words([
    'cat',
    'dog',
    'rhinosaurus',
    'rhinosaurus-rex',
    'frog'
  ]),
  "These words are quite long: rhinosaurus"
)

check_that_these_are_equal(
  report_long_words([
    'cat'
  ]),
  "These words are quite long: "
)

# Once you're done, move on to 041_challenge_2_example.py
