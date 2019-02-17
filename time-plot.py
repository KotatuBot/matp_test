import collections
from datetime import datetime as dt
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
class Timeplot():
	def __init__(self):
		self.all_datetime_label = []
		self.all_datetime_value = []
	def SortData(self,data):
		# 並び順とカウントを行なう
		date_time = [dt.strptime(tstr,'%Y-%m-%d %H:%M:%S') for tstr in data]
		data_counter = collections.Counter(date_time)
		data_origin = collections.Counter(data)
		test2 = list(data_counter.keys())
		test2.sort()
		# データを元に戻す．
		datetime_label = [date_str.strftime('%Y-%m-%d %H:%M:%S') for date_str in test2]
		count_value = [data_origin[time_name] for time_name in datetime_label]
		self.all_datetime_label.append(datetime_label)
		self.all_datetime_value.append(count_value)
	
	def Plot(self,title):
		COL = 1
		ROW = len(title)
		fig, axs = plt.subplots(ncols=1, nrows=ROW, figsize=(20,10),dpi=200)
		for number,title_name in enumerate(title):
			axs[number].plot(self.all_datetime_label[number],self.all_datetime_value[number])
    
		if COL*ROW - len(title)>0:
			numbers = COL*ROW - len(title)
			for j in range(numbers):
				number += 1
				axs[number].axis('off')

		plt.tight_layout()
		plt.show()

if __name__ == "__main__":
	timeplot = Timeplot()
	
	data = ["2017-07-02 22:17:02",
        "2017-07-02 22:17:02",
        "2017-07-02 22:17:02",
        "2017-07-02 22:17:02",
        "2017-07-02 22:17:02",
        "2017-07-02 22:17:02",
        "2017-07-02 17:48:55",
        "2017-07-02 17:48:55",
        "2017-07-02 17:48:55",
        "2017-07-02 17:48:55",
        "2017-07-02 17:48:55",
        "2017-07-02 17:48:55",
        "2017-07-02 19:45:46",
        "2017-07-02 08:45:46",
        "2017-07-02 19:45:46",
        "2017-07-02 19:45:48",
        "2017-07-02 21:45:48",
        "2017-07-02 20:34:49"
        ]
		
	datalist = [data,data]
	for j in datalist:
		#ここをデータ収集に突っ込む	
		timeplot.SortData(j)
	# ループを抜けてから突っ込む
	timeplot.Plot(['test2','test3'])

