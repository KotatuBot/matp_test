import pandas as pd
import matplotlib.pyplot as plt
from pandas.tools.plotting import scatter_matrix


class ScatterPlotings():
    def __init__(self):
        pass
    def GenerateDict(self,title):
        default_dict = {}
        for title_tip in title:
            default_dict[title_tip] = []

        return default_dict

    def ProcessList(self,title,data):
        value_all = []
        values = data.values()
        for key_value in values:
            tmp = []
            for site_name in title:
                if site_name in key_value.keys():
                    tmp.append(key_value[site_name])
                else:
                    tmp.append(0)
            value_all.append(tmp)

        return value_all

    def DataAlignment(self,title,data):
        value_all = self.ProcessList(title,data)
        default_dicts = self.GenerateDict(title)
        for data_tip in value_all:
            for number,tips in enumerate(data_tip):
                default_dicts[title[number]].append(tips)

        return default_dicts

    def ScatterPlot(self,data_frame):
        df = pd.DataFrame(data_frame)
        scatter_matrix(df, diagonal='kde', color='green', alpha=1)
        plt.savefig("image2.png")


    def main(self,title,data):
        data_frame = self.DataAlignment(title,data)
        self.ScatterPlot(data_frame)

if __name__ == "__main__":
    title = ["test1","test2","test3"]
    data = {"家事":{"test1":83,"test2":54},"テスト":{"test2":54,"test3":55},"みかん":{"test1":46,"test2":47}}
    sp = ScatterPlotings()
    sp.main(title,data)
