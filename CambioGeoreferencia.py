from pyproj import Proj

# primero se debe definir la transformación, que permite ir de lon/lat a x/y
# para ello se debe escojer el tipo de transformada para este caso usaremos 
# 19S UTM <-> WGS84
# para encontrar otros códigos de transformadas https://epsg.io/?q=19s
UTM19S = Proj("+init=EPSG:32719")

#CONVENCIÓN::: Long, Lat -> Este, Norte ::: 
#para Norte, Este -> Long, Lat usar inverse = True

#coordenadas de Santiago
lat = -33.4372
lon = -70.6506

#pasamos de lon/lat a UTM
este, norte = UTM19S(lon, lat)


#devolvemos el cambio
LON, LAT = UTM19S(este, norte, inverse = True)



print('Coordenadas iniciales en lon/lat:')
print('Latitud = ' + str(lat))
print('Longitud =' + str(lon))
print()
print()
print('transformamos a UTM')
print('este = ' + str(este))
print('norte = ' + str(norte))
print()
print()
print('devolvemos la transformada:')
print('Latitud = ' + str(LAT))
print('Longitud = ' + str(LON))