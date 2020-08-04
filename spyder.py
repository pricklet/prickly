# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 10:50:40 2020

@author: SCE
"""
from mcpi.minecraft import Minecraft

mc = Minecraft.create()

x,y,z = mc.player.getTilePos()

block = int(input("請問你想放的方塊ID是甚麼?"))

mc.setBlock(x,y,z,block)
