#!/usr/bin/env python
import numpy as np

try:
    # for Python2
    import Tkinter as tkinter 
except ImportError:
    # for Python3
    import tkinter

def clear_text():
	for e in entries_list:
		e.delete(0, 'end')

	iment= ""
	ment.set(iment)
	iment1= ""
	ment1.set(iment1)
	iment2= ""
	ment2.set(iment2)
	iment3= ""
	ment3.set(iment3)
	iment4= ""
	ment4.set(iment4)
	iment5= ""
	ment5.set(iment5)
	iment6= ""
	ment6.set(iment6)
	iment7= ""
	ment7.set(iment7)

def client_exit():
		exit()

def func(x, a, b):
    	return a * np.exp(-b * x)

def estimate_iron():
	import pandas as pd
	import scipy
	from scipy import optimize
	import matplotlib.pyplot as plt

	TE_list = []
	ROI_list = []
	n= echos_value.get()

	for i in range(1, n + 1):
		te_temp= globals()['te_value%s' % i]
		roi_temp= globals()['roi_value%s' % i]
		TE_list.append(te_temp.get())
		ROI_list.append(roi_temp.get())
	
	x= np.array(TE_list)
	y= np.array(ROI_list)
	

	popt, pcov = scipy.optimize.curve_fit(func, x,  y,  p0=(150, 0.009241962))
	#so= scipy.optimize.curve_fit(lambda t,a,b: a*numpy.exp(b*t),  x,  y,  p0=(150, 0.009241962))
	#print(so[0][1])
	T2 = 1/popt[1]
	R2 = 1000/T2
	LIC = (-454.85+(28.02*R2))/1000

	res= "LIC= {0:.2f}mg/g".format(LIC)
	path1 = path.get()
	plt.scatter(x, y, label='data')
	plt.plot(x, y, 'g-')
	plt.plot(TE_list, func(x, *popt), 'r--',label='fit: a=%5.3f, b=%5.3f' % tuple(popt))
	plt.xlabel('TE')
	plt.ylabel('ROI')
	plt.legend()
	plt.text(min(x),min(y),res, color='red', fontsize=15)
	plt.savefig(path1)
	iment= "DONE!"
	ment.set(iment)

	iment1= res
	ment1.set(iment1)

	res4= "T2*= {0:.2f}ms".format(T2)
	res5= "R2*= {0:.2f}Hz".format(R2)
	res6= "LIC= {0:.2f}mg/g".format(LIC)

	iment5= res4
	ment5.set(iment5)
	iment6= res5
	ment6.set(iment6)
	iment7= res6
	ment7.set(iment7)

	#T2 result
	if T2 > 11.4:
		res1= "Normal"
	elif T2 <= 11.4 and T2 > 3.8:
		res1= "Leve"
	elif T2 <= 3.8 and T2 > 1.8:
		res1= "Moderado"
	else:
		res1= "Severo"

	iment2= res1
	ment2.set(iment2)

	#R2 result
	if R2 < 88:
		res2= "Normal"
	elif R2 >= 88 and R2 < 263:
		res2= "Leve"
	elif R2 >= 263 and R2 < 555:
		res2= "Moderado"
	else:
		res2= "Severo"

	iment3= res2
	ment3.set(iment3)

	#LIC result
	if LIC < 2:
		res3= "Normal"
	elif LIC >= 2 and LIC < 7:
		res3= "Leve"
	elif LIC >= 7 and LIC < 15:
		res3= "Moderado"
	else:
		res3= "Severo"

	iment4= res3
	ment4.set(iment4)

	return



root = tkinter.Tk()
root.title('MRI Iron Estimation')
#root.configure(background="gray")

btn1= tkinter.Button(root, text= "  # RUN! #  ", command= estimate_iron)
btn1.pack()
btn1.grid(row= 0, column= 3)


btn2= tkinter.Button(root, text= "Exit", command= client_exit)
btn2.pack()
btn2.grid(row= 19, column= 3)

