# -*- coding: utf-8 -*-
#"""""""""""""""""""""""""""""""""""
"""Created on Tue Oct 29 19:07:20 2019
"""
"""Author: Tony Amos 
#"""""""""""""""""""""""""""""""""""
#
import numpy as np
import matplotlib.pyplot as plt
#
x = np.linspace(0, 3*np.pi, 500)
plt.plot(x, np.sin(x**2))
plt.title('A simple chirp done by Tony Amos')
plt.show()
#
#