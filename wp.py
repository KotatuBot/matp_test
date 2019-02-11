import matplotlib.pyplot as plt
from wordcloud import WordCloud

class WCP():
    def __init__(self):
        pass

    def wordcloudplot(self,wordlist,title_set):
        """
        wordlist: [[1,2,3],[2,3,4,5]]-> 単語をリストごとに入れたもの
        title_Set: [[title_seting]]
        """
        COL=2
        ROW=2
        fig, axs = plt.subplots(ncols=COL, nrows=ROW, figsize=(15,7))
        axs = axs.flatten()

        for number,j in enumerate(wordlist):
            fonts = '/System/Library/Fonts/ヒラギノ明朝 ProN.ttc'
            text = "　".join(j)
            wordcloud = WordCloud(background_color="white",font_path=fonts,regexp="[\w']+").generate(text)
            axs[number].imshow(wordcloud)
            axs[number].axis('off')
            axs[number].set_title('Topic '+title_set[number])

        if COL*ROW - len(wordlist)>0:
            numbers = COL*ROW - len(wordlist)
            for j in range(numbers):
                number += 1
                axs[number].axis('off')

        plt.tight_layout()
        plt.savefig("wc.png")

if __name__ == "__main__":
    word = ['中国','日本','日本','アメリカ','神','神']
    wordlist = [word,word]
    title = ["test1","test2"]
    wcp = WCP()
    wcp.wordcloudplot(wordlist,title)
