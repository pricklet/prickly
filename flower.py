# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 10:50:40 2020

@author: SCE
"""


from mcpi.minecraft import Minecraft
import time

mc=Minecraft.create()

while True:
    x,y,z = mc.player.getTilePos()
    mc.setBlock(x,y,z,8)
    mc.setBlock(x,y,z,19)
    time.sleep(5)