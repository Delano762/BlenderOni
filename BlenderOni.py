import bpy
from math import pi, radians
from mathutils import Matrix, Quaternion, Vector

bl_info={
    'name': "BlenderOni",
    'author': "Delano762",
    'description': "Companion addon for Oni-Rigify animation rig available in the documentation link.",
    'doc_url': "http://mods.oni2.net/node/388",
    'blender': (2,80,0),
    'version': (1,1),
    'location': "View3D > BlenderOni",
    'category': "BlenderOni"
}

class BlenderOniPanel:
    bl_idname = "BLENDERONI_PT_"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "BlenderOni"

class BOP_Main(BlenderOniPanel,bpy.types.Panel):
    bl_label = "BlenderOni"
    bl_idname = "BLENDERONI_PT_Main"
    
    def draw(self,context):
       layout = self.layout
        
class BOP1(BlenderOniPanel,bpy.types.Panel):
    bl_label="Other"
    bl_idname="BLENDERONI_PT_1"
    bl_parent_id="BLENDERONI_PT_Main"
    
    def draw(self,context):
        layout=self.layout
        sc=context.scene

        #OTHERS
        box = layout.box()
        row = box.row()
        row.prop(sc,"intendedRotMode_BKRM",text="")
        #row = box.row()
        #row.prop(sc,"intendedConversionOperation_BKRM",text="Operation")
        row = box.row(align=True)
        row.prop(sc, "BKRM_startFrame",text="Start:")
        row.prop(sc, "BKRM_endFrame",text="End:")
        row = box.row()
        row.operator("data.bake_object_rotation_mode",text= "Bake Object Rotation Mode", icon="LIGHT_DATA")
        row = box.row()
        row.operator("data.bake_bone_rotation_mode",text= "Bake Bone Rotation Mode", icon="BONE_DATA")
        
        box = layout.box()
        row = box.row()
        row.prop(sc,"intendedRotMode_CRM",text="")
        row = box.row()
        row.operator("data.object_rotation_mode_changer",text="Change Object Rotation Mode", icon="ORIENTATION_GIMBAL")  
        row = box.row()
        row.operator("data.bone_rotation_mode_changer",text="Change Bone Rotation Mode", icon="BONE_DATA") 
        
        box = layout.box()
        row = box.row()
        #row.label(text = "Adjust Throw Target")
        '''row = box.row()
        row.prop(sc, "TA_rotation",text="Rotate by 180 degrees")
        row = box.row()
        row.prop(sc, "TA_revert",text="Revert back throw")'''
        #row=row.box()
        row.prop(sc,"TA_operation",text="")
        row=box.row(align=True)
        row.prop(sc, "TA_startFrame",text="Start:")
        row.prop(sc, "TA_endFrame",text="End:")
        row=box.row(align=True)
        row.prop(sc, "TA_x",text="X:")
        row.prop(sc, "TA_y",text="Y:")
        row.prop(sc, "TA_z",text="Z:")
        row = box.row()
        row.operator("data.throw_adjuster",text="Adjust Throw Target",icon="FILE_REFRESH")

class BOP2(BlenderOniPanel,bpy.types.Panel):
    bl_label="Constraint Switches"
    bl_idname="BLENDERONI_PT_2"
    bl_parent_id="BLENDERONI_PT_Main"
    
    def draw(self,context):
        layout=self.layout
        
        #CONSTRAINT SWITCHES
        row=layout.row()
        row.operator("data.object_constraint_enabler",text="Object Constraint Switch", icon="CONSTRAINT")
        row=layout.row()
        row.operator("data.bone_constraint_enabler",text="Bone Constraint Switch", icon="CONSTRAINT_BONE")

class BOP3(BlenderOniPanel,bpy.types.Panel):
    bl_label="Visual Transformers"
    bl_idname="BLENDERONI_PT_3"
    bl_parent_id="BLENDERONI_PT_Main"
    
    def draw(self,context):
        layout=self.layout
        sc=context.scene
        
        #VISUAL TRANSFORMERS
        #row = layout.row()
        #row.prop(sc,"intendedConversionOperation_VT",text="Operation")
        row=layout.row(align=True)
        row.prop(sc, "VT_startFrame",text="Start:")
        row.prop(sc, "VT_endFrame",text="End:")
        row=layout.row()
        row.operator("data.visual_transformer_object",text="Object Visual Transformer",icon="OBJECT_DATA")
        row=layout.row()
        row.operator("data.visual_transformer_bone",text="Bone Visual Transformer",icon="BONE_DATA")
        
