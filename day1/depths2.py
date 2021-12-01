path = './input.txt'

depths_file = open(path, 'r')

def strip_new_line(line):
  return int(line.strip('\n'))

depths = list(map(strip_new_line, depths_file.readlines()))

increases = 0

for i in range(3, len(depths)):
  prev = depths[i - 3]
  curr = depths[i]

  if curr > prev:
    increases += 1


print(increases)
