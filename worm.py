
from mcpi.minecraft import Minecraft
mc = Minecraft.create()
x,y,z = mc.player.getTilePos()

number = 1

for i in range(8):
    
    for j in range(number):
        mc.spawnEntity(x,y,z,60)
        
    mc.postToChat('這次生成了'+str(number)+'隻蠹魚')
        
    number*= 2