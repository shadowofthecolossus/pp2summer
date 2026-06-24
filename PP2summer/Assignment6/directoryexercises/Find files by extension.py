import os

os.chdir("/Users/supernoob/Desktop/PP2/PP2summer/Assignment6/directoryexercises/sample")
l=os.listdir()
tufa=False
for i in l:
    if i.endswith(".jpg"):
        print("file with extension jpg: ",i)
        tufa=True
    elif  i.endswith(".txt"):
        print("file with extension txt: ",i)
        tufa=True
    
if not tufa:
    print("there is no files with txt or jpg extension")
