#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:FG
# datetime:2022/4/1 13:58

from utils import load_data, Ngram
import numpy

'''
寻找超参数
'''


def ppl(n, corpus_len, vocab_len, dict_gram, dict_context, test_corpus, context_size):
    import math
    # 计算条件概率并存入字典 采用平滑
    dict_p = {}
    for x in dict_gram.keys():
        dict_p[x] = (dict_gram[x] + n) / (dict_context[x[0]] + n * vocab_len)
    ppl_num, ppl_sum = 0, 0
    for sentence in test_corpus:
        p_sum = 0
        # 插入句首句尾符号
        sentence = ['<BOS>'] + sentence + ['<EOS>']
        if len(sentence) < context_size:
            pass
        for i in range(context_size, len(sentence)):
            # 长为context_size的上文
            context = tuple(sentence[i - context_size:i])
            # 当前词
            target = sentence[i]
            # 对测试集中未登录词进行加一平滑
            if (context, target) not in dict_p:
                if context not in dict_context:
                    p = n / (n * vocab_len)
                else:
                    p = n / (dict_context[context] + n * vocab_len)
            else:
                p = dict_p[(context, target)]
            # 对数和
            p_sum += math.log(p, 2)
        # 计算困惑度
        ppl_num = 2 ** -(p_sum / len(sentence))
        ppl_sum += ppl_num
    # 计算平均困惑度
    ppl_aver = ppl_sum / corpus_len
    return ppl_aver


def get_num(valid_tr_txt, valid_txt, context_size):
    # 加载数据
    vocab_training, corpus_training = load_data(valid_tr_txt)
    vocab_test, corpus_test = load_data(valid_txt)
    # 得到词表大小 数据大小
    vocab_len = len(vocab_training)
    corpus_len = len(corpus_test)
    # 将数据传入模型
    dataset = Ngram(corpus_training, context_size)
    min_ppl = 1000000
    n = 1
    for i in numpy.arange(0.00005, 1.00, 0.00005):
        print(i)
        ppl_aver = ppl(i, corpus_len, vocab_len, dataset.dict_gram, dataset.dict_context, corpus_test,
                       context_size)
        if ppl_aver < min_ppl:
            min_ppl, n = ppl_aver, i
            print(n, ppl_aver)
    return n


if __name__ == '__main__':
    bigram_size = 1
    trigram_size = 2
    pku_bi_n = get_num("pku/valid-tr_pku.txt", "pku/valid_pku.txt", bigram_size)
    # pku_bi_n = 0.01055
    pku_tri_n = get_num("pku/valid-tr_pku.txt", "pku/valid_pku.txt", trigram_size)
    # pku_tri_n = 0.0009

    msr_bi_n = get_num("msr/valid-tr_msr.txt", "msr/valid_msr.txt", bigram_size)
    # msr_bi_n = 0.00575
    msr_tri_n = get_num("msr/valid-tr_msr.txt", "msr/valid_msr.txt", trigram_size)
    # msr_tri_n = 0.00085

    mix_bi_n = get_num("pku/valid-tr_mix.txt", "pku/valid_mix.txt", bigram_size)
    # mix_bi_n = 0.00565
    mix_tri_n = get_num("pku/valid-tr_mix.txt", "pku/valid_mix.txt", trigram_size)
    # mix_tri_n = 0.00065
