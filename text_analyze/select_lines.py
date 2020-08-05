import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--src_path', type=str)
parser.add_argument('--start', type=int)
parser.add_argument('--end', type=int)
parser.add_argument('--trg_path', type=str)

args = parser.parse_args()

src_file = open(args.src_path, 'r', encoding='utf-8')
trg_file = open(args.trg_path, 'w', encoding='utf-8')
src = src_file.readlines()
n = len(src)
src_file.close()

assert 0 <= args.start and args.start < args.end and args.end <= n

for i in range(args.start, args.end):
	trg_file.write(src[i])
trg_file.close()
