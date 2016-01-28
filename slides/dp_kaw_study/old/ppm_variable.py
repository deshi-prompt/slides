#!/usr/bin/ipython

from matplotlib.pyplot import *
from numpy import *

# user settings
mode = 1
is_savefig = True


# code
margin = 0.5 # [msec]
period = 1.5 # [msec]
#cycle  = 30 # [times]
fig, ax = subplots(1,1)
#fig = figure()
#ax = fig.add_axes()

if mode == 1 :
    cycle = 30 # [times]
elif mode == 2 :
    cycle =  2 # [times]

t = arange(-margin,period * cycle + margin,0.01)
theta = t / period * pi

if mode == 1 :
  figbasename = "ppm_variable"
  num = len(t)
  ax.plot(t[      0:num  /3]-0.25,(sign(sin(theta[      0:num  /3])-0.50) + 1.0) / 2.0 * 5.0, color='k')
  ax.plot(t[num  /3:num*2/3]-0.00,(sign(sin(theta[num  /3:num*2/3])+0.00) + 1.0) / 2.0 * 5.0, color='k')
  ax.plot(t[num*2/3:num    ]+0.25,(sign(sin(theta[num*2/3:num    ])+0.50) + 1.0) / 2.0 * 5.0, color='k')
  ax.set_ylim(-5.0,10.0)
elif mode == 2 :
  figbasename = "ppm_whole"
  ax.plot(t-0.25, (sign(sin(theta) - 0.50) + 1.0) / 2.0 * 5.0, 'k--')
  ax.plot(t-0.00, (sign(sin(theta) + 0.00) + 1.0) / 2.0 * 5.0, 'k-')
  ax.plot(t+0.25, (sign(sin(theta) + 0.50) + 1.0) / 2.0 * 5.0, 'k--')
  ax.set_ylim(-1.0,6.0)

ax.set_xlim(t.min(),t.max())
#ax.set_ylim(-5.0,10.0)

ax.set_xlabel("time [msec]")
ax.set_ylabel("voltage [V]")

if is_savefig :
  fig.savefig(u"./fig/" + figbasename + '.svg')
  fig.savefig(u"./fig/" + figbasename + '.png')

#fig.show()
show()


