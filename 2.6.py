print("2.6")
print("Hello, my name is Dat and these are my ship sizes")
sizes = [5, 7, 300, 90, 24, 50, 75]
print(sizes)
print("Now my biggest sheep has size 300 let's shear it")
sizes[2] = 8
print("After shearing, here is my flock")
print(sizes)
print("MONTH 1 :")
print("One month has passed, now here is my flock")
for i in range(len(sizes)):
    sizes[i] += 50
print(sizes)
print("Now my biggest sheep has size 140 let's shear it")
print("After shearing, here is my flock")
sizes[3] = 8
print(sizes)
print("MONTH 2 :")
print("One month has passed, now here is my flock")
for i in range(len(sizes)):
    sizes[i] += 50
print(sizes)
print("Now my biggest sheep has size 175 let's shear it")
print("After shearing, here is my flock")
sizes[6] = 8
print(sizes)
print("MONTH 3 :")
print("One month has passed, now here is my flock")
for i in range(len(sizes)):
    sizes[i] += 50
print(sizes)
print("My flock has size in total: ", sum(sizes))
a = sum(sizes) * 2
print("I would get",sum(sizes),"*2$ =",a,"$") 
