dives_file = open('./input.txt', 'r')

dives = [line.strip('\n') for line in dives_file.readlines()]

x_pos = 0
depth = 0

for dive in dives:
  d = dive.split(' ')
  dir = d[0]
  amt = int(d[1])

  if dir == "forward":
    x_pos += amt
  elif dir == "down":
    depth += amt
  else:
    depth -= amt

print(x_pos * depth)