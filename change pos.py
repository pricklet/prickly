# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 10:50:40 2020

@author: SCE
"""


from mcpi.minecraft import Minecraft
import time

mc=Minecraft.create()

time.sleep(5)

x,y,z=mc.player.getTilePos()

mc.player.setTilePos(x,y,z)
y+=5
time.sleep(2)

mc.player.setTilePos(x,y,z)
y+=5
time.sleep(2)

mc.player.setTilePos(x,y,z)
y+=5
time.sleep(2)

mc.player.setTilePos(x,y,z)
y+=5
time.sleep(2)

mc.player.setTilePos(x,y,z)
y+=5
time.sleep(2)


mc.player.setTilePos(x,y,z)
y+=5
time.sleep(2)


mc.player.setTilePos(x,y,z)
y+=5
time.sleep(2)


mc.player.setTilePos(x,y,z)
y+=5
time.sleep(2)

