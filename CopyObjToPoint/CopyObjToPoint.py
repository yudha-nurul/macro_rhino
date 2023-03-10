import rhinoscriptsyntax as rs
objectIds = rs.GetObjects("Select objects yang mau di COPY")
a = list()
if objectIds:
    start = rs.GetPoint("select REFERENSI Point nya")
    print(start)
    print(type(start))
    
    if start:
        targetPoints = rs.GetObjects("select point TARGETnya",rs.filter.point | rs.filter.pointcloud,True,True)
        #end = rs.GetPoint("Point to copy to", start)
        #if end:
        for point in targetPoints:
            xyz = rs.PointCoordinates(point)
            xyzok1 = xyz - start
            rs.CopyObjects( objectIds, xyzok1 )


# print(a)
            #if xyzok1:
#rs.Command("_Copy")
#print(xyz) #xyz ini sudah ok
#translation = point-start
#rs.CopyObjects( objectIds, translation )

""" target point = point2 coordinate, contohnya :
-52.6759008050801,52.3893563178108,-1.41394598074385E-06
-49.0277048977212,40.6402454111804,-1.41394598074385E-06

targetnya menjadi :
    ("_Copy 0,0,0 0,10,0 _Enter")
"""

