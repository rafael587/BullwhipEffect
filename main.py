# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 3.10.1-368-g19bcc292)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################
from numpy import arange, sin, pi
import matplotlib
import csv
import os
import pandas as pd
matplotlib.use('WXAgg')

from datetime import datetime as dt
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas
from matplotlib import pyplot as plt
#from matplotlib.backends.backend_wx import NavigationToolbar2Wx
from matplotlib.figure import Figure
from scipy.stats import spearmanr
from scipy.stats import pearsonr
import wx
import wx.xrc

figuresize=(7.5,3.9)

class Inicial ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 1239,619 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		self.plotData1 = []
		self.plotData2 = []
		self.plot1Name =""
		self.plot2Name =""
		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		gSizer1 = wx.GridSizer( 0, 2, 0, 0 )

		bSizer11 = wx.BoxSizer( wx.VERTICAL )

		bSizer48 = wx.BoxSizer( wx.VERTICAL )

		bSizer48.SetMinSize( wx.Size( 500,60 ) )
		gSizer7 = wx.GridSizer( 0, 2, 0, 0 )

		bSizer51 = wx.BoxSizer( wx.VERTICAL )

		self.m_button24 = wx.Button( self, wx.ID_ANY, u"Listar base", wx.DefaultPosition, wx.Size( 120,50 ), 0 )
		bSizer51.Add( self.m_button24, 0, wx.ALL, 5 )

		self.m_button22 = wx.Button( self, wx.ID_ANY, u"Limpar", wx.DefaultPosition, wx.Size( 120,50 ), 0 )
		bSizer51.Add( self.m_button22, 0, wx.ALL, 5 )

		self.m_button27 = wx.Button( self, wx.ID_ANY, u"Testar", wx.DefaultPosition, wx.Size( 120,50 ), 0 )
		bSizer51.Add( self.m_button27, 0, wx.ALL, 5 )

		self.m_staticText4 = wx.StaticText( self, wx.ID_ANY, u"Selecione a faixa de tempo ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText4.Wrap( -1 )

		bSizer51.Add( self.m_staticText4, 0, wx.ALL, 5 )

		self.m_staticText5 = wx.StaticText( self, wx.ID_ANY, u"em meses a ser testada", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText5.Wrap( -1 )

		bSizer51.Add( self.m_staticText5, 0, wx.ALL, 5 )

		self.m_staticline5 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer51.Add( self.m_staticline5, 0, wx.EXPAND |wx.ALL, 5 )

		gSizer71 = wx.GridSizer( 0, 2, 0, 0 )

		self.m_slider3 = wx.Slider( self, wx.ID_ANY, 5, 5, 100, wx.DefaultPosition, wx.DefaultSize, wx.SL_HORIZONTAL )
		gSizer71.Add( self.m_slider3, 0, wx.ALL, 5 )

		self.m_staticText6 = wx.StaticText( self, wx.ID_ANY, u"5", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText6.Wrap( -1 )

		gSizer71.Add( self.m_staticText6, 0, wx.ALL, 5 )


		bSizer51.Add( gSizer71, 1, wx.EXPAND, 5 )


		gSizer7.Add( bSizer51, 1, wx.EXPAND, 5 )

		bSizer52 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"Dados Disponíveis", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )

		bSizer52.Add( self.m_staticText1, 0, wx.ALL, 5 )

		m_checkList1Choices = []
		self.m_checkList1 = wx.CheckListBox( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_checkList1Choices, 0 )
		bSizer52.Add( self.m_checkList1, 1, wx.ALL|wx.EXPAND, 5 )


		gSizer7.Add( bSizer52, 1, wx.EXPAND, 5 )


		bSizer48.Add( gSizer7, 1, wx.EXPAND, 5 )


		bSizer11.Add( bSizer48, 1, wx.EXPAND, 5 )


		gSizer1.Add( bSizer11, 1, wx.EXPAND, 5 )

		bSizer12 = wx.BoxSizer( wx.VERTICAL )

		sbSizer4 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Índice 1" ), wx.VERTICAL )

		self.m_button7 = wx.Button( sbSizer4.GetStaticBox(), wx.ID_ANY, u"Preencher", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer4.Add( self.m_button7, 0, wx.ALL, 5 )

		self.sbSizer6 = wx.StaticBoxSizer( wx.StaticBox( sbSizer4.GetStaticBox(), wx.ID_ANY, u"" ), wx.VERTICAL )


		sbSizer4.Add( self.sbSizer6, 1, wx.EXPAND, 5 )


		bSizer12.Add( sbSizer4, 1, wx.EXPAND, 5 )

		sbSizer5 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Índice 2" ), wx.VERTICAL )

		self.m_button8 = wx.Button( sbSizer5.GetStaticBox(), wx.ID_ANY, u"Preencher", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer5.Add( self.m_button8, 0, wx.ALL, 5 )

		self.sbSizer7 = wx.StaticBoxSizer( wx.StaticBox( sbSizer5.GetStaticBox(), wx.ID_ANY, u"" ), wx.VERTICAL )


		sbSizer5.Add(self.sbSizer7, 1, wx.EXPAND, 5 )


		bSizer12.Add( sbSizer5, 1, wx.EXPAND, 5 )


		gSizer1.Add( bSizer12, 1, wx.EXPAND, 5 )


		self.SetSizer( gSizer1 )
		self.Layout()
		self.m_menubar3 = wx.MenuBar( 0 )
		self.m_menu1 = wx.Menu()
		self.m_menubar3.Append( self.m_menu1, u"Inicio" )

		self.m_menu2 = wx.Menu()
		self.m_menubar3.Append( self.m_menu2, u"Sobre" )

		self.SetMenuBar( self.m_menubar3 )


		self.Centre( wx.BOTH )

		# Connect Events
		self.m_button24.Bind( wx.EVT_BUTTON, self.ListBase )
		self.m_button22.Bind( wx.EVT_BUTTON, self.CleanGraphics )
		self.m_button27.Bind( wx.EVT_BUTTON, self.TestCorrelation )
		self.m_slider3.Bind( wx.EVT_SLIDER, self.m_slider3OnSlider )
		self.m_checkList1.Bind( wx.EVT_CHECKLISTBOX, self.BoxChecked )
		self.m_button7.Bind( wx.EVT_BUTTON, self.FillingButton1 )
		self.m_button8.Bind( wx.EVT_BUTTON, self.FillingButton2 )

	def __del__( self ):
		pass
	def m_slider3OnSlider( self, event ):
		self.m_staticText6.Label = str(self.m_slider3.GetValue())
		event.Skip()
# Virtual event handlers, override them in your derived class
	
	def CleanGraphics( self, event ):
		self.m_button8.Show()
		self.m_button7.Show()
		self.sbSizer7.Clear(True)
		self.sbSizer6.Clear(True)
		self.plotData1.clear()
		self.plotData2.clear()
		event.Skip()

	def TestCorrelation( self, event ):
		if len(self.plotData1) !=0 and len(self.plotData2) !=0:
			CorrelationData=self.returnFormatedData(self.plotData1,self.plotData2)
			movedCorrelation=self.movingCorrelation(CorrelationData,self.m_slider3.GetValue())
			plt.plot(movedCorrelation[0],movedCorrelation[1], color='darkmagenta',linewidth=3)
			plt.xlabel("Anos", size=16)
			plt.ylabel("Correlação", size=16)
			plt.suptitle("Correlação "+self.plot1Name+" x "+self.plot2Name)
			plt.show()
		event.Skip()
	
	def returnFormatedData(self,data1, data2):
		formatedData = [],[],[]
	
		for index1 in range(len(data1[1])):
			for index2 in (range(len(data2[1])) ):
				if (data1[1][index1].month == data2[1][index2].month) and  (data1[1][index1].year == data2[1][index2].year):
					#print(data2[1][index2])
					formatedData[1].append(data1[0][index1])
					formatedData[2].append(data2[0][index2])
					formatedData[0].append(data1[1][index1])
	
		return formatedData


	def movingCorrelation(self, formatedData,wsize):
		movSpearmans = [],[]
		if len(formatedData[1]) < wsize:
			wsize = len(formatedData[1])

		for index in range(len(formatedData[1])):
			dados1teste =[]
			dados2teste =[]
			if (index+wsize) < len(formatedData[1]) :
				for index2 in range(wsize):
					dados1teste.append(formatedData[1][index + index2])
					dados2teste.append(formatedData[2][index + index2])
				corr, _ = pearsonr(dados1teste, dados2teste)   
				movSpearmans[0].append(formatedData[0][index +index2])
				movSpearmans[1].append(corr)
		return movSpearmans
	def FillingButton1( self, event ):
		if len(self.m_checkList1.GetCheckedItems()) !=1:
			return

		data = self.loadData(self.m_checkList1.GetString(self.m_checkList1.GetCheckedItems()[0]))
		self.plot1Name = self.m_checkList1.GetString(self.m_checkList1.GetCheckedItems()[0]).replace(".csv","")
		self.plotData1 = data
	
		x_values2 = data[1]
		y_values2 = data[0]
		self.sbSizer6.Clear()
		self.figure = Figure(figsize=(figuresize))
		self.plot1 = self.figure.add_subplot(111)
		self.plot1.plot(x_values2,y_values2, color='mediumblue',linewidth=3)
		self.canvas = FigureCanvas(self.sbSizer6.GetStaticBox(), -1, self.figure)
		self.sbSizer6.Add(self.canvas)
	
		self.m_button7.Hide()
		event.Skip()

	def FillingButton2( self, event ):
		if len(self.m_checkList1.GetCheckedItems()) !=1:
			return
		data = self.loadData(self.m_checkList1.GetString(self.m_checkList1.GetCheckedItems()[0]))
		self.plot2Name=self.m_checkList1.GetString(self.m_checkList1.GetCheckedItems()[0]).replace(".csv","")
		self.plotData2 = data
		x_values2 = data[1]
		y_values2 = data[0]
		self.sbSizer7.Clear()
		self.figure = Figure(figsize=(figuresize))
		self.plot1 = self.figure.add_subplot(111)
		self.plot1.plot(x_values2,y_values2, color='red',linewidth=3)
		self.canvas = FigureCanvas(self.sbSizer7.GetStaticBox(), -1, self.figure)
		self.sbSizer7.Add(self.canvas)
		self.m_button8.Hide()
		event.Skip()
	
	def BoxChecked( self, event ):
		if len(self.m_checkList1.GetCheckedItems())> 1:
			self.m_checkList1.CheckedItems = []
		event.Skip()
	# Virtual event handlers, override them in your derived class
	def ListBase( self, event ):
	
		self.m_checkList1.Clear()
		for elementyahoo in self.yahooDatas():
			self.m_checkList1.Append(elementyahoo)
			
		for elementfred in self.fredDatas():
			self.m_checkList1.Append(elementfred)
			
		event.Skip()

	
	def fredDatas(self):
		files=[]
		names = os.listdir("fred")
		for name in names:
			if ".csv" in name:
				print(name)
				files.append(name)
		return files
	
	
	def yahooDatas(self):
		files=[]
		names = os.listdir("yahoo")
		for name in names:
			if ".csv" in name:
				print(name)
				files.append(name)
		return files
	
	def createPlot1(self):
		#plot 1
		self.figure = Figure(figsize=(9.5,3.9))
		self.plot1 = self.figure.add_subplot(111)
		self.canvas = FigureCanvas(self.sbSizer6.GetStaticBox(), -1, self.figure)
		self.sbSizer6.Add(self.canvas)
		

	def createPlot2(self):
		#plot 1
		self.figure = Figure(figsize=(9.5,3.9))
		print(self.sbSizer7.GetStaticBox())
		print(wx.HORIZONTAL)
		print(self.sbSizer7.CalcMin().GetWidth(), self.sbSizer7.CalcMin().GetHeight())
		self.plot2 = self.figure.add_subplot(111)
		self.canvas = FigureCanvas(self.sbSizer7.GetStaticBox(), -1, self.figure)
		self.sbSizer7.Add(self.canvas)

	def loadData(self,file):
		data =''
		for elementyahoo in self.yahooDatas():
			if file == elementyahoo :
				filelocation = "yahoo/"+file
				data = self.readCSVYahooFormat(filelocation)
		for elementfred in self.fredDatas():
			if file == elementfred :
				filelocation = "fred/"+file
				data = self.readCSVFredFormat(filelocation)
		monthly = pd.DataFrame({"VALUE": data[0],"DATE":pd.to_datetime(data[1])})
		average = monthly.resample("M",on="DATE").mean()
		
		processdata = average['VALUE'].values.tolist()
		count = 0
		dates =[]
		while count < average.size:
			date_str = str(average.index[count]).split(' ', 1)
			dates.append(dt.strptime(date_str[0], "%Y-%m-%d").date())
			count +=1
		data.clear()
		data = [processdata,dates]
		return data
	
	def ColumNames(self,file):

	# opening the csv file
		with open(file) as csv_file:
	
			# reading the csv file using DictReader
			csv_reader = csv.DictReader(csv_file)
			dict_from_csv = dict(list(csv_reader)[0])
		
			# making a list from the keys of the dict
			list_of_column_names = list(dict_from_csv.keys())
		return list_of_column_names	
	
	def readCSVFredFormat(self,file):
		dates=[]
		value=[]
		listofcolumnnames=self.ColumNames(file)
		with open(file, newline='') as csvfile:
			reader = csv.DictReader(csvfile)
			for row in reader:
				dates.append(row[listofcolumnnames[0]])
				value.append(float(row[listofcolumnnames[1]]))
		dates = [dt.strptime(d, "%Y-%m-%d").date() for d in dates]
		data=[value,dates]
		return(data)
	
	def readCSVYahooFormat(self,file):
		dates=[]
		value=[]
		listofcolumnnames=self.ColumNames(file)
		with open(file, newline='') as csvfile:
			reader = csv.DictReader(csvfile)
			for row in reader:
		#        print(row['DATE'], row['PCU33443344'])
				dates.append(row[listofcolumnnames[0]])
				value.append(float(row[listofcolumnnames[5]]))
		dates = [dt.strptime(d, "%Y-%m-%d").date() for d in dates]
		data=[value,dates]
		return(data)



if __name__ == '__main__':

    app = wx.App(False)
    #create an object of CalcFrame
    frame = Inicial(None)
    #frame.createPlot1()
    #frame.createPlot2()
    #show the frame
    frame.Show(True)
    #app = MyApp(False)
    app.MainLoop()