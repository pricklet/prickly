# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 10:50:40 2020

@author: SCE
"""


from mcpi.minecraft import Minecraft
mc=Minecraft.create()
t=0

while True:
    x,y,z=mc.player.getTilePos()
    mc.postToChat('You are located on x:'+
                  str(x)+',y:'+str(y)+',z:'+str(z))
