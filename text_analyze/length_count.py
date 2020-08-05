import sys
from collections import Counter

path = sys.argv[1]

f = open(path, 'r', encoding='utf-8')
data = f.readlines()

def get_len(text):
	return len(text.strip().split())

lens = list(map(get_len, data))
total_num = len(lens)

counter = Counter(lens)
sorted_lens = sorted(list(counter))

for x in sorted_lens:
	y = counter[x]
	print('%d:\t%d\t%.2f%%' % (x, y, y / total_num * 100))

print('total: %d' % total_num)
print('average_len: %.2f' % (sum(lens) / total_num))
print('max_len: %d' % max(lens))
print('min_len: %d' % min(lens))
