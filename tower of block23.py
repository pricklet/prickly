# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 10:50:40 2020

@author: SCE
"""


from mcpi.minecraft import Minecraft
import time
mc=Minecraft.create()

x,y,z=mc.player.getTilePos()
time.sleep(5)

mc.setBlock(x,y-1,z,100,1)
time.sleep(1)
mc.setBlock(x,y,z+1,100,1)
time.sleep(1)
mc.setBlock(x+1,y,z+1,100,1)
time.sleep(1)
mc.setBlock(x+1,y,z,100,1)
time.sleep(1)
mc.setBlock(x+1,y,z-1,100,1)
time.sleep(1)
mc.setBlock(x,y,z-1,100,1)
time.sleep(1)
mc.setBlock(x-1,y,z-1,100,1)
time.sleep(1)
mc.setBlock(x-1,y,z,100,1)
time.sleep(1)
mc.setBlock(x-1,y,z+1,100,1)
time.sleep(1)
