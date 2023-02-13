import rhinoscriptsyntax as rs
import scriptcontext as sc
# import os


def BatchExport3dmByLayer():
    doc_name=sc.doc.Name
    ft="igs"
    filt = "{} Files (*.{})|*.{}||".format(ft,ft.lower(),ft.lower())
    if not doc_name:
        #document hasn't been saved
        msg="Main file name/folder for {} export?".format(ft)
        filename=rs.SaveFileName(msg, filt)
        #SaveFileName returns the complete path plus file name
        if filename==None: return
    else:
        #document has been saved, get path
        msg="Folder for {} export? (Enter to save in current folder)".format(ft)
        filename=rs.SaveFileName(msg, filt)
        if filename==None: return
        
    
    #start the export sequence
    rs.EnableRedraw(False)
    layers=rs.LayerNames()
    for layer in layers:
        if rs.IsLayerSelectable(layer):
            #split layer name at character "::"
            layer_name=layer.split(":")[-1]
            e_file_name = '"{} {}.{}" '.format(filename[:-4],layer_name,ft.lower())
            rs.UnselectAllObjects()
            rs.ObjectsByLayer(layer,True)
            objs=rs.SelectedObjects()
            if objs:
                #runs the export using the file name/path and your settings
                rs.Command("-_Export "+e_file_name+" _Enter", False)
            rs.UnselectAllObjects()


BatchExport3dmByLayer()