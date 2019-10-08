def isprime(n):
  if type(n)!=int or n<2:
    return False
  for i in range(2,int(n**0.5)+1):
    if n%i==0:
      return False
  return True

def divisors(n):
  if type(n)!=int or n<1:
    return None
  if n==1:
    return [1]
  l=[1]
  for i in range(2,int(n**0.5)+1):
    if n%i==0:
      l.append(i)
      if n//i!=i:
        l.append(n//i)
  return sorted(l)+[n]

def gcd(a,b):
  if type(a+b)!=int:
    return None
  while b!=0:
    a,b=b,a%b
  return abs(a)

def lcm(a,b):
  if type(a+b)!=int:
    return None
  return a*b//gcd(a,b)

def quotient(a,b):
  if type(a+b)!=int:
    return None
  liste=[]
  while b!=0:
    liste.append(a//b)
    a,b=b,a%b
  return liste

def bezout(a,b):
  if gcd(a,b)!=1:
    return None
  u0, v0, u1, v1 = 1, 0, 0, 1
  while b:
    a, (q, b) = b, divmod(a, b)
    u0, v0, u1, v1 = u1, v1, u0 - q * u1, v0 - q * v1
  return u0, v0

def diophant(a,b,c):
  d=gcd(a,b)
  if gcd(d,c)!=d:
    return None
  if abs(a)<abs(b):
    a,b=b,a
  e,f,g=a//d,b//d,c//d
  u,v=bezout(e,f)
  print("(",u*g,"+",f,"k)*",a,"+","(",v*g,"-",e,"k)*",b,"=",c)
