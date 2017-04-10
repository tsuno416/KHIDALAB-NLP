# -*- coding:utf-8 -*-
#!/usr/bin/env python

import pandas as pd
import sys
import re

def load_csv(source_csv):
    df = pd.read_csv(source_csv)
    return df

def list_authors(df):
    # list up authors
    for authors in df[df.columns[0]]:
        for author in authors.split(','):
            print(author.lstrip())
    # temporary use with "xxx | sort|uniq -c | sort-n" 

def search_word(df):
    search_word = r'compet'
    search_pattern = re.compile(search_word)
    ### column numbers ###
    # 11 DOI
    # 0  著者名
    # 1  タイトル
    # 2  出版年
    #
    # 9  ページ数
    # 10 被引用数
    # 12 リンク
    # 13 著者所属機関名
    # 14 著者 + 所属機関
    # 15 抄録
    # 16 著者キーワード
    # 17 索引キーワード
    # 18 参考文献
    # 21 文献タイプ
    #
    ###
    n = 1
    for texts in df[df.columns[n]]:
        match_lines = search_pattern.match(texts)
        print(match_lines)

if __name__ == '__main__':
    source_csv = sys.argv[1]
    df = load_csv(source_csv)
    #list_authors(df)
    search_word(df)
   
