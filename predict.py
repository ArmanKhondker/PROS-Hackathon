"""
Uses model from research.py to predict optimal price
"""
import pickle
import pandas as pd

model = pickle.load(open('prediction_model.sav', 'rb'))

def encode_brand(brand):
	brand_dict = {'brand_Epson': 0, 'brand_Nikon': 0, 'brand_HP': 0, 'brand_Samsung': 0,
	'brand_Panasonic': 0, 'brand_Sigma': 0, 'brand_Sanyo': 0, 'brand_Agfa': 0, 'brand_JVC': 0,
	'brand_Olympus': 0, 'brand_Pentax': 0, 'brand_Kodak': 0, 'brand_Ricoh': 0, 'brand_Casio': 0,
	'brand_Contax': 0, 'brand_Toshiba': 0, 'brand_Sony': 0, 'brand_Fujifilm': 0, 'brand_Leica': 0,
	'brand_Canon': 0, 'brand_Kyocera': 0}

	brand_string = 'brand_' + brand
	if brand_string in brand_dict:
		brand_dict[brand_string] = 1
	else:
		print 'Error: Brand not found'
		return

	return brand_dict

def boost_predict(model,brand,date,max_res,low_res,pixels,zoom_w,zoom_t,normal_focus,macro_focus,storage,weight,dimensions):
	d = {'Release date' : date, 'Max resolution' : max_res, 'Low resolution': low_res, 'Effective pixels': pixels,
	'Zoom wide (W)': zoom_w, 'Zoom tele (T)': zoom_t, 'Normal focus range': normal_focus, 'Macro focus range': macro_focus,
	'Storage included': storage, 'Weight': weight, 'Dimensions' : dimensions}
	encoded_brand = encode_brand(brand)
	d.update(encoded_brand)
	X = pd.DataFrame(d, index=[0])

	y = model.predict(X).round(2)

	return y