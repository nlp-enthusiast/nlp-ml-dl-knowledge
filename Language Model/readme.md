# 语言模型
# 1.为什么需要语言模型
语言模型可以用于 评估输入的语言符合性 选择符合语言的句子 生成符合语言的句子。
# 2.什么是语言模型
能够用于衡量符号序列是否符合某语言的形式化（数学）模型
# 3.如何建立语言模型
# ![image.png](https://cdn.nlark.com/yuque/0/2023/png/26311079/1679898989932-a1defe41-a3d7-4aca-aabc-bf86e7b642d4.png#averageHue=%23f9f8f8&clientId=ud25ddba6-7f4a-4&from=paste&height=426&id=ufa5ae8d9&name=image.png&originHeight=426&originWidth=676&originalType=binary&ratio=1&rotation=0&showTitle=false&size=33461&status=done&style=none&taskId=u8839cedc-0360-49f0-8584-a443f804ec0&title=&width=676)
## 3.1统计语言模型

- 完全独立假设

![image.png](https://cdn.nlark.com/yuque/0/2023/png/26311079/1679899351433-8747e0f4-77dc-4904-99dc-28f9bc11abc7.png#averageHue=%23f3f3f3&clientId=ud25ddba6-7f4a-4&from=paste&height=95&id=uac135783&name=image.png&originHeight=95&originWidth=577&originalType=binary&ratio=1&rotation=0&showTitle=false&size=9276&status=done&style=none&taskId=uf029f05d-04a3-4a56-8d52-7a294746b1a&title=&width=577)

- 单项相关假设

![image.png](https://cdn.nlark.com/yuque/0/2023/png/26311079/1679899363498-e1452e34-3a2e-4311-b1f3-76e90db0b89a.png#averageHue=%23f9f7f6&clientId=ud25ddba6-7f4a-4&from=paste&height=78&id=ud03120c2&name=image.png&originHeight=78&originWidth=912&originalType=binary&ratio=1&rotation=0&showTitle=false&size=5687&status=done&style=none&taskId=u8eec03c1-6d5c-4689-a737-ddcff1e3c81&title=&width=912)

- 双向相关假设

![image.png](https://cdn.nlark.com/yuque/0/2023/png/26311079/1679899382191-d200657e-bca3-425d-aabb-ec587067fd9a.png#averageHue=%23f9f7f5&clientId=ud25ddba6-7f4a-4&from=paste&height=107&id=u73241919&name=image.png&originHeight=107&originWidth=610&originalType=binary&ratio=1&rotation=0&showTitle=false&size=6392&status=done&style=none&taskId=ud7ebc706-251a-4936-91f4-28cc1686eeb&title=&width=610)
### 3.1.1 词独立语言模型
![image.png](https://cdn.nlark.com/yuque/0/2023/png/26311079/1679899588291-5843356e-83be-4ee6-b62a-968fcc1f44e5.png#averageHue=%23f4e9e9&clientId=ud25ddba6-7f4a-4&from=paste&height=291&id=uf286ac48&name=image.png&originHeight=291&originWidth=526&originalType=binary&ratio=1&rotation=0&showTitle=false&size=27923&status=done&style=none&taskId=u199a84dc-6349-407e-8938-8ceb33f9bf8&title=&width=526)
### 3.1.2 n-gram 语言模型
词wi仅与前序 n 个词相关
![image.png](https://cdn.nlark.com/yuque/0/2023/png/26311079/1679899724234-90ab39eb-859c-4d36-a5a0-c1226d690e07.png#averageHue=%23f7f6f5&clientId=ud25ddba6-7f4a-4&from=paste&height=90&id=ufd160f07&name=image.png&originHeight=90&originWidth=339&originalType=binary&ratio=1&rotation=0&showTitle=false&size=2917&status=done&style=none&taskId=ua2a8f4ea-757f-455f-a81d-155d5efa3c8&title=&width=339)
![image.png](https://cdn.nlark.com/yuque/0/2023/png/26311079/1679899787577-6172f071-d767-4731-b60b-45cb1a553745.png#averageHue=%23ededed&clientId=ud25ddba6-7f4a-4&from=paste&height=191&id=u6c14a4e5&name=image.png&originHeight=191&originWidth=676&originalType=binary&ratio=1&rotation=0&showTitle=false&size=21516&status=done&style=none&taskId=u88fa0421-845a-44d0-94ce-5fe8b47fe2a&title=&width=676)

极大似然估计

![image.png](https://cdn.nlark.com/yuque/0/2023/png/26311079/1679899864798-a8a6b860-fe2e-4649-859e-f41b6e13a325.png#averageHue=%23f7f5f4&clientId=uc446a9bd-f212-4&from=paste&height=96&id=u69437315&name=image.png&originHeight=96&originWidth=402&originalType=binary&ratio=1&rotation=0&showTitle=false&size=5221&status=done&style=none&taskId=u00ab458c-efd9-43b9-827b-f61c59a5aad&title=&width=402)

数据稀疏 (Sparse Data) /零计数（Zero Count）引起零概率问题，如何解决？
数据平滑-加1平滑

![image.png](https://cdn.nlark.com/yuque/0/2023/png/26311079/1679900187078-b695c552-72a2-4e12-8daa-d38a7fee1600.png#averageHue=%23f4f2f1&clientId=uc446a9bd-f212-4&from=paste&height=110&id=u95e4530f&name=image.png&originHeight=110&originWidth=402&originalType=binary&ratio=1&rotation=0&showTitle=false&size=5665&status=done&style=none&taskId=u4783bfdc-4138-45fc-ba52-89bd5a25d9d&title=&width=402)
# 3.2评价指标
困惑度（Perplexity）
![image.png](https://cdn.nlark.com/yuque/0/2023/png/26311079/1679900381562-8808be47-d16b-433d-8b04-307646caf7af.png#averageHue=%23f6f5f4&clientId=u4aae8135-89e1-4&from=paste&height=90&id=u079ba86e&name=image.png&originHeight=90&originWidth=532&originalType=binary&ratio=1&rotation=0&showTitle=false&size=5056&status=done&style=none&taskId=u8086cd11-03bd-4fe4-95c3-57ef2a6e34f&title=&width=532)

![image.png](https://cdn.nlark.com/yuque/0/2023/png/26311079/1679900396626-8f03e355-9f2f-4213-96e8-2e18e079e0a0.png#averageHue=%23f7f6f4&clientId=u4aae8135-89e1-4&from=paste&height=114&id=uee1f256a&name=image.png&originHeight=114&originWidth=402&originalType=binary&ratio=1&rotation=0&showTitle=false&size=5120&status=done&style=none&taskId=u99aa133f-b68d-42b3-be0b-9dc32825dbe&title=&width=402)