btn3 = tkinter.Button(root, text='Clear', command= clear_text)
btn3.pack()
btn3.grid(row= 18, column= 3)

l1= tkinter.Label(root, text= "Number of echoes")
l1.grid(row= 0, column= 1)

l2= tkinter.Label(root, text= "File name (.png) and path (/Users/)")
l2.grid(row= 1, column= 1)

ln1= tkinter.Label(root, text= '1')
ln1.grid(row= 3, column= 0)

ln2= tkinter.Label(root, text= '2')
ln2.grid(row= 4, column= 0)

ln3= tkinter.Label(root, text= '3')
ln3.grid(row= 5, column= 0)

ln4= tkinter.Label(root, text= '4')
ln4.grid(row= 6, column= 0)

ln5= tkinter.Label(root, text= '5')
ln5.grid(row= 7, column= 0)

ln6= tkinter.Label(root, text= '6')
ln6.grid(row= 8, column= 0)

ln7= tkinter.Label(root, text= '7')
ln7.grid(row= 9, column= 0)

ln8= tkinter.Label(root, text= '8')
ln8.grid(row= 10, column= 0)

ln9= tkinter.Label(root, text= '9')
ln9.grid(row= 11, column= 0)

ln10= tkinter.Label(root, text= '10')
ln10.grid(row= 12, column= 0)

ln11= tkinter.Label(root, text= '11')
ln11.grid(row= 13, column= 0)

ln12= tkinter.Label(root, text= '12')
ln12.grid(row= 14, column= 0)

ln13= tkinter.Label(root, text= '13')
ln13.grid(row= 15, column= 0)

ln14= tkinter.Label(root, text= '14')
ln14.grid(row= 16, column= 0)

ln15= tkinter.Label(root, text= '15')
ln15.grid(row= 17, column= 0)

ln16= tkinter.Label(root, text= '16')
ln16.grid(row= 18, column= 0)

# define entries

echos_value= tkinter.IntVar()
ev= tkinter.Entry(root, textvariable= echos_value)
ev.grid(row= 0, column= 2)

path= tkinter.StringVar()
dir_path= tkinter.Entry(root, textvariable= path)
dir_path.grid(row= 1, column= 2)

ment= tkinter.StringVar()
iment = tkinter.Label(root, textvariable=ment)
iment.grid(row= 1, column= 3)

ment1= tkinter.StringVar()
iment1 = tkinter.Label(root, textvariable=ment1)
iment1.grid(row= 2, column= 3)

l2= tkinter.Label(root, text= "TE")
l2.grid(row= 2, column= 1)

l3= tkinter.Label(root, text= "ROI")
l3.grid(row= 2, column= 2)


te_value1= tkinter.DoubleVar()
roi_value1= tkinter.DoubleVar()
te1= tkinter.Entry(root, textvariable= te_value1)
te1.grid(row= 3, column= 1)

roi1= tkinter.Entry(root, textvariable= roi_value1)
roi1.grid(row= 3, column= 2)

te_value2= tkinter.DoubleVar()
roi_value2= tkinter.DoubleVar()
te2= tkinter.Entry(root, textvariable= te_value2)
te2.grid(row= 4, column= 1)

roi2= tkinter.Entry(root, textvariable= roi_value2)
roi2.grid(row= 4, column= 2)

te_value3= tkinter.DoubleVar()
roi_value3= tkinter.DoubleVar()
te3= tkinter.Entry(root, textvariable= te_value3)
te3.grid(row= 5, column= 1)

roi3= tkinter.Entry(root, textvariable= roi_value3)
roi3.grid(row= 5, column= 2)

te_value4= tkinter.DoubleVar()
roi_value4= tkinter.DoubleVar()
te4= tkinter.Entry(root, textvariable= te_value4)
te4.grid(row= 6, column= 1)

roi4= tkinter.Entry(root, textvariable= roi_value4)
roi4.grid(row= 6, column= 2)

