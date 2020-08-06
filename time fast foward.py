
from mcpi.minecraft import Minecraft
from time import sleep
mc = Minecraft.create()
x,y,z = mc.player.getTilePos()

while True:
    mc.executeCommand('time add 100')
    sleep(0.05)
