import random
import matplotlib.pyplot as plt
from astropy.io import fits
from astropy.wcs import WCS
from astropy import wcs
from astrodendro import Dendrogram




#image = fits.getdata('PerA_Extn2MASS_F_Gal.fits')
data, header = fits.getdata('original_wave_250_90_pix.fits', header = True)
print(header)
wcs = WCS(header)
# Herschel beamsize is 18"while the pixel size here is 3" ence we should take
# np_pixel = 6
d = Dendrogram.compute(data, min_value=2.0, min_delta=2., min_npix=6, verbose=True)
v = d.viewer()
#v..show()

#strcuure statistics

print('STATISTICS RELATED TO THE LEAVES:')
from astrodendro.analysis import PPStatistic
print(d.trunk[0].children[0].children[0].children[0])
stat = PPStatistic(d.trunk[0].children[0].children[0].children[0])
print('major axis:',stat.major_sigma)
print('minor axix:',stat.minor_sigma)
print('position angle:',stat.position_angle)

#with proper units
from astropy import units as u
metadata={}
metadata['data_unit'] = u.Jy / u.beam
metadata['spatial_scale'] = 3*u.arcsec
metadata['beam_major'] = 18*u.arcsec 
metadata['beam_minor']= 18*u.arcsec
stat = PPStatistic(d.trunk[0].children[0].children[0].children[0],metadata = metadata)
print('major axis:',stat.major_sigma)
print('minor axix:',stat.minor_sigma)
print('position angle:',stat.position_angle)
#print('flux:',stat.flux)

print('THE CATALOGUE:')
#making a catalogue
from astrodendro import Dendrogram, pp_catalog
cat = pp_catalog(d, metadata)
cat.pprint(show_unit = True, max_lines =10)
