s1= ['Ahmad', 18, 17, 19.5, 8, 25]
s2= ['Sami', 20, 20, 19, 9, 28]
s3= ['Faris', 14.5, 16, 13, 7, 23]

name= input("Enter student's name: ")
if name not in s1 and name not in s2 and name not in s3:
    print("Student is not recorded 0")
else:
    if name in s1:
        sSum=s1[1:len(s1)]
        print(name, sum(sSum))
    elif name in s2:
        sSum=s2[1:len(s2)]
        print(name, sum(sSum))
    elif name in s3:
        sSum=s3[1:len(s3)]
        print(name, sum(sSum))