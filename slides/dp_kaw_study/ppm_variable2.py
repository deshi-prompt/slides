#!/usr/bin/ipython

from matplotlib.pyplot import *
from numpy import *

# user settings
mode = 4
is_savefig = True


# code
margin =   2 # [msec]
period =  20 # [msec]
#cycle  = 30 # [times]
fig, ax = subplots(1,1)
#fig = figure()
#ax = fig.add_axes()

if mode == 1 :
    cycle = 10 # [times]
elif mode == 2 :
    cycle = 1.5 # [times]
elif mode == 3 :
    cycle = 0.3 # [times]
elif mode == 4 :
    period = 1 # [msec]
    cycle = 10 # [times]


t = arange(-margin,period * cycle + margin,0.01)
theta = t / period * 2 * pi

if mode == 1 :
  figbasename = "ppm_variable"
  num = len(t)
  ax.plot(t[      0:num  /3]-4.50,(sign(sin(theta[      0:num  /3])-0.988) + 1.0) / 2.0 * 5.0, color='k')
  ax.plot(t[num  /3:num*2/3]-4.25,(sign(sin(theta[num  /3:num*2/3])-0.973) + 1.0) / 2.0 * 5.0, color='k')
  ax.plot(t[num*2/3:num    ]-4.00,(sign(sin(theta[num*2/3:num    ])-0.952) + 1.0) / 2.0 * 5.0, color='k')
  ax.set_ylim(-5.0,10.0)
  ax.set_xlim(t.min(),t.max() - 4.0)
elif mode == 2 :
  print theta
  figbasename = "ppm_period"
  ax.plot(t-4.50, (sign(sin(theta)  - 0.988) + 1.0) / 2.0 * 5.0, 'k--')
  ax.plot(t-4.25, (sign(sin(theta)  - 0.973) + 1.0) / 2.0 * 5.0, 'k-')
  ax.plot(t-4.00, (sign(sin(theta)  - 0.952) + 1.0) / 2.0 * 5.0, 'k--')
  ax.set_ylim(-1.0,6.0)
  ax.set_xlim(t.min(),t.max() - 4.0)
elif mode == 3 :
  figbasename = "ppm_edge"
  ax.plot(t-4.50, (sign(sin(theta)  - 0.988) + 1.0) / 2.0 * 5.0, 'k--')
  ax.plot(t-4.25, (sign(sin(theta)  - 0.973) + 1.0) / 2.0 * 5.0, 'k-')
  ax.plot(t-4.00, (sign(sin(theta)  - 0.952) + 1.0) / 2.0 * 5.0, 'k--')
  ax.set_ylim(-1.0,6.0)
  ax.set_xlim(t.min(),t.max() - 4.0)
elif mode == 4 :
  voltage = 6.6
  #ratio = 0.2
  #ratio = 0.5
  #ratio = 0.7
  ratio = 1.0000
  figbasename = "pwm_" + str(voltage) + "v_" + str(ratio)
  x_offset = pi * (ratio - 0.5)
  y_offset = sin(x_offset)
  if y_offset > 0.999:
      y_offset = 1.05

  y = (sign(sin(theta) + y_offset) + 1.0) / 2.0 * voltage
  ax.plot(t, y, 'k-')
  y_ave = ones(len(y))*average(y)
  ax.plot(t, y_ave, 'r-')
  ax.set_ylim(-1.0, ceil(voltage + 1.0))
  ax.set_xlim(t.min(),t.max() - 4.0)

#ax.set_ylim(-5.0,10.0)

ax.set_xlabel("time [msec]")
ax.set_ylabel("voltage [V]")

if is_savefig :
  fig.savefig(u"./fig/" + figbasename + '.svg')
  fig.savefig(u"./fig/" + figbasename + '.png')

#fig.show()
show()


