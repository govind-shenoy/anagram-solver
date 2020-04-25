# simple program to find the country names from anagrams

from collections import Counter
from names import countries
import sys
from time import time

# if (len(sys.argv) < 2):
# 	print("Please enter anagram as command line argument when running the script. \nUSAGE : python anagram_countries.py anagram")
# 	sys.exit(1)

# anagram = sys.argv[1].strip().lower().replace(" ","")
while (1):
	f = 0
	anagram = input("anagram: ").strip().lower().replace(" ","")
	letters_count = Counter(anagram)
	country = ""
	t0 = time()
	for item in countries:
		name = item.replace(" ","").lower()
		if len(anagram) == len(name):
			if not (set(name) - set(anagram)):
				for letter, count in Counter(name).items():
					if count != letters_count[letter]:
						f = 1
						break
				if not f:
					country = item

	if country:
		print("Country: " + country.strip('    '))
		print("t: ",round(time()-t0,5),"seconds")
	else:
		print("Not found")
	
	again = input("\nContinue? [Y/N]: ")
	if (again == 'y' or again == 'Y'):
		continue
	else: sys.exit(0)