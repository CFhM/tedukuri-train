# tedukuri-train
《基础算法进阶指南》训练，提供系列工具直接拉取线上题库，生成样例，以及校验样例结果、与标程对比单个样例或进行多轮随机数据的对拍。

# env requirement
## for parse online problem set
- python 3.6+
  - bs4 `conda install beautifulsoup4`
- jdk
## for judgement
- python 3.6+
- c++ compiler (recommend g++)

# usage
## parse online problem set
以下操作会拉取[这个题库](http://noi-test.zzstep.com/contest?type=1)下的题目，按照层级建立文件夹，并默认生成solution.cpp，在第一行注释标明题目链接，拉取题目中的样例输入输出，分别为该文件夹下的test.in和test.out
``` shell
# make sure there's no folder names "Problems" in your working directory
python ./parse_probs.py
```
## solve problems
以下操作均可参考`a\^b`题目目录下的示例
> ！注意 以下操作均要在题目目录内进行
### 样例测试
- 编写solution.cpp
- 默认样例输入为test.in，样例输出为test.out
```shell
python ../../../judge.py solution.cpp
```
- 推荐在`~/.bash_profile`或你的环境配置目录下添加 `alias jud="python ../../../judge.py solution.cpp"`，每次`jud`即可
### 单组输入对拍标程
- 编写solution.cpp
- 默认样例输入为test.in，样例输出为test.out，标程为std.cpp
```shell
python ../../../judge.py solution.cpp -s std.cpp
```
- 推荐在`~/.bash_profile`或你的环境配置目录下添加 `alias cmp="python ../../../judge.py solution.cpp -s std.cpp"`，每次`cmp`即可
### 多轮随机数据对拍标程
- 编写solution.cpp
- 编写数据生成脚本gen.py，并将结果输出到gen.in
- 默认标程为std.cpp，测试轮数为100轮
```shell
python ../../../judge.py solution.cpp -s std.cpp -g gen.py -r 100 -i gen.in
```
- 推荐在`~/.bash_profile`或你的环境配置目录下添加 `alias pai="python ../../../judge.py solution.cpp -s std.cpp -g gen.py -r 100 -i gen.in"`，每次`pai`即可
