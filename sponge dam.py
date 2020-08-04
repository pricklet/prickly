# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 10:50:40 2020

@author: SCE
"""
from mcpi.minecraft import Minecraft

mc = Minecraft.create()

x,y,z = mc.player.getTilePos()


a = 0
while a<5:
    mc.setBlocks(x-10,y-1,z,x+10,y-20,z,19)
    a = a+1
    z = z+5