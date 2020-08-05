import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--src_path', type=str)
parser.add_argument('--min', type=int)
parser.add_argument('--max', type=int)
parser.add_argument('--trg_path', type=str, default=None)

args = parser.parse_args()
assert 0 <= args.min and args.min < args.max

src_file = open(args.src_path, 'r', encoding='utf-8')
src = src_file.readlines()
src_file.close()

trg_path = args.src_path if args.trg_path == None else args.trg_path
trg_file = open(trg_path, 'w', encoding='utf-8')

for line in src:
    length = len(line.strip().split())
    if length >= args.min and length <= args.max:
        trg_file.write(line)
trg_file.close()
