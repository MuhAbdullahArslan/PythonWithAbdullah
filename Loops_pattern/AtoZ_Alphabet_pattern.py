# Alphabet A to Z Pattern
print("\n","="*2,"pattern (A)","="*2,"\n")
row = 5
for r in range(1,row+1):
    for c in range(1,row+1):
        if c == 1 or r == 1 or c == row or r == row//2 +1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
print("\n","="*2,"pattern (B)","="*2,"\n")
row = 5
for r in range(1,row+1):
    for c in range(1,row+1):
        if c == 1 or r == 1 or (c == row and r != row//2+1 ) or r == row or (r == row//2+1 and c != row):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
    
print("\n","="*2,"pattern (C)","="*2,"\n")
row = 5
for r in range(1,row+1):
    for c in range(1,row+1):
        if r == 1 or c ==1 or r == row:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
    
print("\n","="*2,"pattern (D)","="*2,"\n")
row = 5
for r in range(1,row+1):
    for c in range(1,row+1):
        if (r == 1 and c != row) or c ==1 or(r == row and c != row) or (c == row and r != 1 and r != row):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
    
print("\n","="*2,"pattern (E)","="*2,"\n")
row = 5
for r in range(1,row+1):
    for c in range(1,row+1):
        if c ==1 or r==1 or r == row or r == 5//2+1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
    
print("\n","="*2,"pattern (F)","="*2,"\n")
row = 5
for r in range(1,row+1):
    for c in range(1,row+1):
        if c ==1 or r==1 or r == 5//2+1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
    
print("\n","="*2,"pattern (G)","="*2,"\n")
row = 5
for r in range(1,row+1):
    for c in range(1,row+1):
        if c ==1  or r==1 or r == row or (c == row and r != row//2 ) or (r == row//2+1 and c != 2 and c != 3):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
    
print("\n","="*2,"pattern (H)","="*2,"\n")
row = 5
for r in range(1,row+1):
    for c in range(1,row+1):
        if c ==1 or c ==row or r == row//2+1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
    
print("\n","="*2,"pattern (I)","="*2,"\n")
row = 5
for r in range(1,row+1):
    for c in range(1,row+1):
        if r ==1 or r ==row or c == row//2+1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
    
print("\n","="*2,"pattern (J)","="*2,"\n")
row = 5
for r in range(1,row+1):
    for c in range(1,row+1):
        if r == 1 or c == row//2+1 or (r == 5 and c <= row//2+1) or (c == 1 and r > row//2+1):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
print("\n","="*2,"pattern (K)","="*2,"\n")
row = 5
for r in range(1,row+1):
    for c in range(1,row+1):
        if c == 1 or r+c == 5 or r-c == 1 :
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
    
print("\n","="*2,"pattern (L)","="*2,"\n")
row = 5
for r in range(1,row+1):
    for c in range(1,row+1):
        if c == 1 or r== 5 :
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
    
print("\n","="*2,"pattern (M)","="*2,"\n")
row = 5
for r in range(1,row+1):
    for c in range(1,row+1):
        if c == 1 or (r-c == 0 and r< row//2+1) or (r+c == 6 and r<= row//2+1) or c == row :
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
    
print("\n","="*2,"pattern (N)","="*2,"\n")
row = 5
for r in range(1,row+1):
    for c in range(1,row+1):
        if c == 1 or r-c == 0  or c == row :
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
    
print("\n","="*2,"pattern (O)","="*2,"\n")
row = 5
for r in range(1,row+1):
    for c in range(1,row+1):
        if c == 1 or r == 1 or c == row or r == row :
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
    
print("\n","="*2,"pattern (P)","="*2,"\n")
row = 5
for r in range(1,row+1):
    for c in range(1,row+1):
        if c == 1 or r == 1 or (c == row and r <= row//2+1) or (r == row//2+1 and c != row) :
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
    
print("\n","="*2,"pattern (Q)","="*2,"\n")
row = 5
for r in range(1,row+1):
    for c in range(1,row+1):
        if (c == 1 and r != row) or (c == row-1 and r != row) or (r == 1 and c != row) or (r == row-1 and c != row) or (r-c == 0 and r > row//2) :
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
    
print("\n","="*2,"pattern (R)","="*2,"\n")
row = 5
for r in range(1,row+1):
    for c in range(1,row+1):
        if r == 1 or c ==1 or r == row//2+1 or (c == row and r <= row//2+1) or (r-c == 0 and r > row//2+1) :
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
    
print("\n","="*2,"pattern (S)","="*2,"\n")
row = 5
for r in range(1,row+1):
    for c in range(1,row+1):
        if r == 1 or r == row or r == row//2+1 or (c == 1 and r < row//2+1) or (c== row and r > row//2+1)  :
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
    
print("\n","="*2,"pattern (T)","="*2,"\n")
row = 5
for r in range(1,row+1):
    for c in range(1,row+1):
        if r == 1 or c == row//2+1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
    
print("\n","="*2,"pattern (U)","="*2,"\n")
row = 5
for r in range(1,row+1):
    for c in range(1,row+1):
        if c == 1 or c == row or r == row:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
    
print("\n","="*2,"pattern (U)","="*2,"\n")
row = 5
for r in range(1,row+1):
    for c in range(1,row+1):
        if c == 1 or c == row or r == row:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
    
print("\n","="*2,"pattern (V)","="*2,"\n")
row = 5
for r in range(1,row+1):
    for c in range(1,row+1):
        if (c ==1 and r <= row//2+1) or (c ==row and r <= row//2+1) or (r == row-1 and c % 2 == 0) or (r ==row and c == 3) :
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
    
print("\n","="*2,"pattern (W)","="*2,"\n")
row = 5
for r in range(1,row+1):
    for c in range(1,row+1):
        if c ==1 or c == row or (r-c == 0 and r >= row//2+1) or (r+c == 6 and r > row//2+1) :
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
    
print("\n","="*2,"pattern (X)","="*2,"\n")
row = 5
for r in range(1,row+1):
    for c in range(1,row+1):
        if r-c == 0  or r+c == 6  :
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
    
print("\n","="*2,"pattern (Y)","="*2,"\n")
row = 5
for r in range(1,row+1):
    for c in range(1,row+1):
        if (r-c == 0 and r<row//2+1)  or (r+c == 6 and r<=row//2+1) or (c== 3 and r > row//2+1) :
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
    
print("\n","="*2,"pattern (Z)","="*2,"\n")
row = 5
for r in range(1,row+1):
    for c in range(1,row+1):
        if r ==1 or r == row or r+c == 6 :
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()


