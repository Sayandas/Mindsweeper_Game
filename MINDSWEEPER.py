import random

def find(matrix,x,y):
    c=0
    if matrix[x][y]!=' ' and matrix[x][y]!='*' and matrix[x][y]==0:
        for i in range(x-1,x+2,1):
            for j in range(y-1,y+2,1):
                if i<n and j <n and i>=0 and j>=0:
                     if matrix[i][j]=='*' :
                                matrix[x][y]= matrix[x][y]+1
                                c=c+1
    
        if c==0:
            matrix[x][y]=' '
            for j in range(x-1,x+2,1):
                     for p in range(y-1,y+2,1):
                         if j<n and p<n and j>=0 and p>=0 and  matrix[j][p]==0:
                             find(matrix,j,p)
        else:
            return
    else:
        return 

def prin(matrix,n):
    c=0;
    for i in range(0,n,+1):
        for j in range(0,n,+1):
            c=c+1
            if matrix[i][j]!=' ':
                if matrix[i][j]==999:
                    print "F\t",
                elif matrix[i][j]==0:
                    #if matrix[i][j]=='*':
                        print "(%d)\t" %c,
                if matrix[i][j]=='*':
                        print "(%d)\t" %c,
                elif matrix[i][j]>0 and matrix[i][j]!=999:
                    print "%d\t" %matrix[i][j],
                elif matrix[i][j]==' ':
                    print matrix[i][j],
                    print"\t"
            else:
                print " \t",
        print ""
        print ""

def oprin(matrix,n):
           c=0;
           for i in range(0,n,+1):
                for j in range(0,n,+1):
                    c=c+1
                    if matrix[i][j]!=' ':
                        if matrix[i][j]==999:
                            print "F\t",
                        elif matrix[i][j]=='*':
                            print "*\t",
                        elif matrix[i][j]==0:
                           print "(%d)\t" %c,
                        elif matrix[i][j]>0 and matrix[i][j]!=999:
                            print "%d\t" %matrix[i][j],
                        else:
                            print matrix[i][j],
                            print"\t",
                    else:
                        print " \t",
                print ""
                print ""

    


#strt logic
n=input("Enter the Matrix value n where n * n mat!")
matrix=[]
for i in range(0,n,+1):
    new=[]
    for j in range(0,n,+1):
        new.append(0)
    matrix.append(new)

prin(matrix,n)
bom=input("Enter the Number of bomb!!")
boom=bom
boom1=bom
for i in range(0,bom,1):
    x=random.randint(0,n-1)
    y=random.randint(0,n-1)
    while(matrix[x][y]=='*'):
        x=random.randint(0,n-1)
        y=random.randint(0,n-1)
    if matrix[x][y]!='*':
        matrix[x][y]='*'
    else:
        i=i-1

while(1):
    print "No of FLAG %d" %boom
    ex=input("Enter the 0 For Exit!!")
    if(ex==0):
        break
    cho=input("Enter the choice Box!!")
    if cho%n==0:     
        x=(cho/n)-1
    else:
        x=(cho/n)

    if cho%n==0:     
        y=n-1
    else:
        y=(cho%n)-1
    c=0
    if matrix[x][y]=='*':
        oprin(matrix,n)
        print "You are out!!"
        break

    elif matrix[x][y]!=' ' and matrix[x][y]==0:
            for i in range(x-1,x+2,+1):
                for j in range(y-1,y+2,+1):
                    if i<n and j<n and i>=0 and j>=0:
                            if matrix[i][j]=='*':
                                matrix[x][y]= matrix[x][y]+1
                                c=c+1
    
            if c==0:
                 matrix[x][y]=' '
                 for j in range(x-1,x+2,1):
                     for p in range(y-1,y+2,1):
                         if j<n and p<n and j>=0 and p>=0:
                             find(matrix,j,p)
               

 
    prin(matrix,n)
    if(boom1>0 and boom>0):
        e=input("Are you Want to set flag enter (1) for yes and (2) for No")
        if(e==1):
            pos=input("Enter the flag position!!");
            if pos%n==0:     
                x=(pos/n)-1
            else:
                x=(pos/n)

            if pos%n==0:     
                y=n-1
            else:
                y=(pos%n)-1
            if matrix[x][y]=='*':
                boom1=boom1-1
                boom=boom-1
                matrix[x][y]=999
                prin(matrix,n)
            else:
                boom1=boom1-1
            if(boom==0):
                print "WINNER WINNER!!!!!"
                break
    elif boom1<=0:
        print " LOSE!!!YOUR FLAG SET CHOICE IS FINISHED!!"
        break                
