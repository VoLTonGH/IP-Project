import pandas as pd
import matplotlib.pyplot as plt

# To print the whole Data frame

def display_dataframe():
    
    print(d)

# Function to search

def search() :
    
    
    state_name=input('enter the state: ')
    print(d.loc[d['states'] == state_name])
    
# Function to modify the values in the csv file
    
def modify():
    
    season=input('enter season: ')
    index=d[d['seasons']==season].index
    #print(d)
    changeseason=input('enter the changed season: ')
    d.at[index,'seasons']=changeseason
    #print(d)
    display_dataframe()
    d.to_csv('seasons.csv',index=False)

# Function to delete a record

def delete():
    
    temp=input('enter temperature: ')
    indx=d[d['temperature(celcius)']==temp].index
    print(d.loc[indx])
    d.drop(indx,inplace=True)
    d.to_csv('bank_file.csv',index=False)
    print('record deleted')
    #display_dataframe()

# Function to sort the data in ascending order

def sorting_ascending():
    
    Df=d.sort_values(by=['temperature(celcius)'],ascending=True)
    print(Df)
    
# Function to sort the data in descending order

def sorting_descending():
    
    df1=d.sort_values('rainfall(cm)',ascending=False)
    print(df1)



def display_seasons():
    
    h=d['seasons']
    print(h)

def display_season_timeperiod_rainfall():
    
    g=d[['seasons','temperature(celcius)','rainfall(cm)']]
    print(g.head(5))

def display_states():
    
    a=d['states']
    print(a)

def plotting_temperature():
    X=d['seasons']
    Y=d['temperature(celcius)']
    plt.xlabel('Seasons')
    plt.ylabel('Temperature in celcius')
    plt.bar(X,Y,width=0.4,color='y')
    plt.show()

def display_timeperiod():
    
    f=d[['seasons','time-period(months)']]
    print(f)

def display_alternative():
    
    print(d.loc[0:10:2])

def display_temperature_rainfall():
    
    o=d[['seasons','temperature(celcius)','rainfall(cm)']]
    print(o)

def display_seasons_timeperiod():
    
    b=d[['seasons','states','time-period(months)']]
    print(b.tail(3))

def plotting_line_graph():
    
    z=d['seasons']
    v=d['rainfall(cm)']
    plt.plot(z,v,'r',linestyle='dotted',marker='*')
    plt.show()

# Generating the CSV file

def generate_csv():
    sno=[1,2,3,4,5,6,7,8,9]
    season=['monsoon','summer','winter','spring','winter','summer','summer','monsoon','spring']
    state=['kerala','rajasthan','karnataka','himachal pradesh','delhi','gujarat','haryana','jammu and kashmir','maharashtra']
    temp=['28-32','33-38','18-32','22-29','13-27','30-35','28-34','14-30','25-32']
    rainfall=['150-200','30-40','80-100','100-120','75-140','50-75','55-110','160-220','128-196']
    time=['march-july','april-june','september-december','july-september','september-october','january-march','april-june','november-december','september-october']
    dict={'sno':sno,'seasons':season,'states':state,'temperature(celcius)':temp,'rainfall(cm)':rainfall,'time-period(months)':time}
    df=pd.DataFrame(dict)
    df.to_csv('seasons.csv')
    pd.set_option('display.max_rows',500)
    pd.set_option('display.max_columns',500)

generate_csv()

d=pd.read_csv('seasons.csv')

c='y'
while(c=='y'):
    print('\n')
    print('1. Display the dataframe')
    print('2. Search')
    print('3. Modify')
    print('4. Delete')
    print('5. Sorting in ascending order')
    print('6. sorting in ascending order')
    print('7. Display seasons')
    print('8. Display first 5 states by season timeperiod rainfall')
    print('9. Display states')
    print('10. Plotting temperature')
    print('11. Displaying timeperiod')
    print('12. Display alternative record')
    print('13. Display temperature rainfall')
    print('14. Display seasons timeperiod')
    print('15. Plotting line graph')
    print('\n')
    ch=int(input('enter your choice number: '))
    print('\n')

    if ch==1:
        display_dataframe()
        print('\n')
    elif ch==2:
        search()
        print('\n')
    elif ch==3:
        modify()
        print('\n')
    elif ch==4:
        delete()
        print('\n')
    elif ch==5:
        sorting_ascending()
        print('\n')
    elif ch==6:
        sorting_descending()
        print('\n')
    elif ch==7:
        display_seasons()
        print('\n')
    elif ch==8:
        display_season_timeperiod_rainfall()
        print('\n')
    elif ch==9:
        display_states()
        print('\n')
    elif ch==10:
        plotting_temperature()
        print('\n')
    elif ch==11:
        display_timeperiod()
        print('\n')
    elif ch==12:
        display_alternative()
        print('\n')
    elif ch==13:
        display_temperature_rainfall()
        print('\n')
    elif ch==14:
        display_seasons_timeperiod()
        print('\n')
    elif ch==15:
        plotting_line_graph()
        print('\n')
    else:
        exit()
    print('\n')      
    #c=input('do you want to continue? y or n: ')
    print('\n')      
