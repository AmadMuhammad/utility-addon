bl_info = {
    "name": "Rhino_CAD(fbx) Processing",
    "description": "works with fbx exported form Rhino",
    "author": "Amad_Muhammad, twitter: @AmadMuhammad17",
    "version": (0, 0, 1),
    "blender": (2, 83, 7),
    "location": "search menu",
}


import bpy


class OBJECT_OT_step2(bpy.types.Operator):
    """Step2 on collections"""
    bl_idname = "object.step2"
    bl_label = "Step2"

    def execute(self, context):
        bpy.ops.object.select_by_type(type='EMPTY')
        bpy.ops.object.delete(use_global=True)
        bpy.ops.object.select_all(action='SELECT')
        bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY')
        bpy.ops.view3d.snap_cursor_to_center()
        bpy.ops.view3d.snap_selected_to_cursor(use_offset=True)
        bpy.ops.transform.resize(value=(0.03, 0.03, 0.03), orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', mirror=True, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False)
        bpy.ops.transform.rotate(value=1.5708, orient_axis='X', orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(True, False, False), mirror=True, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False)

        
        
        return {'FINISHED'}






def register():
    bpy.utils.register_class(OBJECT_OT_step2)


def unregister():
    bpy.utils.unregister_class(OBJECT_OT_step2)

