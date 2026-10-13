def add(a,b):
    return a + b

def sub(a,b):
    return a - b   

def print9():
    for i in range(1,10):
        for j in range(1,i+1):
            print(str(i) + "*" + str(j) + "=" + str(i*j), end="\t")
        print("\n")

print9()
print(add(1,2))