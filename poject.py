import pandas as pd
import matplotlib.pyplot as pl
ch='Y'
while ch=='Y':
  print('1.read CSV File')
  print('2.show all Records')
  print('3.show 1st 3 Records')
  print('4.show last 3 Records')
  print('5.Show the Name of Failed Students')  #marks less than 40
  print('6.Add new Row')
  print('7.Delete Row')
  print('8.Show Result using Line Graph')
  print('9.Show Result using Bar Graph')
  print('10.Save Data into CSV File')
  choice=int(input('Enter your Choice : '))
  if choice==1: 
    df=pd.read_csv('C:\test.csv') #read the csv file
    print('File Opened')
  elif choice==2:
    print(df)
  elif choice==3:
    print(df.head(3))
  elif choice==4:
    print(df.tail(3))
  elif choice==5:
    print(df[df['marks']<40]['name'])
  elif choice==6:
    r=int(input('Enter Roll No: '))
    n=input('Enter Name: ')
    m=int(input('Enter Marks: '))
    df=df.append({'roll':r,'name':n,'marks':m},ignore_index=True)
    print('Record Added')
  elif choice==7:
    r=int(input('Enter Roll No to Delete: '))
    df=df[df['roll']!=r] 
    print('Record Deleted')
  elif choice==8:
    pl.ylabel('Marks')
    pl.xlabel('Rollno')
    pl.plot(df['Roll'].df['Marks'])
    pl.title('Result') 
    pl.show()
  elif choice==9:
    pl.bar(df['Roll'],df['Marks'])
    pl.title('Result')
    pl.xlabel('Rollno')
    pl.ylabel('Marks')
    pl.show()
  elif choice==10:
    df.to_csv('C:\test.csv',index=False)
    print('File Saved')
    ch=input('Do you want to Continue: ').upper()