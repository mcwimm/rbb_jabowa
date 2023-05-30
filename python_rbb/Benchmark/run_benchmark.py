#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@date: 2023-Today
@author: https://github.com/mcwimm
"""

import matplotlib.pyplot as plt
import os
import sys
import inspect


currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

from jabowa import Jabowa

j = Jabowa(b2=48.04, b3=.172, max_growth=162, max_dbh=140, max_height=3500, initial_dbh=10,
           time_step_length=3600*24*365.25)

time_steps = 100
plt.ion()
#fig = plt.figure()  # make a figure
fig, (ax1, ax2, ax3) = plt.subplots(3, sharex=True)

#plt.axis([0, time_steps, 10, 140])
#plt.axis([0, time_steps, 10, 3500])

x = list()
y = list()
for timestep in range(time_steps):
    # print(timestep)
    j.updateGeometry(f_resources=0.9, f_competition=1.0)
    output = j.getOutput()
    # x.append(timestep)
    # y.append(output)
    # print(output)

    ax1.scatter(timestep, output["height"], s=1, c="#000")
    ax1.set(ylabel="Tree height")
    ax2.scatter(timestep, output["dbh"], s=1, c="#000")
    ax2.set(ylabel="Tree dbh")
    ax3.scatter(timestep, output["growth"], s=1, c="#000")
    ax3.set(ylabel="Tree growth", xlabel="Year")
    plt.show()
    plt.pause(0.001)

