## Summary
As one of the cheapest PRNG class of algorithms in use, xorshift is invaluable for computationally constrained environments. It's algorithm, however, depends on having 3 special precomputed constants to have a period equal to ```2**word_size - 1```.

Having a collection of these values is useful. This script exists to exhaustively find and validate all triples for 16 bit and lower architectures with an algorithm of form:
```
x ^= x << a
x ^= x >> b
x ^= x << c
```
The source code can easily be modified to test less common variants of xorshift.


## Results

There are 24 valid triples for a 8 bit register:
[(1, 1, 2), (1, 1, 3), (1, 7, 3), (1, 7, 6), (1, 7, 7), (2, 1, 1), (2, 5, 5), (3, 1, 1), (3, 1, 5), (3, 5, 4), (3, 5, 5), (3, 5, 7), (3, 7, 1), (4, 5, 3), (5, 1, 3), (5, 3, 6), (5, 3, 7), (5, 5, 2), (5, 5, 3), (6, 3, 5), (6, 7, 1), (7, 3, 5), (7, 5, 3), (7, 7, 1)]

There are 60 valid triples for a 16 bit register:
[(1, 1, 14), (1, 1, 15), (1, 5, 2), (1, 7, 4), (1, 7, 11), (1, 11, 3), (1, 15, 6), (1, 15, 7), (2, 5, 1), (2, 5, 13), (2, 5, 15), (2, 7, 13), (2, 7, 15), (3, 1, 12), (3, 1, 15), (3, 5, 11), (3, 11, 1), (3, 11, 11), (3, 13, 9), (4, 3, 7), (4, 7, 1), (4, 11, 11), (5, 7, 14), (5, 9, 8), (5, 11, 6), (5, 11, 11), (6, 7, 13), (6, 11, 5), (6, 15, 1), (7, 1, 11), (7, 3, 4), (7, 9, 8), (7, 9, 13), (7, 15, 1), (8, 9, 5), (8, 9, 7), (9, 7, 13), (9, 13, 3), (11, 1, 7), (11, 3, 13), (11, 5, 3), (11, 7, 1), (11, 11, 3), (11, 11, 4), (11, 11, 5), (12, 1, 3), (12, 3, 13), (13, 3, 11), (13, 3, 12), (13, 5, 2), (13, 7, 2), (13, 7, 6), (13, 7, 9), (13, 9, 7), (14, 1, 1), (14, 7, 5), (15, 1, 1), (15, 1, 3), (15, 5, 2), (15, 7, 2)]

## Setup
To run the test, simply import ```xor_shift_test_all``` . ```xor_shift_test_all``` will run with a word size of 16 bits or less. Sizes greater than 16 are impractical with this script. See *Xorshift RNGs* by Marsaglia for more information about xorshift and generating high quality RNG.

