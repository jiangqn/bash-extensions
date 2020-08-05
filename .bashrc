split_apart_by_tab() {
	src_path=$1
	trg1_path=$2
	trg2_path=$3
	python /home/data_ti4_c/jiangqn/text_analyze/split_apart_by_tab.py $src_path $trg1_path $trg2_path
}

length_count() {
	path=$1
	python /home/data_ti4_c/jiangqn/text_analyze/length_count.py $path
}

length_filter() {
	args_num=$#
	if [ $args_num == 3 ]; then
		src_path=$1
		min=$2
		max=$3
		python /home/data_ti4_c/jiangqn/text_analyze/length_filter.py --src_path $src_path --min $min --max $max
	elif [ $args_num == 4 ]; then
		src_path=$1
		min=$2
		max=$3
		trg_path=$4
		python /home/data_ti4_c/jiangqn/text_analyze/length_filter.py --src_path $src_path --min $min --max $max --trg_path $trg_path
	else
		echo "arguments num error"
	fi
}

select_lines() {
	src_path=$1
	start=$2
	end=$3
	trg_path=$4
	python /home/data_ti4_c/jiangqn/text_analyze/select_lines.py --src_path $src_path --start $start --end $end --trg_path $trg_path
}

random_text() {
	args_num=$#
	if [ $args_num == 2 ]; then
		path=$1
		lines=$2
		python /home/data_ti4_c/jiangqn/text_analyze/random_text.py --path $path --lines $lines
	elif [ $args_num == 3 ]; then
		path=$1
		lines=$2
		max_len=$3
		python /home/data_ti4_c/jiangqn/text_analyze/random_text.py --path $path --lines $lines --max_len $max_len
	else
		echo "arguments num error"
	fi
}

code_rows() {
	path=$1
	suffixes=$2
	python /home/data_ti4_c/jiangqn/text_analyze/code_rows.py --path $path --suffixes $suffixes
}