class BOP4(BlenderOniPanel,bpy.types.Panel):
    bl_label="Constraint Setters"
    bl_idname="BLENDERONI_PT_4"
    bl_parent_id="BLENDERONI_PT_Main"
    
    def draw(self,context):
        layout=self.layout
        sc=context.scene
        
        #CONSTRAINT TARGET SETTERS
        
        box = layout.box()
        row=box.row(align=True)
        row.label(text="Target rig name:")
        row.prop(sc, "OCTS_rigName",text="")
        row=box.row()
        row.operator("data.object_constraint_target_setter",text="Set Object Constraint Targets",icon="TRACKER")

        box = layout.box()
        row=box.row()
        row.label(text = "Target rig name:")
        row.prop(sc, "RBCTS_rigName",text="")
        row=box.row()
        row.label(text = "Bone constraints' suffix / Target objects' suffix:")
        row=box.row(align=True)
        row.prop(sc, "RBCTS_constraintSuffix",text="")
        row.prop(sc, "RBCTS_targetSuffix",text="")
        row=box.row()
        row.operator("data.rig_bone_constraint_target_setter",text="Set Rig Bone Constraint Targets",icon="BONE_DATA")

        box = layout.box()
        row=box.row(align=True)
        row.label(text="Character model suffix:")
        row.prop(sc, "CMC_modelSuffix",text="")
        row=box.row(align=True)
        row.label(text="Target rig name:")
        row.prop(sc, "CMC_rigName",text="")
        row=box.row(align=True)
        row.operator("data.character_model_constrainer",text="Constrain Character Model",icon="CONSTRAINT")

class BakeObjectRotationMode_Operator(bpy.types.Operator):
        bl_idname="data.bake_object_rotation_mode"
        bl_label="Bake Keyframe Rotation Mode"
        bl_description="Bake keyframes of the selected objects in the specified frame range and rotation mode.\nUse in Object mode"
        
        def execute(self,context):
            #print(bpy.context.scene.BQK_start_frame)
            #bpy.ops.mesh.primitive_cube_add()
            
            sc=bpy.context.scene

            start=sc.BKRM_startFrame
            end=sc.BKRM_endFrame

            objs=bpy.context.selected_objects

            for i in range(start,end+1):
                sc.frame_set(i)
                for obj in objs:
                    tmp=obj.rotation_mode
                    obj.rotation_mode=sc.intendedRotMode_BKRM#"QUATERNION"
                    bpy.ops.anim.keyframe_insert_menu(type="Rotation")
                    obj.rotation_mode=tmp#"XYZ"
            return{"FINISHED"}
        
class BakeBoneRotationMode_Operator(bpy.types.Operator):
    bl_idname="data.bake_bone_rotation_mode"
    bl_label="Bake Bone Rotation Mode"
    bl_description="Bake keyframes of the selected bones in the specified frame range and rotation mode.\nUse in Pose mode"
    def execute(self,context):
        #print(bpy.context.scene.BQK_start_frame)
        #bpy.ops.mesh.primitive_cube_add()
        
        sc=bpy.context.scene

        start=sc.BKRM_startFrame
        end=sc.BKRM_endFrame

        bones=bpy.context.selected_pose_bones_from_active_object

        for i in range(start,end+1):
            sc.frame_set(i)
            for bone in bones:
                tmp=bone.rotation_mode
                bone.rotation_mode=sc.intendedRotMode_BKRM#"QUATERNION"
                bpy.ops.anim.keyframe_insert_menu(type="Rotation")
                bone.rotation_mode=tmp#"XYZ"
        return{"FINISHED"}

class ObjectRotationModeChanger_Operator(bpy.types.Operator):
        bl_idname="data.object_rotation_mode_changer"
        bl_label="Object Rotation Mode Changer"
        bl_description="Change rotation mode of selected objects to the specified rotation mode.\nUse in Object mode"

        def execute(self,context):
            sc=bpy.context.scene

            objects=bpy.context.selected_objects

            rot_mode=sc.intendedRotMode_CRM#XYZ or QUATERNION

            for obj in objects:
                obj.rotation_mode=rot_mode
            return{"FINISHED"}

class BoneRotationModeChanger_Operator(bpy.types.Operator):
        bl_idname="data.bone_rotation_mode_changer"
        bl_label="Bone Rotation Mode Changer"
        bl_description="Change rotation mode of selected bones to the specified rotation mode.\nUse in Object mode"
        
        def execute(self,context):
            sc=bpy.context.scene

            bones=bpy.context.selected_pose_bones_from_active_object

            rot_mode=sc.intendedRotMode_CRM#XYZ or QUATERNION

            for bone in bones:
                bone.rotation_mode=rot_mode
            return{"FINISHED"}
                                
