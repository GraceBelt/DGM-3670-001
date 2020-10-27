import maya.cmds as cmds

if not cmds.commandPort(':4434', query=True):
    cmds.commandPort(name=':4434')

cmds.polySphere(name='Sphere_Geo',
                subdivisionsHeight=20,
                subdivisionsAxis=32)

print (cmds.polySphere('Sphere_Geo', name=True, subdivisionsHeight=True))