import rhinoscriptsyntax as rs

#objToCopy = rs.GetObjects("select object yang mau diCOPY")
#print(objToCopy)

#reffPoint = rs.GetPoint("select point REFERENSInya")

# create list target point
#targetPoints = rs.GetObjects("select point TARGETnya",rs.filter.point | rs.filter.pointcloud,True,True)

objToCopy = rs.GetObjects("select object yang mau diCOPY")
reffPoint = rs.GetPoint("select point REFERENSInya")#ini sudah xyz
print(reffPoint)
targetPointsId = rs.GetObjects("select point TARGETnya",rs.filter.point | rs.filter.pointcloud,True,True)
target = None
rs.Command("Copy")
rs.Command(reffPoint)



"""
#dari example
objectIds = rs.GetObjects("Select objects to copy")
start = rs.GetPoint("Point to copy from")
for go in targetPoints:
    end = rs.GetPoint("Point to copy to", start)
    
    rs.CopyObjects( objectIds, go )
"""



"""
# create list target point
targetPoints = rs.GetObjects("select point TARGETnya",rs.filter.point | rs.filter.pointcloud,True,True)
for point in targetPoint:
    point = rs.PointCoordinates(id)
    #print(point)
"""

"""
- select object yang mau dicopy, var objtocopy
- select point refference (filter point), var pointreffxyz
- select target point (filter point), var targetPoint
- command :
    copy
    select object objToCopy,  enter
    input point from pointReff
    input target from target point
    enter
    finish
    
"""