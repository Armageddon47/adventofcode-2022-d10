
coordinates = []
arr_2d = [["#" for j in range(40)] for i in range(6)]

count = 0
x = 1
total = 0
J = 0
K = 0
test = 0
with open("ww.txt") as f:
    for line in f:
        coordinates.append(line.strip())
        
def Call(v=None):
    global J,K,total,x,count,test
    if J > 39:
        J=0
        K+=1

    if x not in [J, J-1 , J+1]:
        arr_2d[K][J] = "."

    J += 1
    test += 1
    count += 1
    if count in [20, 60, 100, 140, 180, 220]:
        print("count is " ,count)
        print(x)
        total += count*x

    if v is not None:
        Call()
        
        x += v

    
           
for line in coordinates:
    if(line[0] == "a"):
        size = int(line[line.find(" "):])

        Call(size)
    
    elif(line[0] == "n"):
        Call()
        
        

print(total)
print(count,"total count")    

#### End of part 1

# Print the 2D array
for i in range(6):
    for j in range(40):
        print(arr_2d[i][j], end=' ')
    print() # To move to the next line after each row
print(test,"test")
