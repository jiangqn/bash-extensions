import argparse
import random

parser = argparse.ArgumentParser()
parser.add_argument('--path', type=str)
parser.add_argument('--lines', type=int)
parser.add_argument('--max_len', type=int, default=10)

args = parser.parse_args()
f = open(args.path, 'w', encoding='utf-8')

for i in range(args.lines):
	length = random.randint(1, args.max_len)
	for j in range(length):
		f.write(str(random.randint(0, 9)) + ('\n' if j == length - 1 else ' '))

f.close()
