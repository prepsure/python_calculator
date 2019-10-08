from input_handler import __input_eval as enput

def __enter_matrix():
  return [[float(i) for i in input("Enter Row of Matrix: ").split(",")] for j in range(int(input("Number of Rows: ")))]

def total_sum():
  m = __enter_matrix()
  r = 0
  for i in range(len(m)):
    for j in range(len(m[i])):
      r += m[i][j]
      m[i][j] = r
  print(m)

# works for 2 x 2 and 3 x 3 matrices
def det():
  print("row must be 2 or 3")
  m = __enter_matrix()
  r = 0
  if len(m) == 2:
    r = m[0][0]*m[1][1] - m[0][1]*m[1][0]
  elif len(m) == 3:
    r = m[0][0] * (m[1][1] * m[2][2] - m[1][2] * m[2][1]) - m[0][1] * (m[1][0] * m[2][2] - m[2][0] * m[1][2]) + m[0][2] * (m[1][0] * m[2][1] - m[1][1] * m[2][0])
  print(r)

def rref():
  m = __enter_matrix()

  if not m: return
  l = 0
  rC = len(m)
  cC = len(m[0])
  for r in range(rC):
      if l >= cC:
          return
      i = r
      while m[i][l] == 0:
          i += 1
          if i == rC:
              i = r
              l += 1
              if cC == l: return
      m[i], m[r] = m[r], m[i]
      lv = m[r][l]
      m[r] = [mrx / float(lv) for mrx in m[r]]
      for i in range(rC):
          if i != r:
              lv = m[i][l]
              m[i] = [ iv - lv*rv for rv,iv in zip(m[r], m[i])]
      l += 1
  
  for rw in m:
    print((",").join((str(rv) for rv in rw)))