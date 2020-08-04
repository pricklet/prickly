# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 10:50:40 2020

@author: SCE
"""


from mcpi.minecraft import Minecraft
import time
import random

mc=Minecraft.create()

time.sleep(5)

color = random.randrange(16)

a = 0

while a<50:
    a = a+1
    x,y,z = mc.player.getTilePos()
    mc.setBlock(x,y,z,38,color)
    time.sleep(0.2)