class ObjectConstraintEnabler_Operator(bpy.types.Operator):
    bl_idname="data.object_constraint_enabler"
    bl_label="Object Constraint Enabler"
    bl_description="Switch on and off object constraints within selected objects\nUse in Object mode"

    def execute(self,context):
        #ObjectConstraintEnabler
        body_parts = bpy.context.selected_objects  #All selected objects

        #Search all objects in body parts for the first object with constraint.
        for part in body_parts: 
            if len(part.constraints)>0: 
                if part.constraints[0].mute==0: #At this point, check if the first constraint in the bone is enabled or disabled...
                    value=1 #...and set the value as invertion of that
                else:
                    value=0
                break #Break the loop as we just need the first mute value we will run into
            
        for body_part in body_parts:
            for con in body_part.constraints:
                con.mute = value
        return{"FINISHED"}

class BoneConstraintEnabler_Operator(bpy.types.Operator):
    bl_idname="data.bone_constraint_enabler"
    bl_label="Bone Constraint Enabler"
    bl_description="Switch on and off bone constraints within selected armature bones.\nUse in Pose mode"
    
    def execute(self,context):
        body_part = bpy.context.selected_pose_bones_from_active_object #All bones in the rig
        #Search all bones in body parts for the first bone with constraint.
        for bone in body_part: 
            if len(bone.constraints)>0: 
                if bone.constraints[0].mute==0: #At this point, check if the first constraint in the bone is enabled or disabled...
                    value=1 #...and set the value as invertion of that
                else:
                    value=0
                break #Break the loop as we just need the first mute value we will run into   
            
        for bone in body_part:
            for con in bone.constraints:
                con.mute = value
        return{"FINISHED"}

#ORIGINAL ObjectConstraintTargetSetter_Operator
'''class ObjectConstraintTargetSetter_Operator(bpy.types.Operator):
    bl_idname="data.object_constraint_target_setter"
    bl_label="Object Constraint Target Setter"
    bl_description="Set the target armature for the selected objects by specifying the suffix of the rig.\nNOTE: The target rig is always assumed to have 'rig' at the start of its name"

    def execute(self,context):
        scene = bpy.context.scene
        objects = bpy.context.selected_objects

        suffix=scene.OCTS_suffix

        for obj in objects:
            for con in obj.constraints:
                if "rig" in con.target.name:
                    con.target.name="rig"+suffix
        return{"FINISHED"}'''
    
class ObjectConstraintTargetSetter_Operator(bpy.types.Operator):
    bl_idname="data.object_constraint_target_setter"
    bl_label="Object Constraint Target Setter"
    bl_description="Set the target armature for the selected objects by specifying the object name of the rig.\nUse in Object mode"

    def execute(self,context):
        scene = bpy.context.scene
        selObjects = bpy.context.selected_objects
        objects = bpy.data.objects
        rig_name=scene.OCTS_rigName

        for obj in selObjects:
            name = str(obj)
            if "pelvis" in name:
                obj.constraints["Copy Location"].target = objects[rig_name]
            obj.constraints["Copy Rotation"].target = objects[rig_name]

        return{"FINISHED"}

