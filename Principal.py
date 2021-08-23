import time


!pip install WazeRouteCalculator
import WazeRouteCalculator
import time

from geopy.geocoders import Nominatim

import math

import pandas as pd



base_test01 = pd.read_csv("../input/dataenteltest/test.csv")


## Funcion 
def formato_01( lat1, long1 ):
    origen =   str(lat1) + ',' + str(long1 )
    return origen 

base_test01["ORIGEN_01"]   = base_test01.apply(lambda x: formato_01(  x.LATITUD_ORIGEN  , x.LONGITUD_ORIGEN  ), axis=1)
base_test01["DESTINO_01"]  = base_test01.apply(lambda x: formato_01(  x.LATITUD_DESTINO  , x.LONGITUD_DESTINO  ), axis=1)



for a0, row_0 in base_test01.iterrows():
    origen_1    = row_0['ORIGEN_01']
    destino_1   = row_0['DESTINO_01']
    
    print(origen_1)
        
    
    try:
        route = WazeRouteCalculator.WazeRouteCalculator(origen_1, destino_1)
        mm = route.calc_route_info(real_time=True)

        base_test01.loc[a0, 'TIEMPO']      = math.ceil(mm[0])*60
        base_test01.loc[a0, 'DISTANCIA']   = round(mm[1], 2 )*1000
        result = 'Exitoso'
    except:
        print("error")
##        time.sleep(3)            
##        pass



##   adding header
headerList = ['ID', 'DISTANCIA', 'TIEMPO']

# converting data frame to csv
base_test01[["ID", "DISTANCIA" , "TIEMPO"]].to_csv("sampleSubmission.csv", header=headerList, index=False)
