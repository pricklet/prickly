# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 10:50:40 2020

@author: SCE
"""


from mcpi.minecraft import Minecraft
import time
import random

mc=Minecraft.create()

x,y,z=mc.player.getTilePos()

time.sleep(5)

width =15
height = 10
length =25

block = 5
air = 0

mc.setBlocks(x,y,z,x+length,y+height,z+width,block)
mc.setBlocks(x+1,y+1,z+1,x+length-1,y+height-1,z+width-1,air)