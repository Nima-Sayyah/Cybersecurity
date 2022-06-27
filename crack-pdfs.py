import pikepdf
from tqdm import tqdm

# load password list
passwords = [ line.strip() for line in open("wordlist.txt") ]
