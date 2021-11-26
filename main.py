import numpy as np
import Chromaticity.Color as Color
import Chromaticity.Database as Db

if __name__ == '__main__':
	wl_source, D_65, A = np.loadtxt('D65_A_data.dat', unpack = True)
	D_65_spectra = Color.Color_processing(data_range = wl_source, data_value = D_65)
	D_65_spectra.calc_color_values()
	print(D_65_spectra.XYZ)
	print(D_65_spectra.xy)
	print(D_65_spectra.xyY)
	print(D_65_spectra.sRGB)
	print(D_65_spectra.adobeRGB)

	print('------')
	data_D65 = Db.D65_standart()
	D_65_spectra = Color.Color_processing(data_range = data_D65[:,0], data_value = data_D65[:,1])
	D_65_spectra.calc_color_values()
	print(D_65_spectra.XYZ)
	print(D_65_spectra.xy)
	print(D_65_spectra.xyY)
	print(D_65_spectra.sRGB)
	print(D_65_spectra.adobeRGB)
