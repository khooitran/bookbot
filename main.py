import sys
from stats import get_num_words, get_num_characters, sort_num_characters

def get_book_text(path):
  with open(path) as f:
    return f.read()

def main():
  if len(sys.argv) != 2:
    raise Exception("Usage: python3 main.py <path_to_book>")
  else:
    char_list = ""
    for item in sort_num_characters(get_num_characters(get_book_text(sys.argv[1]))):
      if item["char"].isalpha():
        char_list += f"{item["char"]}: {item["num"]}\n"
    
    print(f'''
============ BOOKBOT ============
Analyzing book found at {sys.argv[1]}...
----------- Word Count ----------
Found {get_num_words(get_book_text(sys.argv[1]))} total words
--------- Character Count -------
{char_list}
============= END ===============
          ''')

try:
  main()
except Exception as e:
  print(e)
  sys.exit(1)
