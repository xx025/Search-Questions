# Search-Questions

搜题

1. 搜题算法描述：
   - 通过结巴(jieba)分词器将要搜索的文本进行（精确）分词得到一个词组列表list，假设列表的长度为L,遍历题库文本向每个文本搜素list的每一个词，每查找到一个设置记录加一操作，得到每个题库文本个包含词组list中词的个数，最后返回包含词组词数目最多的题目
   - 或返回完全包含所搜索文字的题目
   ```PYTHON
       def cover(self):
        num = 0
        for i in self.str1_list:
            if i in self.str2:
                num += 1
        if self.str_qes in self.str2:
            k = 1
            return k
        return num / len(self.str1_list)
      ```
   
2.  脚本 main_server.py 运行一个小型服务器 通过浏览器搜题
      ![](https://cdn.jsdelivr.net/gh/xx025/cloudimg/img/20210630121138.png)
    ![](https://cdn.jsdelivr.net/gh/xx025/cloudimg/img/20210630121231.png)
3. 运行前请更改config.cfg配置的路径信息

4. 项目打包`pyinstaller -D main_server.py`

---
Warning: this is very unsafe

https://blog.csdn.net/gramdog/article/details/79225246

有关于允许跨域和http和http混合加载的安全策略的阻止方法


Chrome   
添加启动项：
右键点击Chrome快捷方式，在目标一栏后添加启动项

允许跨域：
--disable-web-security --user-data-dir

允许mix-content：
--allow-running-insecure-content


Fire Fox   
进入选项配置
地址栏输入about:config
允许跨域：
security.fileuri.strict_origin_policy改为false

允许mix-content：
security.mixed_content.block_active_content改为false

