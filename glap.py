import matplotlib.pyplot as plt
from wordcloud import WordCloud
import numpy as np

class GenerateGlaf():
    def __init__(self):
        pass

    def generateglaf(self,origindata,title_set):
        """
        origindata: [[1,2,3],[2,3,4,5]]-> 単語をリストごとに入れたもの
        title_Set: [[title_seting]]
        """

        COL=2
        ROW=2
        fig, axs = plt.subplots(ncols=COL, nrows=ROW, figsize=(15,7))
        axs = axs.flatten()

        for number,j in enumerate(origindata):
            axs[number].hist(j, bins=50)
            axs[number].set_title('Topic '+title_set[number])


        # あまりのグラフを非表示にする
        if COL*ROW - len(origindata)>0:
            numbers = COL*ROW - len(origindata)
            for j in range(numbers):
                number += 1
                axs[number].axis('off')

        plt.tight_layout()
        plt.savefig("glaping.png")

if __name__ == "__main__":
    title = ["test1","test2","test3"]
    test2 = [10,23,30,40,50]
    test = [test2,test2,test2]
    gg = GenerateGlaf()
    gg.generateglaf(test,title)
