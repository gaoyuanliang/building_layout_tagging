########building_layout_tagging.py########
from pavi import *

model = load_build_image_categorization_model(
	model_file = 'building_layout.h5py')

def building_layout_tagging(input_file):
	output = {}
	x = read_image_from_local(input_file)
	x = xception.preprocess_input(x)
	x = numpy.array([x])
	x = base_model_Xception.predict(x)
	y_score = model.predict(x)
	prediction = numpy.argmax(y_score)
	score = numpy.max(y_score)
	output["score"] = score
	if prediction > 0:
		output["tag"] = 'building_layout'
	else:
		output["tag"] = 'non_building_layout'  
	return output
########building_layout_tagging.py########
