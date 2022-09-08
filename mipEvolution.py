#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 20 11:18:37 2022

PJD 15 Aug 2022     - Updated to reflect latest model and institution counts

@author: durack1
"""

# %% time labels
import matplotlib.pyplot as plt
import numpy as np
import os

# %% chdir
os.chdir("/Users/durack1/sync/Docs/admin/LLNL/22/220426_CMIP-ESALivingPlanetSymposium-May22/images")

# %% demo
# labels = ['G1', 'G2', 'G3', 'G4', 'G5']
# men_means = [20, 34, 30, 35, 27]
# women_means = [25, 32, 34, 20, 25]

# x = np.arange(len(labels))  # the label locations
# width = 0.35  # the width of the bars

# fig, ax = plt.subplots()
# rects1 = ax.bar(x - width/2, men_means, width, label='Men')
# rects2 = ax.bar(x + width/2, women_means, width, label='Women')

# # Add some text for labels, title and custom x-axis tick labels, etc.
# ax.set_ylabel('Scores')
# ax.set_title('Scores by group and gender')
# ax.set_xticks(x, labels)
# ax.legend()

# ax.bar_label(rects1, padding=3)
# ax.bar_label(rects2, padding=3)

# fig.tight_layout()

# plt.show()

# %% MIPs

labels = ['AMIP1', 'AMIP2', 'CMIP1', 'CMIP2', 'CMIP3', 'CMIP5', 'CMIP6']
experiments = [1, 1, 1, 2, 12, 34, 322]
models = [29, 32, 20, 17, 24, 59, 131]
institutions = [28, 25, 16, 15, 16, 26, 49]
countries = [9, 9, 8, 8, 11, 12, 26]

x = np.arange(len(labels))  # the label locations
width = 0.25  # the width of the bars

fig, ax = plt.subplots(figsize=(9, 6), dpi=300)

rects1 = ax.bar(x - width*.5, experiments, width, label='experiments')
rects3 = ax.bar(x - width, models, width, label='models')
rects2 = ax.bar(x + width*.5, institutions, width, label='institutions')
rects4 = ax.bar(x + width, countries, width, label='countries')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Count', fontname="Microsoft Sans Serif", fontsize=14)
#ax.set_yticks(plt.setp(ax.get_yticks(), ax.get_yticklabels(), fontname="Microsoft Sans Serif", fontsize=14))
plt.yticks(fontname="Microsoft Sans Serif", fontsize=14)
ax.set_title('Experiment, Model, Institution and Country counts by *MIP era',
             fontname="Microsoft Sans Serif", fontsize=14)
ax.set_xticks(x, labels, fontname="Microsoft Sans Serif", fontsize=14)
ax.legend(prop={"family": "Microsoft Sans Serif", "size": 14})

padding = 1
labelSize = 12
ax.bar_label(rects1, padding=padding,
             fontname="Microsoft Sans Serif", fontsize=labelSize)
ax.bar_label(rects2, padding=padding,
             fontname="Microsoft Sans Serif", fontsize=labelSize)
ax.bar_label(rects3, padding=padding,
             fontname="Microsoft Sans Serif", fontsize=labelSize)
ax.bar_label(rects4, padding=padding,
             fontname="Microsoft Sans Serif", fontsize=labelSize)

fig.tight_layout()

plt.show()
fig.savefig("220815_MIPEvolution-Counts.png")
plt.close()
