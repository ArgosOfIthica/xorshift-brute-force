import math
import sys

def xor_shift_period(word_size, x, a, b, c):
	max_int = 2**word_size
	result = [0] * max_int
	for _ in range(max_int):
		x ^= ((x << a) % max_int)
		x ^= x >> b
		x ^= ((x << c) % max_int)
		if result[x] != 0:
			return result
		result[x] = 1
	return result

def xor_shift_test_all(word_size):
	arbitrary_constant = 1 #cannot be zero & must be a number representable by the word size.
	all_answers = list()
	for a in range(1,word_size):
		for b in range(1,word_size):
			for c in range(a,word_size): # a and c are symmetric
				result = xor_shift_period(word_size, arbitrary_constant, a, b, c)
				if check_result_bitfield(result):
					new_triple = (a, b, c)
					all_answers.append(new_triple)
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
			if failed > 1:
				return False
	return True

if __name__ == "__main__":
	results = xor_shift_test_all(int(sys.argv[1]))
	print('There are ' + str(len(results)) + ' unique nontrivial triples. Trivial triples include mirrored triples, where the mirror of a triple (a,b,c) is triple (c,b,a)')
	print(results)
