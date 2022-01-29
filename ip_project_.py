import pandas as pd
import matplotlib.pyplot as plt
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

def display_dataframe():
    d=pd.read_csv('seasons.csv')
    print(d)

def search() :
    d=pd.read_csv('seasons.csv')
    state=input('enter the state: ')
    data=d.loc[d['state']==state]
    print(data)
    
def modify():
    d=pd.read_csv('seasons.csv')
    season=input('enter season: ')
    index=d[d['season']==season].index
    #print(d)
    changeseason=input('enter the changed season: ')
    d.at[index,'season']==changeseason
    #print(d)
    display_dataframe()
    d.to_csv('seasons.csv',index=False)

def delete():
    d=pd.read_csv('seasons.csv')
    temp=input('enter temperature: ')
    indx=d[d['temp']==temp].index
    d1=d.drop(indx)
    d1.to_csv('seasons.csv',index=False)
    print('record deleted')
    display_dataframe()

def sorting_ascending():
    d=pd.read_csv('seasons.csv')
    Df=df.sort_values(by=['temp'],ascending=True)
    print(Df)

def sorting_descending():
    d=pd.read_csv('seasons.csv')
    df1=d.sort_values('rainfall',ascending=False)
    print(df1)

def display_seasons():
    d=pd.read_csv('seasons.csv')
    h=d['season']
    print(h)

def display_season_timeperiod_rainfall():
    d=pd.read_csv('seasons.csv')
    g=d[['season','temp','rainfall']]
    print(g.head(5))

def display_states():
    d=pd.read_csv('seasons.csv')
    a=d['state']
    print(a)

def plotting_temperature():
    X=df['seasons']
    Y=df['temperature(celcius)']
    plt.xlabel('seasons')
    plt.ylabel('temperature in celcius')
    plt.bar(X,Y,width=0.4,color='y')
    plt.show()

def plotting_timeperiod():
    d=pd.read_csv('seasons.csv')
    f=d[['seasons','time-period']]
    print(f)

def display_alternative():
    d=pd.read_csv('seasons.csv')
    print(d.loc[0:10:2])

def display_temperature_rainfall():
    d=pd.read_csv('seasons.csv')
    o=d[['season','temperature(celcius)','rainfall(cm)']]
    print(o)

def display_seasons_timeperiod():
    d=pd.read_csv('seasons.csv')
    b=d[['season','state','time period']]
    print(b.tail(3))

def plotting_line_graph():
    d=pd.read_csv('seasons.csv')
    z=d['seasons']
    v=d['rainfall(cm)']
    plt.plot(z,v,'r',linestyle='dotted',marker='*')
    plt.show()

c='y'
while(c=='y'):
    print('1.display_dataframe')
    print('2.search')
    print('3.modify')
    print('4.delete')
    print('5.sorting_in_ascending_order')
    print('6.sorting_in_ascending_order')
    print('7.display_seasons')
    print('8.display_first_5_states_by_season_timeperiod_rainfall')
    print('9.display_states')
    print('10.plotting_temperature')
    print('11.displaying_timeperiod')
    print('12.display_alternative_record')
    print('13.display_temperature_rainfall')
    print('14.display_seasons_timeperiod')
    print('15.plotting_line_graph')

    ch=int(input('enter your choice number: '))

    if ch==1:
        display_dataframe()
    elif ch==2:
        search()
    elif ch==3:
        modify()
    elif ch==4:
        delete()
    elif ch==5:
        sorting_ascending()
    elif ch==6:
        sorting_descending()
    elif ch==7:
        display_seasons()
    elif ch==8:
        display_first_5_states_by_season_timeperiod_rainfall()
    elif ch==9:
        display_states()
    elif ch==10:
        plotting_temperature()
    elif ch==11:
        displaying_timeperiod()
    elif ch==12:
        display_alternative_record()
    elif ch==13:
        display_temperature_rainfall()
    elif ch==14:
        display_state_timeperiod()
    elif ch==15:
        plotting_line_graph()
    else:
        sys.exit()
        
    c=input('do you want to continue? y or n: ')
