import maya.cmds as cmds

if not cmds.commandPort(':4434', query=True):
    cmds.commandPort(name=':4434')

cmds.rename('nurbsSphere1', 'Arm_#_Jnt')