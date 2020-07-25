def xor_shift_period(word_size, x, a, b, c):
	max_int = 2**word_size
	if max_int > 2**16:
		result = [0] * 2**16
		print('WARNING: Resorting to heuristic method for large word_size. Accuracy not guaranteed')
	else:
		result = [0] * max_int
	for _ in range(2**word_size):
		x ^= ((x << a) % max_int)
		x ^= x >> b
		x ^= ((x << c) % max_int)
		result[x] = 1
	return result

def xor_shift_test_all(word_size):
	if word_size > 16:
		raise Exception('Word size too large')
	arbitrary_constant = 1 #cannot be zero & must be a number representable by the word size.
	all_answers = list()
	for a in range(word_size):
		for b in range(word_size):
			for c in range(word_size):
				result = xor_shift_period(word_size, arbitrary_constant, a, b, c)
				if check_result_bitfield(result):
					new_tuple = (a, b, c)
					all_answers.append(new_tuple)
	return all_answers

def xor_shift_validate_triple(a, b, c, word_size):
	arbitrary_constant = 1
	result = xor_shift_period(word_size, arbitrary_constant, a, b, c)
	return check_result_bitfield(result)

def check_result_bitfield(result):
	failed = 0
	for num in result:
		if num == 0:
			failed += 1
	return failed < 2

if __name__ == "__main__":
	results = xor_shift_test_all(16)
	print('There are ' + str(len(results)) + ' tuples')
	print(results)
