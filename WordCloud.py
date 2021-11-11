from wordcloud import WordCloud
import MeCab
import sys
from sys import argv
input_file_name= sys.argv[1]

print(input_file_name)

text = open("all.txt", encoding="utf8").read()
 
with open(input_file_name, encoding="UTF-8") as f:
    data = f.read()

select_conditions = [ '名詞']
stop_words = ['アプリケーション','サービス','これら','および','Amazon Web Services','Web　Services','AWS','Amazon','Web','Service','!','!!','#','$','(',')','+',',','.','%','-','&','/','2021','All','Services','reserved','affiliates','rights','Inc','©',':','1','2','3','USD','こと','必要','ため','これ','使用','顧客','対応','場合','よう','"Amazon Web','Web Services']

tagger = MeCab.Tagger('-Ochasen -d /usr/local/lib/mecab/dic/mecab-ipadic-neologd/')
tagger.parse('')

def wakati_text(text):
    node = tagger.parseToNode(text)
    terms = []

    while node:

        term = node.surface
        pos = node.feature.split(',')[0]
        if pos in select_conditions:
            if term in stop_words:
                pass
            else:
                terms.append(term)
        node = node.next
    text_result = '\n'.join(terms)
    return text_result

result_text = wakati_text(data)

f = open('result.txt', 'w', encoding='UTF-8')
f.write(result_text)
f.close()

wordcloud = WordCloud(background_color='white',max_font_size=150,max_words=50,font_path="./ipaexg.ttf",width=1000, height=600).generate(result_text)
wordcloud.to_file("result.png")
