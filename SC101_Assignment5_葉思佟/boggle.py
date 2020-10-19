"""
File: boggle.py
Name:
----------------------------------------
TODO:
"""

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it

from tree import Trie

FILE = 'dictionary.txt'
BOARD_SIZE = 4


word_dict = []
board = []
found = []
neighbor_coordinates = [
	(-1, -1),  # Up left
	(-1, 0),   # Up
	(-1, 1),   # Up right
	(0, -1),   # Left
	(0, 1),    # Right
	(1, -1),   # Down left
	(1, 0),    # Down
	(1, 1),    # Down right
	]


def main():

	global board

	for i in range(BOARD_SIZE):
		letters = input(f'{i+1} row of letters: ')
		if len(letters) != 2*BOARD_SIZE or letters[2*i+1] != ' ':
			print('Illegal input')
			break

		letters = letters.replace(' ', '')
		board.append(letters.lower())

	read_dictionary()
	dictionary = Trie()         # Trie Class is imported from my self-made py document tree.py
	for word in word_dict:
		dictionary.add(word)

	for r in range(BOARD_SIZE):
		for c in range(BOARD_SIZE):
			letter = board[r][c]
			dfs(r, c, [], dictionary, '')

	print(f'There are {len(found)} words in total.')


def read_dictionary():
	"""
	This function reads file "dictionary.txt" stored in FILE
	and appends words in each line into a Python list
	"""
	global word_dict

	with open(FILE, 'r') as f:
		for line in f:
			word_list = line.split()
			for word in word_list:
				word_dict.append(word.strip())


def get_neighbors(r, c):
	"""
	Returns the neighbors for a given co-ordinates
	"""
	n = []
	for neigh in neighbor_coordinates:
		new_r = r + neigh[0]
		new_c = c + neigh[1]
		# Check if the  coordinate is outside the range
		if (new_r >= BOARD_SIZE) or (new_c >= BOARD_SIZE) or (new_r < 0) or (new_c < 0):
			continue
		n.append((new_r, new_c))
	return n


def dfs(r, c, visited, dictionary, now_word):

	global board, found

	"""Scan the graph using DFS"""
	if (r, c) in visited:
		return

	letter = board[r][c]
	visited.append((r, c))
	now_word += letter

	# We only want the word that has length >= 4
	# and we can use our trie to search if the word exists in the dictionary
	if len(now_word) >= 4 and dictionary.search(now_word):
		if now_word not in found:        # To make sure we do not print the same answer over 1 time
			found.append(now_word)
			print(f'Found "{now_word}"')

	# Find all neighbors from 8 different directions if they exist.
	neighbors = get_neighbors(r, c)

	# Do DFS for the new cell again and again (Recursion)
	for n in neighbors:
		dfs(n[0], n[1], visited[::], dictionary, now_word)


if __name__ == '__main__':
	main()
