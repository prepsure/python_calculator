from math import sqrt

def form(a,b,c,x):
  return a*x**2+b*x+c;

def discr(a,b,c):
  return b**2 - 4*a*c

def quad():
  print("ax**2+bx+c")
  a = float(input("a="))
  b = float(input("b="))
  c = float(input("c="))
  delta = discr(a,b,c)
  if delta == 0:
    return -b/(2*a)
  elif delta > 0:
    return (-b+sqrt(delta))/(2*a), (-b-sqrt(delta))/(2*a)
  else:
    return complex(-b/(2*a),(sqrt(delta*-1))/(2*a)),complex(-b/(2*a),-(sqrt(delta*-1))/(2*a))