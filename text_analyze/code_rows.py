import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--path', type=str)
parser.add_argument('--suffixes', type=str)

def code_rows(path, suffixes):
	filenames = os.listdir(path)
	num = 0
	for filename in filenames:
		real_path = os.path.join(path, filename)
		if os.path.isdir(real_path):
			num += code_rows(real_path, suffixes)
		else:
			if filename.split('.')[-1] in suffixes:
				f = open(real_path, 'r', encoding='utf-8')
				count = 0
				for line in f.readlines():
					if len(line.strip()) > 0:
						count += 1
				num += count
	return num

args = parser.parse_args()
path = args.path
suffixes = args.suffixes.split('/')
rows = code_rows(path, suffixes)
print('code rows: %d' % rows)
