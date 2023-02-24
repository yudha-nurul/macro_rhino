import rhino3dm

# read an existing 3dm file
model = rhino3dm.File3dm.Read("existing_model.3dm")

# access the objects in the model
objects = model.Objects

# modify the objects in the model
for i, obj in enumerate(objects):
    if isinstance(obj, rhino3dm.Sphere):
        # move the sphere to a new location
        obj.SphereGeometry.Center = [i*10, 0, 0]

# save the modified model to a new file
model.Write("modified_model.3dm")



"""from rhino3dm import *
import requests  # pip install requests

req = requests.get("MacroRhino/sample.3dm")

model = File3dm.FromByteArray(req.content)
for obj in model.Objects:
    geometry = obj.Geometry
    bbox = geometry.GetBoundingBox()
    print("{}, {}".format(bbox.Min, bbox.Max))
"""