class RigBoneConstraintTargetSetter_Operator(bpy.types.Operator):
    bl_idname="data.rig_bone_constraint_target_setter"
    bl_label="Rig Bone Constraint Target Setter"
    bl_description="Set the Target Objects for the specified Bone Constraints of the specified target Rig by providing their suffixes.\nNOTE: The target rig is always assumed to have 'rig' at the start of its name.\nCan be used in both Object and Pose mode"
    
    def execute(self,context):
        #RigBoneConstraintTargetSetter
        obj = bpy.data.objects
        sc=bpy.context.scene
        #SET THIS DEPENDING ON WHICH POSE YOU ARE GOING TO USE
        constraintSuffix=sc.RBCTS_constraintSuffix
        targetSuffix=sc.RBCTS_targetSuffix
        rigName=sc.RBCTS_rigName

        armature = bpy.data.objects[rigName]

        #copying location
        armature.pose.bones["torso"].constraints['Copy Location'+constraintSuffix].target=obj['mid'+targetSuffix]
        armature.pose.bones["torso_pivot"].constraints['Copy Location'+constraintSuffix].target=obj['pelvis'+targetSuffix]

        #copying rotation
        #Torso
        armature.pose.bones["hips"].constraints['Copy Rotation'+constraintSuffix].target=obj['pelvis'+targetSuffix]
        armature.pose.bones["tweak_spine.001"].constraints['Copy Rotation'+constraintSuffix].target=obj['mid'+targetSuffix]
        armature.pose.bones["chest"].constraints['Copy Rotation'+constraintSuffix].target=obj['chest'+targetSuffix]
        armature.pose.bones["shoulder.R"].constraints['Copy Rotation'+constraintSuffix].target=obj['right_shoulder'+targetSuffix]
        armature.pose.bones["shoulder.L"].constraints['Copy Rotation'+constraintSuffix].target=obj['left_shoulder'+targetSuffix]
        armature.pose.bones["neck"].constraints['Copy Rotation'+constraintSuffix].target=obj['neck'+targetSuffix]
        armature.pose.bones["head"].constraints['Copy Rotation'+constraintSuffix].target=obj['head'+targetSuffix]

        #Arms
        armature.pose.bones["upper_arm_fk.L"].constraints['Copy Rotation'+constraintSuffix].target=obj['left_biceps'+targetSuffix]
        armature.pose.bones["upper_arm_fk.R"].constraints['Copy Rotation'+constraintSuffix].target=obj['right_biceps'+targetSuffix]
        armature.pose.bones["forearm_fk.L"].constraints['Copy Rotation'+constraintSuffix].target=obj['left_wrist'+targetSuffix]
        armature.pose.bones["forearm_fk.R"].constraints['Copy Rotation'+constraintSuffix].target=obj['right_wrist'+targetSuffix]
        armature.pose.bones["hand_fk.L"].constraints['Copy Rotation'+constraintSuffix].target=obj['left_handfist'+targetSuffix]
        armature.pose.bones["hand_fk.R"].constraints['Copy Rotation'+constraintSuffix].target=obj['right_handfist'+targetSuffix]

        #Legs
        armature.pose.bones["thigh_fk.L"].constraints['Copy Rotation'+constraintSuffix].target=obj['left_thigh'+targetSuffix]
        armature.pose.bones["thigh_fk.R"].constraints['Copy Rotation'+constraintSuffix].target=obj['right_thigh'+targetSuffix]
        armature.pose.bones["shin_fk.L"].constraints['Copy Rotation'+constraintSuffix].target=obj['left_calf'+targetSuffix]
        armature.pose.bones["shin_fk.R"].constraints['Copy Rotation'+constraintSuffix].target=obj['right_calf'+targetSuffix]
        armature.pose.bones["foot_fk.L"].constraints['Copy Rotation'+constraintSuffix].target=obj['left_foot'+targetSuffix]
        armature.pose.bones["foot_fk.R"].constraints['Copy Rotation'+constraintSuffix].target=obj['right_foot'+targetSuffix]
        return{"FINISHED"}

class VisualTransformerObject_Operator(bpy.types.Operator):
    bl_idname="data.visual_transformer_object"
    bl_label="Visual Transformer for Objects"
    bl_description = "Apply Visual Transformation for selected objects and bake their keyframes within the specified frame range.\nUse in Object mode"
    
    def execute(self,context):
        sc = bpy.context.scene
        start = sc.VT_startFrame
        end = sc.VT_endFrame

        sc.frame_set(start) #set start frame
        for i in range(start, end+1): #loop for every frame
            sc.frame_set(i)
            sc.frame_set(i)
            sc.frame_set(i)
            sc.frame_set(i)
            bpy.ops.object.visual_transform_apply()
            bpy.ops.anim.keyframe_insert_menu(type='BUILTIN_KSI_LocRot')
        return{"FINISHED"}

class VisualTransformerBone_Operator(bpy.types.Operator):
    bl_idname="data.visual_transformer_bone"
    bl_label="Visual Transformer for Bones"
    bl_description = "Apply Visual Transformation for selected bones and bake their keyframes within the specified frame range.\nUse in Pose mode"

    def execute(self,context):
        sc = bpy.context.scene
        start = sc.VT_startFrame
        end = sc.VT_endFrame

        scene = bpy.context.scene

        scene.frame_set(start) #set start frame
        for i in range(start, end+1): #loop for every frame
            scene.frame_set(i)
            scene.frame_set(i)
            scene.frame_set(i)
            scene.frame_set(i)
            bpy.ops.pose.visual_transform_apply()
            bpy.ops.anim.keyframe_insert_menu(type='BUILTIN_KSI_LocRot')
        return{"FINISHED"}

