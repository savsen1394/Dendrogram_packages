# overplotting of calculated statistical quantities and the original plots
from astropy.io import fits

from astrodendro import Dendrogram
from astrodendro.analysis import PPStatistic

import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse

hdu = fits.open('original_wave_250_90_pix.fits')[0]
print(hdu.header)
d = Dendrogram.compute(hdu.data, min_value=1.0, min_delta=1., min_npix=6)
p = d.plotter() # provides a non-interactive plotting tool to plot the dendogram.


fig = plt.figure() #adding figure plot
ax = fig.add_subplot(1, 1, 1) # defining a subplot no.1 of 1x1 gridding

# adding the fits data to our subplot figure, interpolation generally makes the
# image look better by preserving the resolution and in this context we can avoid
# this.
ax.imshow(hdu.data, origin='lower', interpolation = 'nearest', cmap=plt.cm.Blues,vmax = 6) 

for leaf in d.leaves: # d.leaves will make an array of all the leaves present in d

    p.plot_contour(ax, structure=leaf, colors='red') # to draw red contours indicating leaves

    s = PPStatistic(leaf)
    ellipse = s.to_mpl_ellipse(edgecolor='orange', facecolor='none') # using the statistics (major and minor axis) of the leaf ellipses of orange colour edge is made.

    ax.add_patch(ellipse) # ellipses are added or patched to the defined figure

ax.set_xlim(0, 91) #xlimit
ax.set_ylim(0, 91) # ylimnit
plt.show()


