#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from library.psalter import psalm1
from pylatex import *

geometry_options = {"tmargin": "1cm", "lmargin": "5cm"}
doc = Document(geometry_options=geometry_options)
doc.add_color("red","red","red")
with doc.create(Section('Psalm 1')):
    psalm1.splitlines()
    for line in (psalm1):
        doc.append(line+'\n')
#import hologion
#import trop/kontaks

doc.generate_pdf('full', clean_tex=False)

#import pylatex

#normal beginning

#psalter(83)
#psalter(84)
#psalter(85)
#G/B, Alle x3, Kyrie x3
#if two, first tropar
#G
#tropar
#B
#Theotokion
#trisagion through pater noster
#kontakion (after 6th ode at matins if two)
#Kyrie x40
#prayer of the hours
#kyriex3, g/b, hore honorable, through the
#9th hour by st basil