class ThrowAdjuster_Operator(bpy.types.Operator):
    bl_idname="data.throw_adjuster"
    bl_label="Throw Adjuster"
    bl_description="Adjust the position and rotation of the Target model for the specified time range.\nGiven the tag: <Position>X Y Z</Position>,\nthe XYZ values above should be X, -Z, -Y.\nUse in Object mode"
    
    def execute(self,context):
        obj = bpy.context.active_object
        sc = bpy.context.scene

        def add_object_offset_about_cursor_Z(object,x,y,z): #Translation function
            worldZero = Vector((0.0,0.0,0.0))
            #cursor_loc = bpy.context.scene.cursor.location #3D Cursor location
            
            mat = (Matrix.Translation(worldZero) @
                Matrix.Translation((x,y,z))) #PositionOffset translation applied
            object.matrix_world = mat @ object.matrix_world #Change applied to object

        def rotate_object_about_cursor_Z(object, degrees): #Rotation function
            worldZero = Vector((0.0,0.0,0.0))
            #cursor_loc = bpy.context.scene.cursor.location #3D Cursor location
            
            mat = (Matrix.Translation(worldZero) @
                Matrix.Rotation(radians(degrees), 4, 'Z') @
                Matrix.Translation(-worldZero)) #Rotation applied
            
            object.matrix_world = mat @ object.matrix_world #Change applied to object

        #BUGGED KEYFRAME-CHECKING FUNCTION, NOT USED BUT MIGHT BE USEFUL IN THE FEATURE
        """def is_keyframe(ob, frame, data_path, array_index=-1):
            if ob is not None and ob.animation_data is not None and ob.animation_data.action is not None:
                for fcu in ob.animation_data.action.fcurves:
                   l if fcu.data_path == data_path:
                        if array_index == -1 or fcu.array_index == array_index:
                            return frame in (p.co.x for p in fcu.keyframe_points)
            return False

        bpy.types.Object.is_keyframe = is_keyframe   """

        #not really sure why those three lines are here, I think they can be left out
        #obj.keyframe_insert(data_path="location", frame = 0)
        #obj.matrix_world.translation += Vector((-100, 0, 0)) 
        #obj.keyframe_insert(data_path="location", frame = 100)
        
        
        X = sc.TA_x
        Y = sc.TA_y
        Z = sc.TA_z
        if sc.TA_operation == 'Adjust':
            if obj.location[0] != 0.0 or obj.location[1] != 0.0:
                X = -sc.TA_x
                Y = -sc.TA_y
                Z = -sc.TA_z
            
        startFrame=sc.TA_startFrame
        for i in range(startFrame, sc.TA_endFrame+1): #loop for every frame
            #if obj.is_keyframe(i, obj.path_from_id("location")): Bugged keyframe-check
            sc.frame_set(i)
            if sc.TA_operation == 'Rotate':
                rotate_object_about_cursor_Z(obj, 180) #rotate object
            add_object_offset_about_cursor_Z(obj,X,Y,Z) #translate object
            obj.keyframe_insert(data_path="rotation_euler", frame=i) #keyframe rotation
            obj.keyframe_insert(data_path="location", frame=i) #keyframe location
        
        '''if sc.TA_operation == 'Rotate':
            sc.frame_set(sc.TA_startFrame) #set start frame
            for i in range(sc.TA_startFrame, sc.TA_endFrame): #loop for every frame
                #if obj.is_keyframe(i, obj.path_from_id("location")): Bugged keyframe-check
                    sc.frame_set(i)
                    rotate_object_about_cursor_Z(obj, 180) #rotate object
                    add_object_offset_about_cursor_Z(obj,sc.TA_x,sc.TA_y,sc.TA_z) #translate object
                    obj.keyframe_insert(data_path="rotation_euler", frame=i) #keyframe rotation
                    obj.keyframe_insert(data_path="location", frame=i) #keyframe location
        else:
            sc.frame_set(sc.TA_startFrame)
            zeroPosition=False #bool to check if the the object should have its location adjusted by the offset positive or negative
            if obj.location[0] == 0.0 and obj.location[1] == 0.0:
                zeroPosition=True #object at first frame is at {X,Y} = {0,0} so we have add positive offset
            else:
                zeroPosition=False #object at first frame is at {X,Y} different than {0,0}, so that means we have to add a negative offset     
            
            if zeroPosition==True:
                for i in range(sc.TA_startFrame, sc.TA_endFrame): #loop for every frame
                    #if obj.is_keyframe(i, obj.path_from_id("location")): Bugged keyframe-check
                    sc.frame_set(i)
                    add_object_offset_about_cursor_Z(obj,sc.TA_x,sc.TA_y,sc.TA_z) #translate object
                    obj.keyframe_insert(data_path="rotation_euler", frame=i) #keyframe rotation
                    obj.keyframe_insert(data_path="location", frame=i) #keyframe location
            else:
                sc.frame_set(sc.TA_startFrame)
                obj.location[0]=0.0
                obj.location[1]=0.0
                add_object_offset_about_cursor_Z(obj,0,0,-sc.TA_z) #translate object
                obj.keyframe_insert(data_path="rotation_euler", frame=sc.TA_startFrame) #keyframe rotation
                obj.keyframe_insert(data_path="location", frame=sc.TA_startFrame) #keyframe location
                for i in range(sc.TA_startFrame+1, sc.TA_endFrame): #loop for every frame
                    #if obj.is_keyframe(i, obj.path_from_id("location")): Bugged keyframe-check
                    sc.frame_set(i)
                    add_object_offset_about_cursor_Z(obj,-sc.TA_x,-sc.TA_y,-sc.TA_z) #translate object
                    obj.keyframe_insert(data_path="rotation_euler", frame=i) #keyframe rotation
                    obj.keyframe_insert(data_path="location", frame=i) #keyframe location'''


        return{"FINISHED"}

