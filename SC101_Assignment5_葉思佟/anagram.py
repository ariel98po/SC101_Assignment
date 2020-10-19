"""
File: anagram.py
Name:
----------------------------------
This program recursively finds all the anagram(s)
for the word input by user and terminates when the
input string matches the EXIT constant defined
at line 19

If you correctly implement this program, you should see the
number of anagrams for each word listed below:
    * arm -> 3 anagrams
    * contains -> 5 anagrams
    * stop -> 6 anagrams
    * tesla -> 10 anagrams
    * spear -> 12 anagrams
"""

# Constants
FILE = 'dictionary.txt'       # This is the filename of an English dictionary
EXIT = '-1'                   # Controls when to stop the loop
word_dict = []
# current_str = ''
anagram_list = []

def main():

    global anagram_list

    print('Welcome to stanCode "Anagram Generator" (or -1 to quit)')

    read_dictionary()

    while True:
        s = input('Find anagram for: ')
        if s == EXIT:
            break
        print("Searching...")
        find_anagrams(s)
        print(f'{len(anagram_list)} anagrams: {anagram_list}')
        anagram_list = []


def read_dictionary():
    global word_dict

    with open(FILE, 'r') as f:
        for line in f:
            word_list = line.split()
            for word in word_list:
                word_dict.append(word.strip())


def find_anagrams(s):
    """
    :param s: The vocabulary we entered
    :return:
    """
    find_anagrams_helper(s, len(s), '')


def find_anagrams_helper(s, target_length, current_str):

    global anagram_list

    if len(current_str) == target_length:
        word = ''
        for i in current_str:
            word += s[int(i)]

        if word in word_dict and word not in anagram_list:
            print(f'Found: {word}')
            print("Searching...")
            anagram_list.append(word)

    else:
        if has_prefix(current_str, s):
            for i in range(len(s)):

                if str(i) not in current_str:
                    # Choose
                    current_str = current_str + str(i)
                    # Explore
                    find_anagrams_helper(s, target_length, current_str)
                    # Un-choose
                    current_str = current_str[:len(current_str)-1]





def has_prefix(sub_s, s):
    """
    :param sub_s:
    :return: True or False
    """

    global word_dict

    index_word = ''

    for i in sub_s:
        index_word += s[int(i)]

    for word in word_dict:
        if word.startswith(index_word):
            return True

    return False









if __name__ == '__main__':
    main()
