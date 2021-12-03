input_file = open('./input.txt', 'r')

inputs = [line.strip('\n') for line in input_file.readlines()]

"""
Intuition:

We want to keep track of whether there have been more 1s or 0s
in all of the inputs seen so far. One way we could do this is 
by having a map from index position in the binary numbers to the count
of each seen so far.

e.g. if we had the numbers:
11011
01101
11001
10001

Then we could have a map with five elements:
{
  index 0: (3 ones, 1 zero),
  index 1: (3 ones, 1 zero),
  index 2: (1 one, 3 zeroes),
  index 3: (1 one, 3 zeroes),
  index 4: (4 ones, 0 zeroes)
}

However, a lot of this information is redundant. Instead
of keeping a count of ones and zeroes, we could just keep a single
int, that we increment every time we see a 1, and decrement every
time we see a 0, which would end up giving us the difference between
the number of 1s and 0s.

We also don't need to map from the index to the count, since we 
can just have an array of size 5 and use the indexes of the array
itself as a 1:1 mapping.

So instead, we'd have this structure:
[2, 2, -1, -1, 4]
Where all of the negative numbers correspond to bit positions where
we saw more 0s than 1s, and positive numbers correspond to bit positions
where we saw more 1s than 0s.

And we can use this array to build the final answers:
gamma = 11001
epsilon = 00110

(note: epsilon could also be calculated by performing a bitwise NOT 
on gamma)
"""
totals = [0]*12

for input in inputs:
  for i, char in enumerate(input):
    if char == '0':
      totals[i] -= 1
    else:
      totals[i] += 1

gamma = ""
epsilon = ""

for count in totals:
  if count < 0:
    gamma += "0"
    epsilon += "1"
  else:
    gamma += "1"
    epsilon += "0"

print(int(gamma, 2) * int(epsilon, 2))

input_file.close()