class CharacterModelConstrainer(bpy.types.Operator):
    bl_idname="data.character_model_constrainer"
    bl_label="Character Model Constrainer"
    bl_description="Constrain Oni character model with the specified object name suffix to the specified rig"
    
    def execute(self,context):
        objects = bpy.data.objects
        sc = bpy.context.scene
        suffix = sc.CMC_modelSuffix
        rig = objects[sc.CMC_rigName]
        objs = ["pelvis","mid","chest","neck","head",
            "left_shoulder","left_biceps","left_wrist","left_handfist",
            "left_thigh","left_calf","left_foot",
            "right_shoulder","right_biceps","right_wrist","right_handfist",
            "right_thigh","right_calf","right_foot"]

        hasConstraints=False
        for obj in objs:
            if len(objects[obj+suffix].constraints) > 0:
                hasConstraints=True
                break

        if hasConstraints == False:
            
            objects['pelvis'+suffix].constraints.new(type='COPY_LOCATION')
            objects['pelvis'+suffix].constraints['Copy Location'].target=rig
            objects['pelvis'+suffix].constraints['Copy Location'].subtarget='ORG-spine'
            
            bones = ["ORG-spine","ORG-spine.001","ORG-spine.002","ORG-spine.003","ORG-spine.004",
                "ORG-shoulder.L","ORG-upper_arm.L","ORG-forearm.L","ORG-hand.L",
                "ORG-thigh.L","ORG-shin.L","ORG-foot.L",
                "ORG-shoulder.R","ORG-upper_arm.R","ORG-forearm.R","ORG-hand.R",
                "ORG-thigh.R","ORG-shin.R","ORG-foot.R"]
            axisCorrections = ["ACPelvis","ACSpine","ACSpine","ACSpine","ACSpine",
                "ACLimbs","ACLimbs","ACLimbs","ACHandL",
                "ACLimbs","ACLimbs","ACFeet",
                "ACLimbs","ACLimbs","ACLimbs","ACHandR",
                "ACLimbs","ACLimbs","ACFeet"]
            for obj in objs:
                objects[obj+suffix].constraints.new(type='COPY_ROTATION')
                objects[obj+suffix].constraints['Copy Rotation'].target=rig
                objects[obj+suffix].constraints['Copy Rotation'].subtarget=bones[objs.index(obj)]
                objects[obj+suffix].constraints['Copy Rotation'].euler_order='ZYX'
                objects[obj+suffix].constraints['Copy Rotation'].mix_mode='REPLACE'
                
                objects[obj+suffix].constraints.new(type='COPY_ROTATION')
                objects[obj+suffix].constraints['Copy Rotation.001'].target=objects[axisCorrections[objs.index(obj)]]
                objects[obj+suffix].constraints['Copy Rotation.001'].mix_mode='AFTER'     
            
            return{"FINISHED"}
                
        else:
            self.report({"ERROR"}, "Objects of the specified character model already have constraints, please clear all of them first")
            return {"CANCELLED"}
        
        

