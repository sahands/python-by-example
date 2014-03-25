#!/usr/bin/env python
#
# Unpacking iterables.

# Any iterables can be unpacked using an assignment statement.
# Rule:
#   Except for a single variable, variables to unpack values into should be equal to the number of
#   elements in the iterable. (It is slightly different in Python 3 using the star expression)
#
#
# A small testing utility
def test_equal(expected, value, msg=None):
    if expected == value:
        print('\033[92mSUCCESS: %s\033[0m' % msg or 'SUCCESS: {} equals expected value {}'.format(value, expected))
    else:
        print('\033[91mFAILED: Expected {0} to have a value of {1}. Got {0} instead\033[0m'.format(value, expected))


print("Unpacking Iterables.\n===================\n\n")

# Single assignment to tuple
a = 1, 2
print('a = 1, 2')
test_equal((1,2), a, '`a` has value (1, 2)')


print('\n\n')

a, b, c = 1, 2, 3

print 'a, b, c = 1, 2, 3'
test_equal((1,2,3), (a,b,c))
test_equal(1, a, '`a` has a value of 1')
test_equal(2, b, '`b` has a value of 2')
test_equal(3, c, '`c` has a value of 3')
# Parenthesis are optional on both sides in which case a tuple is assumed.
# Most of the time this is not something to worry about during unpacking as the data type
# does not affect the speed or order of distribution.
# Be careful about sets (unordered sets) as they don't have a fixed order.
#
# Unpacking dictionaries only unpacks the keys. But the order is non-deterministic.
print('\nUnpacking dictionaries unpacks only the keys')
print('\t(NOTE: Just like unpacking sets the order cannot be trusted.)\n')
a, b = { 'key1': 'value1', 'key2': 'value2' }
print("a, b = { 'key1': 'value1', 'key2': 'value2'  }")

test_equal('key1', a, '`a` has value key1') # could report an error
test_equal('key2', b, '`b` has value key2') # could report an error

print('\n\nUnpacking sets\n===')
# Unpacking sets.
#
# Elements of a set are not ordered so various unpackings would assign different
# values at different times. Don't trust what you see when you unpack like this:
a, b, c, d = set([1, 2, 3, 4])
print('a, b, c, d = set([1, 2, 3, 4])')
test_equal(1, a, '`a` has a value of 1')
test_equal(2, b, '`b` has a value of 2')
test_equal(3, c, '`c` has a value of 3')
test_equal(4, d, '`d` has a value of 4')


print('\n\nSwapping values via unpacking\n===')
# Swapping values
#
# In most programming languages, swapping the values of 2 variables requires a
# third, usually called `temp` (tmp, or variations of it).
# In Python, swapping the values of 2 (and as such any number of) variables is
# as straight forward as:

a, b = 1, 2
print('a, b = 1, 2')
test_equal(1, a, '`a` has value of 1')
test_equal(2, b, '`b` has value of 2')

print('\nSwapping a, b.')
a, b = b, a
print('a, b = b, a')
test_equal(2, a, '`a` has value of 2')
test_equal(1, b, '`b` has value of 1')
