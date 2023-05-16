import random
import matplotlib.pyplot as plt
from astropy.io import fits
from astropy.wcs import WCS
from astropy import wcs
from astrodendro import Dendrogram
from astrodendro import Dendrogram, ppv_catalog
from astrodendro.analysis import PPVStatistic




image,header = fits.getdata('../fits_files/improved_13co/hf02072_13co21_ftbase_0p5kms.fits', header = True)
wcs = WCS(header)


#with proper units
from astropy import units as u
metadata={}
metadata['data_unit'] = u.K
metadata['wcs'] = wcs
metadata['velocity_scale']=u.km/u.s
metadata['wavelength'] = 220.398e+9*u.Hz
metadata['spatial_scale'] = 3*u.arcsec
metadata['beam_major'] = 18*u.arcsec 
metadata['beam_minor']= 18*u.arcsec

d = Dendrogram.compute(image, min_value=3.0, min_delta=0.5, min_npix=3, verbose=True)
v = d.viewer()
v.show()

stat = PPVStatistic(d.trunk[0],metadata = metadata)


#making a catalogue

cat = ppv_catalog(d, metadata)
cat.pprint(show_unit = True, max_lines =10)

#cat.write('temp_3d_fil_stat.csv')  


cat.write('../tables/integrated_temperature_catalogue.csv')  

