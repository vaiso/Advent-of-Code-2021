path = './input.txt'

depths_file = open(path, 'r')

def strip_new_line(line):
  return int(line.strip('\n'))

depths = list(map(strip_new_line, depths_file.readlines()))

increases = 0

"""
Trying to solve the sliding window problem more efficiently

My intuition is that for two consecutive windows (e.g. A and B), 
they share values 200 and 208, so the only difference is between
value 199 and value 210. This means we can just compare those directly
instead of actually summing up the sliding window.

199  A      
200  A B    
208  A B
210    B

A1 == 199
A2 == 200 == B1
A3 == 208 == B2
      210 == B3
(B3 + B2 + B1) - (A3 + A2 + A1) == B3 - A1
"""
for i in range(3, len(depths)):
  prev = depths[i - 3]
  curr = depths[i]

  if curr > prev:
    increases += 1


print(increases)
