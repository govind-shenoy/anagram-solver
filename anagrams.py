# simple program to crack anagrams
from collections import Counter
import sys
from time import time

with open('words.txt', 'r') as f:
    dictionary = f.read()

# Remove white spaces, apostrophes and hyphens 
dictionary = [word.replace(" ","").replace("'","").replace("-","").lower() for word in dictionary.split('\n')]

def solve(anagram):
		letters_count = Counter(anagram)
		solution = set()
		t0 = time() # to find the time for each solution
		for word in dictionary:
			f = 0 # if f is 1, the check failed 
			if len(anagram) == len(word):
				if not (set(word) - set(anagram)):
					for letter, count in Counter(word).items():
						if count != letters_count[letter]:
							f = 1 
							break
					if not f:
						solution.add(word)	# word added to solution set							
		if solution:
			print("Soluiton: " , solution)
			print("t: ",round(time()-t0,5),"seconds")
		else:
			print("Not found")
			
if __name__ == '__main__':
	while(1):
		anagram = input("anagram: ").strip().lower().replace(" ","")
		solve(anagram)
		repeat = input("\nContinue? [Y/N]: ")
		if (repeat == 'y' or repeat == 'Y'):
			continue
		else: sys.exit(0)