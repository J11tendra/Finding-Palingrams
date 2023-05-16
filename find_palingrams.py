#Importing the module to load list:
from opening_file import open_file

#Loading the list of words:
word_list = open_file('D:/Python_work/text_files/All_Words.txt')

#Function to find word-pairs Palingrams:
def find_palingrams():
	'''find word-pairs palingrams and appending to list'''
	palingrams_list = []
	words = set(word_list)
	for word in words:
		word_len = len(word)
		reverse_word = word[::-1]
		if word_len > 1:
			for x in range(word_len):
				if word[x:] == reverse_word[:word_len-1] and reverse_word[word_len-1:] in words:
				    palingrams_list.append((word, reverse_word[word_len-1:]))
				elif word[:x] == reverse_word[word_len-1:] and reverse_word[:word_len-1:] in words:
				    palingrams_list.append((reverse_word[:word_len-1], word))
	return palingrams_list

palingram = find_palingrams()
sorted_palingram = sorted(palingram)
print(sorted_palingram)
print(f'\n\n\nWe have found {len(sorted_palingram)} palingrams word-pairs in the wordlist.\n\n\n')