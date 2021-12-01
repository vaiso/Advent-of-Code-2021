path = './input.txt'

depths_file = open(path, 'r')

def strip_new_line(line):
  return int(line.strip('\n'))

depths = list(map(strip_new_line, depths_file.readlines()))

increases = 0

"""
A very straightforward solution, just read each value and compare it 
to the value just before it.
"""
for i in range(1, len(depths)):
  prev = depths[i - 1]
  curr = depths[i]

  if curr > prev:
    increases += 1

print(increases)
