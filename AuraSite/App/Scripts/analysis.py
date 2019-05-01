#!/usr/bin/python3

import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('Agg')				# for preventing local thread error
import matplotlib.pyplot as plt
import openpyxl


def analyse(report):

	file_path = "/home/jatin/Aura-Project/AuraSite/App/Uploads/" + str(report)
	file_upload = open(file_path,'rb') 		# open the file in new data object and then load into the function
	book = openpyxl.load_workbook(filename=file_upload)
	sheet_name11 = book.get_sheet_names()[0]		# data_type = string

	#print(type(sheet_name))				list
	#print(type(sheet_name[0]))				string

	data_frame = pd.read_excel(file_upload,sheet_name = sheet_name11)

	final_result =[]

	#-------------------------------------------------------------------------------------------------------------
	# to find the name
	title = data_frame.columns.values[2]
	#print(type(title))			string

	temp_names = title.split()

	person_name=""
	for i in range(3,len(temp_names)):
		person_name = person_name + str(temp_names[i]) + " "
	#print(person_name)																			#IMP
	final_result.append(person_name)

	report_date = temp_names[0]																	#IMP
	final_result.append(report_date)

	#--------------------------------------------------------------------------------------------------------------

	# Report Values

	emotional_pressure = data_frame.iloc[2,2]
	#print(type(emotional_pressure))			#float											#IMP
	final_result.append(emotional_pressure)

	energy = data_frame.iloc[3,2]
	#print(energy)								#float											# IMP (in J)
	final_result.append(energy)

	symmetry = data_frame.iloc[4,2]
	#print(symmetry)							#float											# IMP
	final_result.append(symmetry)


	organ = data_frame.iloc[5,2]
	#print(organ)								#float											# IMP
	final_result.append(organ)

	entropy = data_frame.iloc[6,2]
	#print(entropy)								#float											# IMP
	final_result.append(entropy)

	form = data_frame.iloc[7,2]
	#print(form)								#float											# IMP
	final_result.append(form)


	#--------------------------------------------------------------------------------------------------------------

	# Graph Analysis

	chakra_values = data_frame.iloc[22:29,1:3]
	chakra_symm =  data_frame.iloc[40:47,1:3]
	yin_values = data_frame.iloc[55:64,1:3]

	chakra_values1 = chakra_values.values.tolist()
	chakra_symm1 = chakra_symm.values.tolist()
	yin_values1 = yin_values.values.tolist()


	# allocating the values in the corresponding list
	values=[]
	x1=[]
	asymm=[]
	x2=[]
	yin_yang_values=[]
	yin_yang_x1=[]

	for i in range(0,len(chakra_values1)):
		values.append(chakra_values1[i][1])
		x1.append(chakra_values1[i][0])

	for i in range(0,len(chakra_symm1)):
		asymm.append(chakra_symm1[i][0])
		x2.append(chakra_symm1[i][1])

	for i in range(0,len(yin_values1)):
		yin_yang_values.append(yin_values1[i][1])
		yin_yang_x1.append(yin_values1[i][0])



	# plotting the first graph

	plt.figure(1)
	plt.title('Values')
	plt.xlabel('chakras')
	plt.ylabel('values')

	# allocating the colors to the each chakra
	chakra_color=['red', 'orange', 'yellow', 'green', 'azure', 'blue', 'violet']

	bars = plt.bar( x1, values, 0.6, color=chakra_color)
	for bar in bars:
		y_val = bar.get_height()
		plt.text(bar.get_x() + 0.1, y_val + 0.1, y_val)

	plt.axis([-1,7,0,8])
	figure = plt.gcf()
	figure.set_size_inches(10,6)
	plt.savefig('/home/jatin/Aura-Project/AuraSite/App/static/analysis_img/chakra_values.png')
	final_result.append('/home/jatin/Aura-Project/AuraSite/App/static/analysis_img/chakra_values.png')

	# plotting the second graph

	plt.figure(2)
	plt.title('Asymmetry')
	plt.xlabel('chakras')
	plt.ylabel('asymmetric values')

	plt.plot( x2, asymm, 'ro', markersize=20)
	plt.plot([0.0,0.0],[-0.5,6.5], 0.1,color='blue')

	plt.plot([-1.9,1.9],[6.0,6.0], 0.1, color='blue')
	plt.plot([-1.9,1.9],[5.0,5.0], 0.05, color='blue')
	plt.plot([-1.9,1.9],[4.0,4.0], 0.05, color='blue')
	plt.plot([-1.9,1.9],[3.0,3.0], 0.05, color='blue')
	plt.plot([-1.9,1.9],[2.0,2.0], 0.05, color='blue')
	plt.plot([-1.9,1.9],[1.0,1.0], 0.05, color='blue')
	plt.plot([-1.9,1.9],[0.0,0.0], 0.05, color='blue')

	plt.axis([-2,2,-1,7])
	#plt.show()
	figure = plt.gcf()
	figure.set_size_inches(11,8)
	plt.savefig('/home/jatin/Aura-Project/AuraSite/App/static/analysis_img/chakra_asymmetry.png')
	final_result.append('/home/jatin/Aura-Project/AuraSite/App/static/analysis_img/chakra_asymmetry.png')


	# plotting the third graph

	plt.figure(3)
	plt.title('Yin_yang Values')
	plt.xlabel('parameters')
	plt.ylabel('Energy')

	# allocating different colors to the bar
	#print(yin_yang_values)
	yin_yang_color=[]
	for i in yin_yang_values:
		if(i<4.0):
			yin_yang_color.append('orange')
		elif(i>6.0):
			yin_yang_color.append('red')
		else:
			yin_yang_color.append('green')
	#print(yin_yang_color)

	bars = plt.bar( ["Heart", "Lungs", "Liver", "Spleen", "Kidneys", "Pericardium", "Small intestine", "Intestine", "Gallbladder" ], yin_yang_values, 0.4, color=yin_yang_color)
	for bar in bars:
		y_val = bar.get_height()
		plt.text(bar.get_x() + 0.05, y_val + 0.1, y_val)

	plt.axis([-0.3,8.3,0,8])
	figure = plt.gcf()
	figure.set_size_inches(11,6)
	plt.savefig('/home/jatin/Aura-Project/AuraSite/App/static/analysis_img/yin_yang_values.png')
	final_result.append('/home/jatin/Aura-Project/AuraSite/App/static/analysis_img/yin_yang_values.png')





	return final_result
