import rhinoscriptsyntax as rs
objectIds = rs.GetObjects("Select objects to copy")
if objectIds:
    start = rs.GetPoint("Point to copy from")
    print(start)
    if start:
        targetPoints = rs.GetObjects("select point TARGETnya",rs.filter.point | rs.filter.pointcloud,True,True)
        #end = rs.GetPoint("Point to copy to", start)
        #if end:
        for point in targetPoints:
            xyz = rs.PointCoordinates(point)
            xyzok1 = xyz - start
            print(xyzok1)
            if xyzok1:
                rs.Command("_Copy")
            #print(xyz) #xyz ini sudah ok
            #translation = point-start
            #rs.CopyObjects( objectIds, translation )
            
