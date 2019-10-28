temp = input("What is your temperature? ")
temp = float(temp)

startType = input("Type 1 for F, 2 for C, or 3 for K, for what it is currently in. ")
startType = int(startType)

endType = input("Type 1 for F, 2 for C, or 3 for K, for what you want to convert to. ")
endType = int(endType)

answer = 0

if (startType == endType) :
  print ("bruh you stupid")

if (startType == 1 and endType == 2) :
  answer = (((temp - 32) * 5) / 9)

if (startType == 1 and endType == 3) :
  answer = (((temp - 32) * 5) / 9 + 273.15)

if (startType == 2 and endType == 1) :
  answer = (((temp * 9) / 5) + 32)

if (startType == 2 and endType == 3) :
  answer = (temp + 273.15)

if (startType == 3 and endType == 1) :
  answer = ((((temp - 273.15) * 9) / 5) + 32)

if (startType == 3 and endType == 2) :
  answer = (temp - 273.15)


print (answer)