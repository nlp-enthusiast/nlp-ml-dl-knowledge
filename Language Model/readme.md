<a name="Kktay"></a>
## 1. 为什么需要语言模型
语言模型可以用于 评估输入的语言符合性 选择符合语言的句子 生成符合语言的句子。
<a name="MkPWI"></a>
## 2. 什么是语言模型
能够用于衡量符号序列是否符合某语言的形式化（数学）模型
<a name="obsQO"></a>
## 3. 如何建立语言模型
<a name="Ukb17"></a>
# ![image.png](https://cdn.nlark.com/yuque/0/2023/png/26311079/1679898989932-a1defe41-a3d7-4aca-aabc-bf86e7b642d4.png#averageHue=%23f9f8f8&clientId=ud25ddba6-7f4a-4&from=paste&height=426&id=ufa5ae8d9&name=image.png&originHeight=426&originWidth=676&originalType=binary&ratio=1&rotation=0&showTitle=false&size=33461&status=done&style=none&taskId=u8839cedc-0360-49f0-8584-a443f804ec0&title=&width=676)
<a name="d9DEi"></a>
## 4. 统计语言模型

- 完全独立假设

![image.png](https://cdn.nlark.com/yuque/0/2023/png/26311079/1679899351433-8747e0f4-77dc-4904-99dc-28f9bc11abc7.png#averageHue=%23f3f3f3&clientId=ud25ddba6-7f4a-4&from=paste&height=69&id=uac135783&name=image.png&originHeight=95&originWidth=577&originalType=binary&ratio=1&rotation=0&showTitle=false&size=9276&status=done&style=none&taskId=uf029f05d-04a3-4a56-8d52-7a294746b1a&title=&width=417)

- 单项相关假设

![image.png](https://cdn.nlark.com/yuque/0/2023/png/26311079/1679899363498-e1452e34-3a2e-4311-b1f3-76e90db0b89a.png#averageHue=%23f9f7f6&clientId=ud25ddba6-7f4a-4&from=paste&height=46&id=ud03120c2&name=image.png&originHeight=78&originWidth=912&originalType=binary&ratio=1&rotation=0&showTitle=false&size=5687&status=done&style=none&taskId=u8eec03c1-6d5c-4689-a737-ddcff1e3c81&title=&width=541)

- 双向相关假设

![image.png](https://cdn.nlark.com/yuque/0/2023/png/26311079/1679899382191-d200657e-bca3-425d-aabb-ec587067fd9a.png#averageHue=%23f9f7f5&clientId=ud25ddba6-7f4a-4&from=paste&height=86&id=u73241919&name=image.png&originHeight=107&originWidth=610&originalType=binary&ratio=1&rotation=0&showTitle=false&size=6392&status=done&style=none&taskId=ud7ebc706-251a-4936-91f4-28cc1686eeb&title=&width=488)
<a name="K79X5"></a>
### 4.1 词独立语言模型
![image.png](https://cdn.nlark.com/yuque/0/2023/png/26311079/1679899588291-5843356e-83be-4ee6-b62a-968fcc1f44e5.png#averageHue=%23f4e9e9&clientId=ud25ddba6-7f4a-4&from=paste&height=271&id=uf286ac48&name=image.png&originHeight=291&originWidth=526&originalType=binary&ratio=1&rotation=0&showTitle=false&size=27923&status=done&style=none&taskId=u199a84dc-6349-407e-8938-8ceb33f9bf8&title=&width=490)
<a name="RvRiG"></a>
### 4.2 n-gram 语言模型
词wi仅与前序 n 个词相关<br />![image.png](https://cdn.nlark.com/yuque/0/2023/png/26311079/1679899724234-90ab39eb-859c-4d36-a5a0-c1226d690e07.png#averageHue=%23f7f6f5&clientId=ud25ddba6-7f4a-4&from=paste&height=63&id=ufd160f07&name=image.png&originHeight=90&originWidth=339&originalType=binary&ratio=1&rotation=0&showTitle=false&size=2917&status=done&style=none&taskId=ua2a8f4ea-757f-455f-a81d-155d5efa3c8&title=&width=238)<br />![image.png](https://cdn.nlark.com/yuque/0/2023/png/26311079/1679899787577-6172f071-d767-4731-b60b-45cb1a553745.png#averageHue=%23ededed&clientId=ud25ddba6-7f4a-4&from=paste&height=142&id=u6c14a4e5&name=image.png&originHeight=191&originWidth=676&originalType=binary&ratio=1&rotation=0&showTitle=false&size=21516&status=done&style=none&taskId=u88fa0421-845a-44d0-94ce-5fe8b47fe2a&title=&width=502)<br />极大似然估计<br />![image.png](https://cdn.nlark.com/yuque/0/2023/png/26311079/1679899864798-a8a6b860-fe2e-4649-859e-f41b6e13a325.png#averageHue=%23f7f5f4&clientId=uc446a9bd-f212-4&from=paste&height=61&id=u69437315&name=image.png&originHeight=96&originWidth=402&originalType=binary&ratio=1&rotation=0&showTitle=false&size=5221&status=done&style=none&taskId=u00ab458c-efd9-43b9-827b-f61c59a5aad&title=&width=256)<br />数据稀疏 (Sparse Data) /零计数（Zero Count）引起零概率问题，如何解决？<br />数据平滑-加1平滑<br />![image.png](https://cdn.nlark.com/yuque/0/2023/png/26311079/1679900187078-b695c552-72a2-4e12-8daa-d38a7fee1600.png#averageHue=%23f4f2f1&clientId=uc446a9bd-f212-4&from=paste&height=71&id=u95e4530f&name=image.png&originHeight=110&originWidth=402&originalType=binary&ratio=1&rotation=0&showTitle=false&size=5665&status=done&style=none&taskId=u4783bfdc-4138-45fc-ba52-89bd5a25d9d&title=&width=261)
<a name="X7qM0"></a>
### 4.3 评价指标
困惑度（Perplexity）

![image.png](https://cdn.nlark.com/yuque/0/2023/png/26311079/1679900381562-8808be47-d16b-433d-8b04-307646caf7af.png#averageHue=%23f6f5f4&clientId=u4aae8135-89e1-4&from=paste&height=62&id=u079ba86e&name=image.png&originHeight=90&originWidth=532&originalType=binary&ratio=1&rotation=0&showTitle=false&size=5056&status=done&style=none&taskId=u8086cd11-03bd-4fe4-95c3-57ef2a6e34f&title=&width=364)<br />![image.png](https://cdn.nlark.com/yuque/0/2023/png/26311079/1679900396626-8f03e355-9f2f-4213-96e8-2e18e079e0a0.png#averageHue=%23f7f6f4&clientId=u4aae8135-89e1-4&from=paste&height=77&id=uee1f256a&name=image.png&originHeight=114&originWidth=402&originalType=binary&ratio=1&rotation=0&showTitle=false&size=5120&status=done&style=none&taskId=u99aa133f-b68d-42b3-be0b-9dc32825dbe&title=&width=272)
<a name="E896U"></a>
## 5. 神经语言模型

- n-gram 语言模型维度过高 1000 词汇 参数空间为 1000000000
- 只能依赖固定距离的词汇 不够灵活
- 无法判别同义词

单向相关语言模型：

![image.png](https://cdn.nlark.com/yuque/0/2023/png/26311079/1679903258072-d3ebeb93-d976-4022-ab84-7367940e8e71.png#averageHue=%23f9f7f6&clientId=u33be5a7e-a8b5-4&from=paste&height=78&id=uc965a009&name=image.png&originHeight=78&originWidth=912&originalType=binary&ratio=1&rotation=0&showTitle=false&size=5852&status=done&style=none&taskId=ube0ecc70-0969-452b-9fdd-67bed841ca9&title=&width=912)

单向有限相关假设：<br />词wi仅与前序 n-1 个词相关

![image.png](https://cdn.nlark.com/yuque/0/2023/png/26311079/1679903400024-aaac6b28-e6f3-4673-99a4-2f58feff6975.png#averageHue=%23f7f5f3&clientId=u33be5a7e-a8b5-4&from=paste&height=41&id=u72332e1e&name=image.png&originHeight=51&originWidth=475&originalType=binary&ratio=1&rotation=0&showTitle=false&size=3158&status=done&style=none&taskId=u9ecadedb-2bd7-461e-879a-ad1a425f7c8&title=&width=380)
<a name="zcP1c"></a>
### 5.1 模型定义

![image.png](https://cdn.nlark.com/yuque/0/2023/png/26311079/1679903446411-de677dd4-abce-4f92-b23a-f652284b366f.png#averageHue=%23f7f5f3&clientId=u33be5a7e-a8b5-4&from=paste&height=39&id=ufc4b82f7&name=image.png&originHeight=50&originWidth=476&originalType=binary&ratio=1&rotation=0&showTitle=false&size=3060&status=done&style=none&taskId=u03f01273-7e4f-47a7-8f97-ebc4f62cbe0&title=&width=374)<br />![image.png](https://cdn.nlark.com/yuque/0/2023/png/26311079/1679903454293-725411b7-2fb4-47e5-a6ab-fc2edf3542fe.png#averageHue=%23f5f3f1&clientId=u33be5a7e-a8b5-4&from=paste&height=41&id=uaaa850cb&name=image.png&originHeight=48&originWidth=636&originalType=binary&ratio=1&rotation=0&showTitle=false&size=3522&status=done&style=none&taskId=u72521194-3e9f-4d98-b695-a4fce28d54e&title=&width=546)

函数 g 的输出是 |V| 维度的向量，向量第 t 维是条件概率P(wi=t|w1i-1)的估计

![image.png](https://cdn.nlark.com/yuque/0/2023/png/26311079/1679903539836-e0c207dd-2678-414c-885f-f24e506724b0.png#averageHue=%23f3f1ef&clientId=u33be5a7e-a8b5-4&from=paste&height=51&id=u87ee9e2f&name=image.png&originHeight=51&originWidth=185&originalType=binary&ratio=1&rotation=0&showTitle=false&size=2055&status=done&style=none&taskId=u54a7d7a4-38c7-4cbe-9304-86e52a87140&title=&width=185)<br />每一个词的 m 维的向量表征，C 是一个 |V|×m 的矩阵，其第 i 行为C(wi)<br />![image.png](https://cdn.nlark.com/yuque/0/2023/png/26311079/1679904339965-e12c6bd9-d407-4067-a75e-8054aa6304b2.png#averageHue=%23f5f5f5&clientId=u33be5a7e-a8b5-4&from=paste&height=478&id=u10e72924&name=image.png&originHeight=564&originWidth=822&originalType=binary&ratio=1&rotation=0&showTitle=false&size=122646&status=done&style=none&taskId=u345e7212-1fd6-4f12-869e-79eba910e76&title=&width=697)

![image.png](https://cdn.nlark.com/yuque/0/2023/png/26311079/1679904412070-b2ab38f8-8a56-4862-9856-bac6a185e1d7.png#averageHue=%23fcfcfc&clientId=u33be5a7e-a8b5-4&from=paste&height=158&id=ue835c2bb&name=image.png&originHeight=246&originWidth=769&originalType=binary&ratio=1&rotation=0&showTitle=false&size=16978&status=done&style=none&taskId=u1df761dd-6925-4620-bb69-86221f35b2b&title=&width=495)<br />优势：泛化能力强，相似的上下文的词具有相似的表征向量<br />劣势：有限单项相关性，不能注意超过窗口的词汇，没考虑多义词的问题，同一单词不同含义应用不同向量表征。

