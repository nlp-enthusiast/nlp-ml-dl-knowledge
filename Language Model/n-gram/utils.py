#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:FG
# datetime:2022/3/28 21:47

from tqdm.auto import tqdm
# from torch.utils.data import Dataset
from vocab import Vocab

BOS_TOKEN = "<BOS>"
EOS_TOKEN = "<EOS>"


class Ngram():
    def __init__(self, corpus, context_size):
        self.data = []
        # 存放 ((前文),目标词) 频次
        self.dict_gram = {}
        # 存放 (前文) 频次
        self.dict_context = {}
        self.bos = BOS_TOKEN
        self.eos = EOS_TOKEN
        self.sum = 0
        for sentence in tqdm(corpus, desc="Dataset Construction"):
            # 插入句首句尾符号
            sentence = [self.bos] + sentence + [self.eos]
            if len(sentence) < context_size:
                continue
            for i in range(context_size, len(sentence)):
                # 长为context_size的上文
                context = tuple(sentence[i - context_size:i])
                # 当前词
                target = sentence[i]
                self.data.append((context, target))
                # 记录历史与当前词共现的频次
                self.dict_gram[(context, target)] = self.dict_gram.get((context, target), 0) + 1
                # 记录历史频次
                self.dict_context[context] = self.dict_context.get(context, 0) + 1

    def __len__(self):
        return len(self.data)

    def __getitem__(self, i):
        return self.data[i]


# 计算困惑度与平均困惑度
def ppl(n, corpus_len, vocab_len, dict_gram, dict_context, test_corpus, context_size):
    import math
    # 计算条件概率并存入字典 采用平滑
    dict_p = {}
    for x in dict_gram.keys():
        dict_p[x] = (dict_gram[x] + n) / (dict_context[x[0]] + n * vocab_len)
    ppl_num, ppl_sum = 0, 0
    ppl_list = []
    for sentence in tqdm(test_corpus, desc="Calculate PPL"):
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
        ppl_list.append(ppl_num)
        # if ppl_num<3:
        #     print(sentence)
        ppl_sum += ppl_num
    # 计算平均困惑度
    ppl_aver = ppl_sum / corpus_len

    return dict_p, ppl_list, ppl_aver


# 加载数据
def load_data(data):
    with open(data, 'r', encoding='utf-8') as f1:
        corpus = list()
        for sentence in f1.readlines():
            sentence_data = sentence.split()
            corpus.append(sentence_data)
            # 构建词表,传入预留标记
        vocab = Vocab.build(corpus, reserved_tokens=[BOS_TOKEN, EOS_TOKEN])
        f1.close()
    return vocab, corpus


# 得到模型参数与实验结果
def get_ppl(n, train_txt, test_txt, context_size):
    # 加载数据
    vocab_training, corpus_training = load_data(train_txt)
    vocab_test, corpus_test = load_data(test_txt)
    # 得到词表大小 数据大小
    vocab_len = len(vocab_training)
    corpus_len = len(corpus_test)
    # 将数据传入模型
    dataset = Ngram(corpus_training, context_size)
    # 计算困惑度与平均困惑度
    dict_p, ppl_, ppl_aver = ppl(n, corpus_len, vocab_len, dataset.dict_gram, dataset.dict_context, corpus_test,
                                 context_size)
    # 返回条件概率句子困惑度与平均困惑度

    return dict_p, ppl_, ppl_aver


# 加载混合数据
def load_mix_data(train_pku_txt, train_msr_txt):
    # 导入数据
    with open(train_pku_txt, 'r', encoding='utf-8') as f1:
        with open(train_msr_txt, 'r', encoding='utf-8') as f2:
            corpus = list()
            sentences1 = f1.readlines()
            sentences2 = f2.readlines()
            for sentence in sentences1:
                sentence1_data = sentence.split()
                corpus.append(sentence1_data)
            for sentence in sentences2:
                sentence2_data = sentence.split()
                corpus.append(sentence2_data)
            vocab = Vocab.build(corpus, reserved_tokens=[BOS_TOKEN, EOS_TOKEN])

    return vocab, corpus


def get_mix_ppl(n, train_pku_txt, train_msr_txt, test_txt, context_size):
    vocab_training, corpus_training = load_mix_data(train_pku_txt, train_msr_txt)
    vocab_test, corpus_test = load_data(test_txt)
    vocab_len = len(vocab_training)
    corpus_len = len(corpus_test)
    dataset = Ngram(corpus_training, context_size)
    dict_p, ppl_mix, ppl_aver = ppl(n, corpus_len, vocab_len, dataset.dict_gram, dataset.dict_context, corpus_test,
                                    context_size)
    return dict_p, ppl_mix, ppl_aver


# 写入模型数据
def write_model(model, model_txt):
    with open(model_txt, 'w', encoding='utf-8') as f:
        key, value = list(model.keys()), list(model.values())
        for i in range(len(key)):
            f.write('第' + str(i) + '个参数' + str(key[i]) + '-----' + str(value[i]) + '\n')
        f.close()


# 写入结果
def write_result(data, data_txt):
    with open(data_txt, 'w', encoding='utf-8') as f:
        for i in range(len(data)):
            f.write('第' + str(i) + '句的困惑度' + '-----' + str(data[i]) + '\n')
        f.close()


# 写入频次
def write_count(train_txt, context_size, gram_count, context_count):
    # 加载数据
    vocab_training, corpus_training = load_data(train_txt)
    # 将数据传入模型
    dataset = Ngram(corpus_training, context_size)
    with open(gram_count, 'w',encoding="utf-8") as f1:
        key, value = list(dataset.dict_gram.keys()), list(dataset.dict_gram.values())
        for i in range(len(key)):
            f1.write(str(key[i]) + '的频次-----' + str(value[i]) + '\n')
        f1.close()

    with open(context_count, 'w',encoding="utf-8") as f2:
        key, value = list(dataset.dict_context.keys()), list(dataset.dict_context.values())
        for i in range(len(key)):
            f2.write(str(key[i]) + '的频次-----' + str(value[i]) + '\n')
        f2.close()
