#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:FG
# datetime:2022/4/1 15:59

if __name__ == '__main__':

    '''
    生成验证集和其对应训练集
    验证集为原训练集的1/10 剩余9/10 作为对应训练集
    '''

    with open('pku/training_pku.txt',"r",encoding="utf-8") as f1:
        with open('pku/valid_pku.txt', 'w',encoding="utf-8") as f2:
            with open('pku/valid-tr_pku.txt', 'w',encoding="utf-8") as f3:
                sentences = f1.readlines()
                for i in range(1900):
                    f2.write(sentences[i])
                for j in range(1900, len(sentences)):
                    f3.write(sentences[j])
            f3.close()
        f2.close()
    f1.close()

    with open('msr/training_msr.txt',"r",encoding="utf-8") as f1:
        with open('msr/valid_msr.txt', 'w',encoding="utf-8") as f2:
            with open('msr/valid-tr_msr.txt', 'w',encoding="utf-8") as f3:
                sentences = f1.readlines()
                for i in range(8690):
                    f2.write(sentences[i])
                for j in range(8690, len(sentences)):
                    f3.write(sentences[j])
            f3.close()
        f2.close()
    f1.close()

    with open('pku/training_pku.txt', 'r', encoding='utf-8') as f1:
        with open('msr/training_msr.txt', 'r', encoding='utf-8') as f2:
            with open('pku/valid_mix.txt', 'w',encoding="utf-8") as f3:
                with open('pku/valid-tr_mix.txt', 'w',encoding="utf-8") as f4:
                    # 存验证集
                    text1 = list()
                    # 存训练集
                    text2 = list()
                    sentences1 = f1.readlines()
                    sentences2 = f2.readlines()

                    for i in range(1900):
                        f3.write(sentences1[i])
                    for i in range(1900, len(sentences1)):
                        f4.write(sentences1[i])

                    for i in range(8690):
                        f3.write(sentences2[i])
                    for i in range(8690, len(sentences2)):
                        f4.write(sentences2[i])
                f1.close()
            f2.close()
        f3.close()
    f4.close()
