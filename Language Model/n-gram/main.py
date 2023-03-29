#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:FG
# datetime:2022/3/29 13:48
from utils import get_ppl, write_model, write_result, get_mix_ppl, write_count

if __name__ == '__main__':
    # 依赖长度
    bigram_size = 1
    trigram_size = 2

    # 超参数
    pku_bi_n = 0.01055
    pku_tri_n = 0.0009
    msr_bi_n = 0.00575
    msr_tri_n = 0.00085
    mix_bi_n = 0.00565
    mix_tri_n = 0.00065

    # 输出频次
    # write(训练数据, size, gram频次, 前文频次)
    write_count('pku/training_pku.txt', bigram_size, 'count/gram_pku_bi.txt', 'count/context_pku_bi.txt')
    write_count('pku/training_pku.txt', trigram_size, 'count/gram_pku_tri.txt', 'count/context_pku_tri.txt')
    write_count('msr/training_msr.txt', bigram_size, 'count/gram_msr_bi.txt', 'count/context_msr_bi.txt')
    write_count('msr/training_msr.txt', trigram_size, 'count/gram_msr_tri.txt', 'count/context_msr_tri.txt')

    # 输出四种模型及实验数据
    # pku 数据 bi模型
    pku_bi_model, pku_bi_ppl, pku_aver_bi = get_ppl(pku_bi_n, "pku/training_pku.txt", 'pku/test_pku.txt', bigram_size)
    write_model(pku_bi_model, 'model/pku_bi_model.txt')
    write_result(pku_bi_ppl, 'result/pku_bi_result.txt')
    print('pku_aver_bi', pku_aver_bi)  # 超参数:0.01055 平均困惑度:4132.187
    print('')

    # pku 数据 tri模型
    pku_tri_model, pku_tri_ppl, pku_aver_tri = get_ppl(pku_tri_n, "pku/training_pku.txt", 'pku/test_pku.txt',
                                                       trigram_size)
    write_model(pku_tri_model, 'model/pku_tri_model.txt')
    write_result(pku_tri_ppl, 'result/pku_tri_result.txt')
    print('pku_aver_tri', pku_aver_tri)  # 平均困惑度:9080.823
    print('')

    # msr 数据 bi模型
    msr_bi_model, msr_bi_result, msr_aver_bi = get_ppl(msr_bi_n, "msr/training_msr.txt", 'msr/test_msr.txt',
                                                       bigram_size)
    write_model(msr_bi_model, 'model/msr_bi_model.txt')
    write_result(msr_bi_result, 'result/msr_bi_result.txt')
    print('msr_aver_bi', msr_aver_bi)  # 平均困惑度:2148.493
    print('')

    # msr 数据 tri模型
    msr_tri_model, msr_tri_result, msr_aver_tri = get_ppl(msr_tri_n, "msr/training_msr.txt", 'msr/test_msr.txt',
                                                          trigram_size)
    write_model(msr_tri_model, 'model/msr_tri_model.txt')
    write_result(msr_tri_result, 'result/msr_tri_result.txt')
    print('msr_aver_tri', msr_aver_tri)  # 平均困惑度:7077.380
    print('')

    # 互换测试数据 输出结果
    # pku 建模 msr 测试 bi模型
    pku_bi_msr_model, pku_bi_msr_result, pku_bi_msr_aver = get_ppl(pku_bi_n, "pku/training_pku.txt", 'msr/test_msr.txt',
                                                                   bigram_size)
    write_result(pku_bi_msr_result, 'result/pku_bi_msr_result.txt')
    print('pku_bi_msr_aver', pku_bi_msr_aver)  # 平均困惑度:3048.676
    print('')

    # pku 建模 msr 测试 tri模型
    pku_tri_msr_model, pku_tri_msr_result, pku_tri_msr_aver = get_ppl(pku_tri_n, "pku/training_pku.txt",
                                                                      'msr/test_msr.txt',
                                                                      trigram_size)
    write_result(pku_tri_msr_result, 'result/pku_tri_msr_result.txt')
    print('pku_tri_msr_aver', pku_tri_msr_aver)  # 平均困惑度:8105.584
    print('')

    # msr 建模 pku 测试 bi模型
    msr_bi_pku_model, msr_bi_pku_result, msr_bi_pku_aver = get_ppl(msr_bi_n, "msr/training_msr.txt", 'pku/test_pku.txt',
                                                                   bigram_size)
    write_result(msr_bi_pku_result, 'result/msr_bi_pku_result.txt')
    print('msr_bi_pku_aver', msr_bi_pku_aver)  # 平均困惑度:7632.463
    print('')

    # msr 建模 pku 测试 tri模型
    msr_tri_pku_model, msr_tri_pku_result, msr_tri_pku_aver = get_ppl(msr_tri_n, "msr/training_msr.txt",
                                                                      'pku/test_pku.txt',
                                                                      trigram_size)
    write_result(msr_tri_pku_result, 'result/msr_tri_pku_result.txt')
    print('msr_tri_pku_aver', msr_tri_pku_aver)  # 平均困惑度:14975.679
    print('')

    # 混合数据训练 两种语言模型 两个测试数据
    # bi 模型 pku 测试
    mix_bi_model, mix_bi_pku_result, mix_bi_pku_aver = get_mix_ppl(mix_bi_n, "msr/training_msr.txt",
                                                                   "pku/training_pku.txt",
                                                                   "pku/test_pku.txt",
                                                                   bigram_size)
    write_model(mix_bi_model, 'model/mix_bi_model.txt')
    write_result(mix_bi_pku_result, 'result/mix_bi_pku_result.txt')
    print('mix_bi_pku_aver', mix_bi_pku_aver)  # 平均困惑度:4977.873
    print('')

    # bi 模型 msr 测试
    mix_bi_model, mix_bi_msr_result, mix_bi_msr_aver = get_mix_ppl(mix_bi_n, "msr/training_msr.txt",
                                                                   "pku/training_pku.txt",
                                                                   "msr/test_msr.txt",
                                                                   bigram_size)
    write_result(mix_bi_msr_result, 'result/mix_bi_msr_result.txt')
    print('mix_bi_msr_aver', mix_bi_msr_aver)  # 平均困惑度:2084.420
    print('')

    # tri 模型 pku 测试
    mix_tri_model, mix_tri_pku_result, mix_tri_pku_aver = get_mix_ppl(mix_tri_n, "msr/training_msr.txt",
                                                                      "pku/training_pku.txt",
                                                                      "pku/test_pku.txt",
                                                                      trigram_size)
    write_model(mix_tri_model, 'model/mix_tri_model.txt')
    write_result(mix_tri_pku_result, 'result/mix_tri_pku_result.txt')
    print('mix_tri_pku_aver', mix_tri_pku_aver)  # 平均困惑度:11774.780
    print('')

    # tri 模型 msr 测试
    mix_tri_model, mix_tri_msr_result, mix_tri_msr_aver = get_mix_ppl(mix_tri_n, "msr/training_msr.txt",
                                                                      "pku/training_pku.txt",
                                                                      "msr/test_msr.txt",
                                                                      trigram_size)
    write_result(mix_tri_msr_result, 'result/mix_tri_msr_result.txt')
    print('mix_tri_msr_aver', mix_tri_msr_aver)  # 平均困惑度:7496.348
