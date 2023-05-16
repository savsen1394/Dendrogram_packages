from astrodendro import Dendrogram
import numpy as np
import random
import matplotlib.pyplot as plt
from astropy.io import fits
from astropy import wcs



image,header = fits.getdata('../fits_files/improved_13co/hf02072_13co21_ftbase_0p5kms.fits', header = True)
wcs=wcs.WCS(header)
pix_size = header['CDELT2']
pix_size_arcsec = 3600*pix_size
telescope_ang_resol_350 = 15
pix_wise_resol = telescope_ang_resol_350 / pix_size_arcsec

d = Dendrogram.compute(image,min_value=3.0,min_delta = 0.5,min_npix=pix_wise_resol, verbose=False,wcs = wcs)

v = d.viewer()
v.show()

#changing parameters
d = Dendrogram.compute(image,min_value=3.0,min_delta = 0.7,min_npix=pix_wise_resol, verbose=False)

v = d.viewer()
v.show()

#changing parameters
d = Dendrogram.compute(image,min_value=3.0,min_delta = 1.5,min_npix=pix_wise_resol, verbose=False)

v = d.viewer()
v.show()

