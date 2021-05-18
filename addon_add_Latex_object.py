bl_info = {
    "name": "Add Blender Latex",
    "author": "Aki78",
    "version": (1, 0),
    "blender": (2, 92, 0),
    # "location": "View3D > Add > Mesh > New Object",
    "description": "Adds a new Latex Object",
    "warning": "Still Alpha",
    "doc_url": "",
    "category": "Add Mesh",
}


import bpy
from bpy.types import Operator
from bpy.props import FloatVectorProperty
from bpy_extras.object_utils import AddObjectHelper, object_data_add
from mathutils import Vector
import re
import subprocess
import os
from pathlib import Path
home = str(Path.home())

class add_latex_object(bpy.types.Operator):
    """Select by  Python Regex"""
    bl_idname = "object.add_latex"
    bl_label = "add_latex"
    bl_options = {'REGISTER', 'UNDO'}
    text = bpy.props.StringProperty(name= "Enter Tex Expression (\\\\=\\)", default= "" )

    def execute(self, context):
        if not os.path.exists(home+"/.latex_blender"):
            subprocess.run(["mkdir", home+"/.latex_blender"])
            print(home+"/.latex_blender/latex_blender_template.tex")
#            subprocess.run(["echo",  "\documentclass{standalone}", ">>" , home+"/.latex_blender/latex_blender_template.tex"])
            subprocess.run([ "touch", home+"/.latex_blender/latex_blender_template.tex"])
            text_file = open(home+"/.latex_blender/latex_blender_template.tex","w")
            n = text_file.write(
             "\\documentclass{standalone}\n\\usepackage{lmodern} %or whatever you like\n\\usepackage[intlimits]{amsmath}\n\\usepackage{amsthm, amssymb, amsfonts} %Useful stuff\n\\begin{document}\n$ change $\n\\end{document}"
                    )
            text_file.close()
            print("CREATING STORE DIRECTORY")
        
        t = self.text
        print(t)
        
        subprocess.run(["cp", home+"/.latex_blender/latex_blender_template.tex",home+ "/.latex_blender/template2.tex" ])
        subprocess.run(['sed', '-i', 's/change/' + t +'/g',home+ '/.latex_blender/template2.tex' ])

        subprocess.run(["pdflatex", "-halt-on-error","-output-directory",home+"/.latex_blender",home+"/.latex_blender/template2.tex"])
        subprocess.run(["pdftocairo", "-svg", home+"/.latex_blender/template2.pdf", home+"/.latex_blender/expression.svg"])
        bpy.ops.import_curve.svg(filepath=home+"/.latex_blender/expression.svg")
#        bpy.data.objects["Curve"].name = t
        bpy.data.collections["expression.svg"].name = t
#        col = bpy.data.collections.get("expression.svg")
        col = bpy.data.collections.get(t)
        for obj in col.all_objects:
            print(obj)
            obj.scale = (1000,1000,1000)
            obj.location = bpy.data.scenes[0].cursor.location
#incorrect        bpy.data.collections[t].location  = bpy.data.scenes[0].cursor.location
        return {'FINISHED'}

     
    
    def invoke(self, context, event):
        
        return context.window_manager.invoke_props_dialog(self)



# store keymaps here to access after registration
addon_keymaps = []

def register():
    bpy.utils.register_class(add_latex_object)

    # handle the keymap
    wm = bpy.context.window_manager
    km = wm.keyconfigs.addon.keymaps.new(name='Object Mode', space_type='EMPTY')
    kmi = km.keymap_items.new(add_latex_object.bl_idname, 'T', 'PRESS', ctrl=False, shift=True)
    addon_keymaps.append(km)

def unregister():
    bpy.utils.unregister_class(OBJECT_OT_add_object)

if __name__ == "__main__":
    register()