classes = (BOP_Main,BOP1,BOP2,BOP3,BOP4,
    BakeObjectRotationMode_Operator, 
    BakeBoneRotationMode_Operator, 
    ObjectRotationModeChanger_Operator,
    BoneRotationModeChanger_Operator,
    BoneConstraintEnabler_Operator, 
    ObjectConstraintEnabler_Operator,
    ObjectConstraintTargetSetter_Operator, 
    RigBoneConstraintTargetSetter_Operator,
    VisualTransformerObject_Operator, 
    VisualTransformerBone_Operator,
    ThrowAdjuster_Operator,
    CharacterModelConstrainer)

def register():
    for cls in classes:
        bpy.utils.register_class(cls)
        
    bpy.types.Scene.intendedRotMode_BKRM = bpy.props.EnumProperty(
        name = "Intended Rotation Mode",
        description = "Intended rotation mode in which selected objects will have their keyframes baked",
        items=(
            ('QUATERNION',"Quaternion (WXYZ)",""),
            ('XYZ',"XYZ Euler",""),
            ('XZY',"XZY Euler",""),
            ('YXZ',"YXZ Euler",""),
            ('YZX',"YZX Euler",""),
            ('ZXY',"ZXY Euler",""),
            ('XYZ',"XYZ Euler",""),
            ('ZYX',"ZYX Euler",""),
            ('AXIS_ANGLE',"Axis Angle","")
        ),
        default='QUATERNION'
    )
    
    bpy.types.Scene.intendedRotMode_CRM = bpy.props.EnumProperty(
        name = "Intended Rotation Mode",
        description = "Intended rotation mode for the selected objects",
        items=(
            ('QUATERNION',"Quaternion (WXYZ)",""),
            ('XYZ',"XYZ Euler",""),
            ('XZY',"XZY Euler",""),
            ('YXZ',"YXZ Euler",""),
            ('YZX',"YZX Euler",""),
            ('ZXY',"ZXY Euler",""),
            ('XYZ',"XYZ Euler",""),
            ('ZYX',"ZYX Euler",""),
            ('AXIS_ANGLE',"Axis Angle","")
        ),
        default='XYZ'
    )

    '''bpy.types.Scene.intendedConversionOperation_BKRM = bpy.props.EnumProperty(
        name = "Intended Operation",
        items=(
            ('CONVERT',"Convert existing keyframes",""),
            ('BAKE',"Bake all frames","")
        ),
        default='CONVERT'
    )'''
    
    bpy.types.Scene.BKRM_startFrame = bpy.props.IntProperty(
        name = "Start frame",
        description = "Start frame for baking",
        default = 0,
    )
    
    bpy.types.Scene.BKRM_endFrame = bpy.props.IntProperty(
        name = "End frame",
        description = "End frame for baking",
        default = 100
    )
    
    bpy.types.Scene.OCTS_rigName = bpy.props.StringProperty(
        name = "Name of the target rig object",
        description = "Name of constraint target rig of the selected objects",
        default = "rig"
    )
    
    bpy.types.Scene.RBCTS_rigName = bpy.props.StringProperty(
        name = "Name of the target rig object",
        description = "Name of the armature object on which changes will be made",
        default = "rig"
    )
    
    bpy.types.Scene.RBCTS_constraintSuffix = bpy.props.EnumProperty(
        name = "Bone constraints' suffix",
        description = "Suffix of rig's bone constraints on which changes will be made",
        items=(
            ('.001',".001",""),
            ('.002',".002","")
        ),
        default='.001'
    )
    #ALTERNATIVE DEFINITION OF RBCTS_constraintSuffix PROPERTY
    '''bpy.types.Scene.RBCTS_constraintSuffix = bpy.props.StringProperty(
        name = "Rig's bone constraints' suffix",
        description = "Suffix of rig's bone constraints on which changes will be made.\nNOTE: This is supposed to be either .001 or .002",
        default = ".001"
    )'''
    bpy.types.Scene.RBCTS_targetSuffix = bpy.props.StringProperty(
        name = "Target objects' suffix",
        description = "Suffix of objects to which the specified rig's bone constraints will be targeted.\nNOTE: Leave blank if there is no suffix",
        default = ".001"
    )


    bpy.types.Scene.VT_startFrame = bpy.props.IntProperty(
        name = "Visual Transformer start frame",
        description = "Start frame for the Visual Transformer",
        default=0
    )

    bpy.types.Scene.VT_endFrame = bpy.props.IntProperty(
        name = "Visual Transformer end frame",
        description = "End frame for the Visual Transformer",
        default=100
    )
    
    #TO BE WORKED ON IN NEXT VERSION
    '''bpy.types.Scene.intendedConversionOperation_VT = bpy.props.EnumProperty(
        name = "Intended Operation",
        items=(
            ('CONVERT',"Transform existing keyframes",""),
            ('BAKE',"Bake all frames","")
        ),
        default='CONVERT'
    )'''

    bpy.types.Scene.TA_operation = bpy.props.EnumProperty(
        name = "Throw Target Adjuster Operation",
        items = (
            ('Rotate',"Adjust and rotate forward throw target",
                "Add location offset and rotate a throw target by 180 degrees, use for forward throws"),
            ('Adjust',"Adjust back throw target",
                "Add location offset to a throw target, use for back throws")
            #('Adjust',"Adjust back throw target",
                #"Add location offset to a back throw"),
            #('Revert',"Invert a back throw target",
                #"Add an inverted location offset to a back throw")
        ),
        default='Rotate'
    )
    
    '''bpy.types.Scene.TA_rotation = bpy.props.BoolProperty(
        name="Throw Adjuster Rotation Bool",
        description="Set this if you wish to rotate the target by 180 degrees (i.e. use this if you're dealing with/making a forward throw, uncheck if it's a back throw)",
        default=True
    )
    
    bpy.types.Scene.TA_revert = bpy.props.BoolProperty(
        name="Throw Adjuster Revert Bool",
        description="Set this if you're dealing with a back throw and adjusting the target back to 0,0,0 (works only when Rotate by 180 degrees is unchecked)",
        default=False
    )'''
    
    bpy.types.Scene.TA_startFrame = bpy.props.IntProperty(
        name = "Visual Transformer start frame",
        description = "Start frame for the Throw Target Adjuster",
        default=0
    )

    bpy.types.Scene.TA_endFrame = bpy.props.IntProperty(
        name = "Visual Transformer end frame",
        description = "End frame for the Throw Target Adjuster",
        default=100
    )

    bpy.types.Scene.TA_x = bpy.props.FloatProperty(
        name = "Blender X",
        description = "Blender X, Oni X",
        default=-0.98142
    )

    bpy.types.Scene.TA_y = bpy.props.FloatProperty(
        name = "Blender Y",
        description = "Blender Y, Oni -Z",
        default=-11.8147
    )

    bpy.types.Scene.TA_z = bpy.props.FloatProperty(
        name = "Blender Z",
        description = "Blender Z, Oni -Y",
        default=0
    )
    
    bpy.types.Scene.CMC_modelSuffix = bpy.props.StringProperty(
        name = "Suffix of the character model objects",
        description = "Suffix of the character model objects to be constrained to the specified rig.\nNOTE: Leave blank if there is no suffix",
        default = ""
    )    
    
    bpy.types.Scene.CMC_rigName = bpy.props.StringProperty(
        name = "Name of the target rig object",
        description = "Name of the target rig to which the specified character model will be constrained",
        default = "rig"
    )

