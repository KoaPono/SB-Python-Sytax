def print_upper_words(words):
    """Prints out each word on a separate line in all capital letters.

    For example:
      print_upper_words(["test", "one", "hello"])

    Should print:
      TEST
      ONE
      HELLO
    """
    for word in words:
        print(word.upper())

def print_upper_words_that_begin_with_e(words):
    """Prints out each word beginning with e on a separate line in all capital letters.

    For example:
      print_upper_words_that_begin_with_e(["test", "elf", "hello"])

    Should print:
      ELF
    """
    for word in words:
        if word.startswith("e") or word.startswith("E"):
            print(word.upper())

def print_upper_words_that_begin_with(words, starting_letters):
    """Prints out each word beginning with the given letter on a separate line in all capital letters.

      For example:
        print_upper_words_that_begin_with(["test", "elf", "hello"], {"e", "h"})

      Should print:
        ELF
        HELLO
    """

    for word in words:
        for letter in starting_letters:
            if word.startswith(letter):
                print(word.upper())
                break