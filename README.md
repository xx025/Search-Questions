# Search-Questions

搜题

1. 搜题算法描述：
    1. 首先看要搜索的字符串是否是属于题目文本如果是则返回这个题目
        - (具有不唯一性，当要搜索字符串仅包含问题时比较合适)
    2. 如果没能找到包含要搜索字符串的题目则将要搜索到字符串进行分词操作得到一个词列表
        1. 遍历题目列表找到包含词列表中词最多一个题目，返回这个题目
        2. 如果多个题目同时得到相同的最大词列表项包含数，将这多个题目与要搜索的字符串进行莱温斯坦距离计算，返回距离最短的题目之一
            - (具有不唯一性，但概率较小，不考虑选线顺序变动对于要搜索的字符串较长时比较合适)

```PYTHON
import jieba

from pyscript.Question import question
import Levenshtein

jieba.initialize()  # 初始化


class base_cover:
    # 通过分词后词组的覆盖率对比
    coverage = None
    str1_list = ""
    str2 = ""
    str_qes = ""

    def __init__(self, str1_list, str2, str_qus):
        self.str1_list = str1_list
        self.str2 = str2
        self.str_qes = str_qus
        self.coverage = self.cover()

    def cover(self):
        num = 0
        if self.str_qes in self.str2:
            k = 1
            return k
        else:
            for i in self.str1_list:
                if i in self.str2:
                    num += 1
            return num / len(self.str1_list)


class base_leven():
    distance = 9999
    str2 = ""
    str1 = ""

    def __init__(self, str1, str2):
        self.str1 = str1
        self.str2 = str2
        self.distance = Levenshtein.distance(str1, str2)


class searchAns:
    ques_str = ""  # 要搜索的题目文本
    best_match = question()

    def __init__(self, ques):
        self.ques_str = self.formatstr(ques)

    def formatstr(self, ques):
        ques = str(ques)
        return ques.replace(" ", "").replace("\n", "").replace("\t", "")

    def get_ans(self, ques_bank):
        max_cover = 0
        best_match_list = []  # 记录分词覆盖率相同的
        for i in ques_bank:
            split = list(jieba.cut(self.ques_str, cut_all=False))
            cover = base_cover(str1_list=split, str2=i.get_ques_text(), str_qus=self.ques_str).coverage
            if cover == 1:
                self.best_match = i
                break
            elif cover == max_cover:
                best_match_list.append(i)
            elif cover >= max_cover:
                self.best_match = i
                max_cover = cover
                best_match_list = []  # 清空基于分词覆盖相同覆盖率的列表
        else:
            print(best_match_list)
            min_dis = 99999
            for k in best_match_list:
                distance = base_leven(str1=self.ques_str, str2=i.get_ques_text()).distance
                if distance == 0:
                    self.best_match = k
                elif distance <= min_dis:
                    min_dis = distance
                    self.best_match
                else:
                    pass
        return self.best_match


 ```

2. 脚本 main_server.py 运行一个小型服务器 通过浏览器搜题
   ![](https://cdn.jsdelivr.net/gh/xx025/cloudimg/img/20210630121138.png)
   ![](https://cdn.jsdelivr.net/gh/xx025/cloudimg/img/20210630121231.png)
3. 运行前请更改config.cfg配置的路径信息

3. 依赖

```
flask
flask_cors
jieba
Levenshtein
gevent
requests
pyperclip
```

4. 项目打包`pyinstaller -D main_server.py`

---
Warning: this is very unsafe

https://blog.csdn.net/gramdog/article/details/79225246

有关于允许跨域和http和http混合加载的安全策略的阻止方法

Chrome   
添加启动项： 右键点击Chrome快捷方式，在目标一栏后添加启动项

允许跨域： --disable-web-security --user-data-dir

允许mix-content： --allow-running-insecure-content

Fire Fox   
进入选项配置 地址栏输入about:config 允许跨域： security.fileuri.strict_origin_policy改为false

允许mix-content： security.mixed_content.block_active_content改为false

