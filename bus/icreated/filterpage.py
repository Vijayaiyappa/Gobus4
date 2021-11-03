import sqlite3
from sqlite3 import OperationalError
import pandas as pd


class pan:
    @staticmethod
    def filt():
         
         import pandas as pd
         
         
         con = sqlite3.connect("C:/Users/Aiyoo/busfinal/viche/db.sqlite3")
         df = pd.read_sql_query("SELECT  Middle_route, source, destination, arrive_t, leave_t, Busname from bus_data_given_by_user", con)
         array_send=[]
         pf=df[df.duplicated()]
         #print(pf)
         #print("printing the name")

         #filtered_data = pd.DataFrame(columns = ['Middle_route', 'source', 'destination','arrive_t','leave_t','Busname'], 
                   
  
         pds=df[df.duplicated()].drop_duplicates()
         name=pds.iloc[0][1] # change first index to chnage the name 
         """
         print("first name 0 index row1")
         print(name)
         print("_____________")
         print(pds.iloc[0]) 
         print("____Duplicates droped____")
         print(pds)
         print("_____________")
         """
        
         for i in pds.iloc:
             print(i[0])
             name=i[0]
             same5=df.loc[(df["Middle_route"]==i[0]) &( df["source"]==i[1]) & ( df["destination"]==i[2]) & ( df["arrive_t"]==i[3])& ( df["leave_t"]==i[4]) & ( df["Busname"]==i[5]) ]
             
          
             count=len(same5.loc[same5["Middle_route"]==name].index)
            
             same_data=[]
             if(count>=5):
                 
                 fit=same5.loc[same5["Middle_route"]==name].drop_duplicates()
                
                 array_send.append([same5.iat[0,0],same5.iat[0,1],same5.iat[0,2],same5.iat[0,3],same5.iat[0,4],same5.iat[0,5]])
                
         print("boo",array_send)
         return array_send

# Be sure to close the connection
         
class filter_un_data:
     @staticmethod
     def filt():
         
         import pandas as pd
         
         
         con = sqlite3.connect("C:/Users/Aiyoo/busfinal/viche/db.sqlite3")
         df = pd.read_sql_query("SELECT  town_tab_name, post_id,complaint  from bus_incorrect_data", con)
         array_send=[]
         pf=df[df.duplicated()]
       
         pds=df[df.duplicated()].drop_duplicates()
         print(pds)
         name=pds.iloc[0][1] # change first index to chnage the name 
         
        
         for i in pds.iloc:
             print(i[0])
             name=i[0]
           
             same5=df.loc[(df["town_tab_name"]==i[0]) &( df["post_id"]==i[1]) & ( df["complaint"]==i[2])  ]
             
             count=len(same5.loc[same5["town_tab_name"]==name].index)
             
             same_data=[]
             if(count>=5):
               
                 array_send.append([same5.iat[0,0],same5.iat[0,1],same5.iat[0,2]])
         
         print("boo",array_send)
         return array_send

class updater:
  
    @staticmethod
    #  Middle_route source destination arrive_t leave_t Busname
   
    def update_pls(Middle_route,source,destination,arrive_t,leave_t,Busname,ide):
        from django.apps import apps
        c=apps.get_model("bus",source)
        filtered=c.objects.all().get(id=ide)
        filtered.source=source
        filtered.Middle_route=Middle_route
        filtered.destination=destination
        filtered.arrive_t=arrive_t
        filtered.leave_t=leave_t
        filtered.Busname=Busname
        filtered.save()
        print("updated")
        
    @staticmethod
    def fetch_data(source,ide):
        from django.apps import apps
        c=apps.get_model("bus",source)
        filtered=c.objects.all().get(id=ide)
        return filtered 
        


