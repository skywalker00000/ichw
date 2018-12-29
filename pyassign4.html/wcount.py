"""wcount.py: count words from an Internet file.

__author__ = "Liyuhao"
__pkuid__  = "1800011761"
__email__  = "1800011761@pku.edu.cn"
"""

import string
import sys
import urllib.request


def wcount(content, topn=10, tongji={}):
    for sen in content:
        desen = sen.decode()
        ready = desen.translate(dele)
        lst = ready.split()
        for word in lst:
            if word in tongji:
                tongji[word] += 1
            else:
                tongji[word] = 1
    tongji = sorted(tongji.items(), key=lambda x: x[1], reverse=True)
    for i in range(10):
        print(tongji[i][0], '     ', tongji[i][1])


def main():
    topn = input()
    wcount(content, topn)


url = input()
myfile = urllib.request.urlopen(url)
content = myfile.readlines()
dele = str.maketrans({key: None for key in string.punctuation})
if __name__ == "__main__":
    if len(sys.argv) == 1:
        print('Usage: {} url [topn]'.format(sys.argv[0]))
        print('  url: URL of the txt file to analyze ')
        print('  topn: how many (words count) to output. \
                If not given, will output top 10 words')
        main()
