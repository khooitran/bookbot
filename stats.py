def get_num_words(string):
  words_list = string.split()
  return len(words_list)

def get_num_characters(string):
  string = string.lower()
  char_dict = {}
  for c in string:
    if c in char_dict:
      char_dict[c] += 1
    elif c != " ":
      char_dict[c] = 1
  return char_dict

def sort_on(dict):
  return dict["num"]

def sort_num_characters(dict):
  characters_list = []
  for key, value in dict.items():
    characters_list.append({"char": key, "num": value})
  characters_list.sort(reverse=True, key=sort_on)
  return characters_list

