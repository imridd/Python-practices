def get_word(word_type):
  return input(f"Enter a {word_type}: ")

def mad_libs():
  noun_1 = get_word("noun")
  adjective_1 = get_word("adjective")
  verb_1 = get_word("verb (ing form)")
  adverb = get_word("adverb")
  noun_2 = get_word("noun")
  adjective_2 = get_word("adjective")
  verb_2 = get_word("verb")

  
  story = f"The {adjective_1} {noun_1} was {verb_1} {adverb} when it encountered a {adjective_2} {noun_2}.  They {verb_2} happily ever after."

  print(story)

if __name__ == "__main__":
  mad_libs()
