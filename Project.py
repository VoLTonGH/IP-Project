import pandas as pd
import matplotlib.pyplot as pl
print("""

      ░█████╗░███████╗███╗░░██╗████████╗██████╗░░█████╗░██╗░░░░░  ██████╗░░█████╗░███╗░░██╗██╗░░██╗
      ██╔══██╗██╔════╝████╗░██║╚══██╔══╝██╔══██╗██╔══██╗██║░░░░░  ██╔══██╗██╔══██╗████╗░██║██║░██╔╝
      ██║░░╚═╝█████╗░░██╔██╗██║░░░██║░░░██████╔╝███████║██║░░░░░  ██████╦╝███████║██╔██╗██║█████═╝░
      ██║░░██╗██╔══╝░░██║╚████║░░░██║░░░██╔══██╗██╔══██║██║░░░░░  ██╔══██╗██╔══██║██║╚████║██╔═██╗░
      ╚█████╔╝███████╗██║░╚███║░░░██║░░░██║░░██║██║░░██║███████╗  ██████╦╝██║░░██║██║░╚███║██║░╚██╗
      ░╚════╝░╚══════╝╚═╝░░╚══╝░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚═╝╚══════╝  ╚═════╝░╚═╝░░╚═╝╚═╝░░╚══╝╚═╝░░╚═╝
      _____________________________________________________________________________________________
      """)

usr=input(" ENTER USERNAME: ")
passwd=input("\n ENTER PASSWORD: ")
ch='N'

print('\n')
if usr=='admin' and passwd=='admin':
	ch='Y'
	print("==============================================================================================\n")
	print("LOGIN SUCCESFUL!!!\n")
	print("==============================================================================================\n\n")
else:
	print("INCORRECT PASSWORD AND OR USERNAME !!!\n")
	quit()

print("Reading the Bank File...")
df=pd.read_csv('bank_file.csv') # Read the csv file

while ch=='Y':
  print('\n')
  print("==============================================================================================")
 
  print("\n")
  print("1.Make a Deposit or Withdrawal")
  print('2.Add new Account')
  print('3.Show all Records')
  print('4.Show 1st 3 Records')
  print('5.Show last 3 Records')
  print('6.Show the Accounts with Low Balance')  #Balance less than 10k
  print('7.Delete Account')
  print('8.Show Bank Balances using Line Graph')
  print('9.Show Bank Balances using Bar Graph')
  print('10.Show Total Bank Deposits')
  print('11.Save Data into CSV File')
  print('\n')
  choice=int(input('Enter your Choice : '))
  print('\n')
  print("==============================================================================================")
  print('\n')
  
  if choice==1:  # Deposit or Withdrawal
    hmm=input("Do you want to Deposit or Withdrawal?(D/W): ")
    hmm=hmm.upper()
    if hmm=='D':
      x=int(input('Enter the Account Number : '))
      y=int(input('Enter the Amount : '))
      df.loc[df['Account_number']==x,'Balance'] = df.loc[df['Account_number']==x,'Balance'] + y
      print('\n')
      print("Deposited Successfully!")
      df['Balance'] = df['Balance'].replace([],'new value')
      
    elif hmm=='W':
      x=int(input('Enter the Account Number : '))
      y=int(input('Enter the Amount : '))
      
      if int(df.loc[df['Account_number']==x,'Balance']) >= y :
        df.loc[df['Account_number']==x,'Balance'] = df.loc[df['Account_number']==x,'Balance'] - y
        print('\n')
        print('Withdrawal Successful!')
      else:
        print('\n')
        print('\nInsufficient Balance.')
  
  elif choice==2: # Add new Account
    r=int(input('Enter Account Number: '))
    n=input('Enter Name of Account Holder: ')
    o=input('Enter Phone Number: ')
    m=int(input('Enter Balance: '))
    p=input('Enter Address: ')
    df=df.append({'Account_number':r,'Name':n,'Balance':m,'Phone_Number':o,'Address':p},ignore_index=True)
    print('\n')
    print('Account Added')
    print("""

      ████████╗██╗░░██╗░█████╗░███╗░░██╗██╗░░██╗  ██╗░░░██╗░█████╗░██╗░░░██╗
      ╚══██╔══╝██║░░██║██╔══██╗████╗░██║██║░██╔╝  ╚██╗░██╔╝██╔══██╗██║░░░██║
      ░░░██║░░░███████║███████║██╔██╗██║█████═╝░  ░╚████╔╝░██║░░██║██║░░░██║
      ░░░██║░░░██╔══██║██╔══██║██║╚████║██╔═██╗░  ░░╚██╔╝░░██║░░██║██║░░░██║
      ░░░██║░░░██║░░██║██║░░██║██║░╚███║██║░╚██╗  ░░░██║░░░╚█████╔╝╚██████╔╝
      ░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝╚═╝░░╚═╝  ░░░╚═╝░░░░╚════╝░░╚═════╝░""")
      
  elif choice==3: # Show all Records
    print(df)
    
  elif choice==4: # Show 1st 3 Records
    print(df.head(3))
    
  elif choice==5: # Show last 3 Records
    print(df.tail(3))
    
  elif choice==6: # Show the Accounts with low balace
    min=10000 # df['Balance'].min()
    index=df.index[df['Balance']<=min].tolist()
    print(df.loc[index])
    
  elif choice==7: # Delete Account
    r=int(input('Enter Account Number to Delete: '))
    indx=df.index[df['Account_number']==r]
    x=int(input('Enter Phone Number: '))
    print(indx)
    df.drop(indx,inplace=True)
    print('\n')
    print('Account Deleted')
    
  elif choice==8: # Show Bank Balances using Line Graph
    pl.ylabel('Balance')
    pl.xlabel('Account_number')
    pl.plot(df['Account_number'],df['Balance'])
    pl.title('Line Graph of the Accounts') 
    pl.show()
    
  elif choice==9: # Show Bank Balances using Bar Graph
    pl.xlabel('Account Number')
    pl.ylabel('Balance')
    pl.bar(df['Account_number'],df['Balance'])
    pl.title('Bar Graph of Accounts')
    pl.show()
    
  elif choice==10: # Show Total Bank Deposit
    print("Bank Total Deposits: ",df['Balance'].sum())
    
  elif choice==11: # Save Data into CSV File
    df.to_csv('bank_file.csv',index=False)
    print('File Saved')
    ch=input('Do you want to Continue: ').upper()
    if ch=='Y':
      continue
    else:
      print("""

      ████████╗██╗░░██╗░█████╗░███╗░░██╗██╗░░██╗  ██╗░░░██╗░█████╗░██╗░░░██╗
      ╚══██╔══╝██║░░██║██╔══██╗████╗░██║██║░██╔╝  ╚██╗░██╔╝██╔══██╗██║░░░██║
      ░░░██║░░░███████║███████║██╔██╗██║█████═╝░  ░╚████╔╝░██║░░██║██║░░░██║
      ░░░██║░░░██╔══██║██╔══██║██║╚████║██╔═██╗░  ░░╚██╔╝░░██║░░██║██║░░░██║
      ░░░██║░░░██║░░██║██║░░██║██║░╚███║██║░╚██╗  ░░░██║░░░╚█████╔╝╚██████╔╝
      ░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝╚═╝░░╚═╝  ░░░╚═╝░░░░╚════╝░░╚═════╝░""")
