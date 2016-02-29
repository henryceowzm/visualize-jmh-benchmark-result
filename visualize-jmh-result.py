#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as py
x,a,b,c=np.genfromtxt('dateformats-chart.csv',unpack=True)
py.scatter(x,a)
py.scatter(x,b)
py.scatter(x,c)
py.plot(x,a)
py.plot(x,b)
py.plot(x,c)
py.show()

