import rhinoscriptsyntax as rs
objectIds = rs.GetObjects("Select objects to copy")
a = []
if objectIds:
    start = rs.GetPoint("Point to copy from")
    print(start)
    print(type(start))
    if start:
        targetPoints = rs.GetObjects("select point TARGETnya",rs.filter.point | rs.filter.pointcloud,True,True)
        #end = rs.GetPoint("Point to copy to", start)
        #if end:
        for point in targetPoints:
            xyz = rs.PointCoordinates(point)
            xyzok1 = xyz - start
            xyzok1 = str(xyzok1)
            print(xyzok1)
            print(type(xyzok1))
            a = List.append(xyzok1)
print(a)
            #if xyzok1:
#rs.Command("_Copy")
#print(xyz) #xyz ini sudah ok
#translation = point-start
#rs.CopyObjects( objectIds, translation )