te_value5= tkinter.DoubleVar()
roi_value5= tkinter.DoubleVar()
te5= tkinter.Entry(root, textvariable= te_value5)
te5.grid(row= 7, column= 1)

roi5= tkinter.Entry(root, textvariable= roi_value5)
roi5.grid(row= 7, column= 2)

te_value6= tkinter.DoubleVar()
roi_value6= tkinter.DoubleVar()
te6= tkinter.Entry(root, textvariable= te_value6)
te6.grid(row= 8, column= 1)

roi6= tkinter.Entry(root, textvariable= roi_value6)
roi6.grid(row= 8, column= 2)

te_value7= tkinter.DoubleVar()
roi_value7= tkinter.DoubleVar()
te7= tkinter.Entry(root, textvariable= te_value7)
te7.grid(row= 9, column= 1)

roi7= tkinter.Entry(root, textvariable= roi_value7)
roi7.grid(row= 9, column= 2)

te_value8= tkinter.DoubleVar()
roi_value8= tkinter.DoubleVar()
te8= tkinter.Entry(root, textvariable= te_value8)
te8.grid(row= 10, column= 1)

roi8= tkinter.Entry(root, textvariable= roi_value8)
roi8.grid(row= 10, column= 2)

te_value9= tkinter.DoubleVar()
roi_value9= tkinter.DoubleVar()
te9= tkinter.Entry(root, textvariable= te_value9)
te9.grid(row= 11, column= 1)

roi9= tkinter.Entry(root, textvariable= roi_value9)
roi9.grid(row= 11, column= 2)

te_value10= tkinter.DoubleVar()
roi_value10= tkinter.DoubleVar()
te10= tkinter.Entry(root, textvariable= te_value10)
te10.grid(row= 12, column= 1)

roi10= tkinter.Entry(root, textvariable= roi_value10)
roi10.grid(row= 12, column= 2)

te_value11= tkinter.DoubleVar()
roi_value11= tkinter.DoubleVar()
te11= tkinter.Entry(root, textvariable= te_value11)
te11.grid(row= 13, column= 1)

roi11= tkinter.Entry(root, textvariable= roi_value11)
roi11.grid(row= 13, column= 2)

te_value12= tkinter.DoubleVar()
roi_value12= tkinter.DoubleVar()
te12= tkinter.Entry(root, textvariable= te_value12)
te12.grid(row= 14, column= 1)

roi12= tkinter.Entry(root, textvariable= roi_value12)
roi12.grid(row= 14, column= 2)

l4= tkinter.Label(root, text= "Valor do T2*")
l4.grid(row= 15, column= 1)
l5= tkinter.Label(root, text= "Valor do R2*")
l5.grid(row= 16, column= 1)
l6= tkinter.Label(root, text= "Valor do LIC")
l6.grid(row= 17, column= 1)

ment5= tkinter.StringVar()
iment5 = tkinter.Label(root, textvariable=ment5)
iment5.grid(row= 15, column= 2)

ment6= tkinter.StringVar()
iment6 = tkinter.Label(root, textvariable=ment6)
iment6.grid(row= 16, column= 2)

ment7= tkinter.StringVar()
iment7 = tkinter.Label(root, textvariable=ment7)
iment7.grid(row= 17, column= 2)


ment2= tkinter.StringVar()
iment2 = tkinter.Label(root, textvariable=ment2)
iment2.grid(row= 15, column= 3)

ment3= tkinter.StringVar()
iment3 = tkinter.Label(root, textvariable=ment3)
iment3.grid(row= 16, column= 3)

ment4= tkinter.StringVar()
iment4 = tkinter.Label(root, textvariable=ment4)
iment4.grid(row= 17, column= 3)

entries_list = [ev, dir_path, te1, roi1, te2, roi2, te3, roi3, te4, roi4, te5, roi5, te6, roi6, te7, roi7, te8, roi8, te9, roi9, te10, roi10, te11, roi11, te12, roi12]

root.mainloop() 
