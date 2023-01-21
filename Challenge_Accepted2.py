# Digital Evolution of a Diamond
# Created by Anietie Essien
def diamond_creation(n,m,o):
    for i in range(27):
        a= [n]*27
        b= (len(a)//2)
        if i >= 0 and i < 14:
            a[b-i] = a[b+i] = o
            a[(b-i)+1:b+i] = m*len(a[(b-i)+1:b+i])
        else:
            a[i-b] = a[b-i-1] = o
            a[i-b+1:b-i-1] = m*len(a[i-b+1:b-i-1])
        print("".join(a))

diamond_creation("–","–","o")
print("\n\n")
diamond_creation("o","o","–")
print("\n\n")

diamond_creation("\u25a0","\u25a0","–")
print("\n\n")
diamond_creation("\u25a1","\u25a1","o")
print("\n\n")

diamond_creation("\u25a0","\u25a1","★")    
print("\n\n")
diamond_creation("\u25a1","\u25a0","★")
print("\n\n")

def diamond_within(n,m,o):
    z = -1
    for i in range(27):
        a= [n]*27
        b= (len(a)//2)
        if i >= 0 and i < 14:
            a[b-i] = a[b+i] = o
            a[(b-i)+1:b+i] = m*len(a[(b-i)+1:b+i])
            if i >= 8 :
                z += 1
                a[b-z]=a[b+z]= o
                a[b-z+1:b+z] = n*len(a[b-z+1:b+z])
        else:
            a[i-b] = a[b-i-1] = o
            a[i-b+1:b-i-1] = m*len(a[i-b+1:b-i-1])
            if i < 19 :
                      z -= 1
                      a[b-z]=a[b+z]= o
                      a[b-z+1:b+z] = n*len(a[b-z+1:b+z])
        print("".join(a))
        
diamond_within("\u25a0","\u25a1","★")
print("\n\n")
diamond_within("\u25a1","\u25a0","★")
print("\n\n")        
diamond_within("\u2606","\u25a1","\u25a0")
print("\n\n")
diamond_within("★","\u25a0","\u25a1")
print("\n\n")

def little_mouth(n,m,o):
    z = -1
    for i in range(27):
        a= [n]*27
        b= (len(a)//2)
        if i >= 0 and i < 14:
            a[b-i] = a[b+i] = o
            a[(b-i)+1:b+i] = m*len(a[(b-i)+1:b+i])
            if i >= 8 :
                z += 1
                a[b-z]=a[b+z]= o
                a[b-z+1:b+z] = n
        else:
            a[i-b] = a[b-i-1] = o
            a[i-b+1:b-i-1] = m*len(a[i-b+1:b-i-1])
            if i < 19 :
                      z -= 1
                      a[b-z]=a[b+z]= o
                      a[b-z+1:b+z] = n
        print("".join(a))

little_mouth("\u25a0","\u25a1","★")
print("\n\n")
little_mouth("\u25a1","\u25a0","★")
print("\n\n")

def giant_mouth(n,m,o):
    for i in range(27):
        a= [n]*27
        b= (len(a)//2)
        if i >= 0 and i < 14:
            a[b-i] = a[b+i] = o
            a[(b-i)+1:b+i] = m
        else:
            a[i-b] = a[b-i-1] = o
            a[i-b+1:b-i-1] = m
        print("".join(a))

giant_mouth("\u25a0","\u25a1","★")
print("\n\n")
giant_mouth("\u25a1","\u25a0","★")
print("\n\n")
