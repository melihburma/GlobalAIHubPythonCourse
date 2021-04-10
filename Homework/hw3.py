def notes(): #funcion is ask user to student notes
    notes=[]
    x=input("midterm note: ")
    notes.append(x)
    y=input("project note: ")
    notes.append(y)
    z=input("final note: ")
    notes.append(z)
    return notes
def psGrade(x):#funcion is calculate passgrade
    note=int(stDic[x][0])*(0.3)+int(stDic[x][1])*(0.3)+int(stDic[x][2])*(0.4)
    notes=[x,note]
    return notes
def takeSecond(elem):#for sorting
    return elem[1]
sID=(1,2,3,4,5) #students id numbers
stDic={}
pGL=[]
for n in range(1,len(sID)+1):
    print(f"input {n}. student notes")
    stDic[n]=notes()
for n in range(1,len(sID)+1):
    pGL.insert(n-1,(psGrade(n)))
pGL.sort(reverse=True,key=takeSecond)
print(pGL)
