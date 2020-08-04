# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 10:50:40 2020

@author: SCE
"""


from mcpi.minecraft import Minecraft

mc=Minecraft.create()

x=-289
y=88
z=218

mc.player.setTilePos(x,y,z)
