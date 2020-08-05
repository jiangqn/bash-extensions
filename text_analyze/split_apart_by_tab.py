import sys

src_path = sys.argv[1]
trg1_path = sys.argv[2]
trg2_path = sys.argv[3]

src_file = open(src_path, 'r', encoding='utf-8')
trg1_file = open(trg1_path, 'w', encoding='utf-8')
trg2_file = open(trg2_path, 'w', encoding='utf-8')

for line in src_file.readlines():
	line = line.strip().split('\t')
	assert len(line) == 2
	trg1_file.write(line[0] + '\n')
	trg2_file.write(line[1] + '\n')

src_file.close()
trg1_file.close()
trg2_file.close()
