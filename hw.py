def is_increasing(n):
  return n[0] < n[1] < n[2] < n[3]

def is_decreasing(n):
  return n[0] > n[1] > n[2] > n[3]

if __name__ == '__main__':
  nums = []
  for i in range(1000, 10000, 1):
    if is_increasing([int(j) for j in str(i)]) or is_decreasing([int(j) for j in str(i)]) :
      nums.append(i)
  print "Probability: ", len(nums)/9000.0