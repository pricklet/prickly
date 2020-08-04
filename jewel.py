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

mc.setBlocks(x+50,y-1,z+50,x-50,y-1,z-50,57)

mc.setBlocks(x+50,y+50,z+50,x-50,y-1,z-50,0)