def unregister():
    #bpy.utils.unregister_class(BlenderOniPanel)
    for cls in classes:
        bpy.utils.unregister_class(cls)
    
    del bpy.types.Scene.BKRM_startFrame
    del bpy.types.Scene.BKRM_endFrame
    del bpy.types.Scene.intendedRotMode_CRM
    del bpy.types.Scene.intendedRotMode_BKRM
    #del bpy.types.Scene.intendedConversionOperation_BKRM
    #del bpy.types.Scene.intendedConversionOperation_VT
    del bpy.types.Scene.OCTS_rigName
    del bpy.types.Scene.RBCTS_constraintSuffix
    del bpy.types.Scene.RBCTS_targetSuffix
    del bpy.types.Scene.RBCTS_rigName
    del bpy.types.Scene.VT_startFrame
    del bpy.types.Scene.VT_endFrame
    del bpy.types.Scene.TA_operation
    #del bpy.types.Scene.TA_rotation
    #del bpy.types.Scene.TA_revert
    del bpy.types.Scene.TA_startFrame
    del bpy.types.Scene.TA_endFrame
    del bpy.types.Scene.TA_x
    del bpy.types.Scene.TA_y
    del bpy.types.Scene.TA_z
    del bpy.types.Scene.CMC_modelSuffix
    del bpy.types.Scene.CMC_rigName
    


if __name__ == "__main__":
    register()

