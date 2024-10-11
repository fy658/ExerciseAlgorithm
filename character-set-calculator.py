import sys

"""

给定两个字符集合，一个是全量字符集，一个是已占用字符集，已占用字符集中的字符不能再使用。 要求输出剩余可用字符集。
输入描述
1. 输入一个字符串 一定包含@，@前为全量字符集 @后的为已占用字符集
2. 已占用字符集中的字符一定是全量字符集中的字符
3. 字符集中的字符跟字符之间使用英文逗号隔开
4. 每个字符都表示为字符+数字的形式用英文冒号分隔，比如a:1标识一个a字符
5. 字符只考虑英文字母，区分大小写
6. 数字只考虑正整型 不超过100
7. 如果一个字符都没被占用 @标识仍存在，例如 a:3,b:5,c:2@
输出描述
* 输出可用字符集
* 不同的输出字符集之间用回车换行
* 注意 输出的字符顺序要跟输入的一致，如下面用例不能输出b:3,a:2,c:2
* 如果某个字符已全部占用 则不需要再输出
输入


a:3,b:5,c:2@a:1,b:2
输出


a:2,b:3,c:2
说明
全量字符集为三个a，5个b，2个c 已占用字符集为1个a，2个b 由于已占用字符不能再使用 因此剩余可用字符为2个a，3个b，2个c 因此输出a:2,b:3,c:2

sys.stdin

sys 是Python的一个内置模块，提供了一些变量和函数，用于与Python解释器强烈耦合的对象。
stdin 是 sys 模块中的一个对象，代表标准输入流。它是一个文件对象，用于从控制台读取输入。


readline()

这是文件对象的一个方法，用于从文件（在这里是标准输入流）中读取一行文本。
它会读取直到遇到换行符（\n）为止，并返回读取的内容，包括换行符。
如果已经到达文件末尾，它会返回一个空字符串。


strip()

这是字符串对象的一个方法。
它用于删除字符串开头和结尾的空白字符（包括空格、制表符、换行符等）。
如果不传入参数，它会删除字符串两端的所有空白字符。
你也可以传入一个字符串参数，指定要删除的字符。



所以，整行代码 sys.stdin.readline().strip() 的功能是：

从标准输入（通常是键盘输入）读取一行文本。
删除这行文本开头和结尾的所有空白字符。
返回处理后的字符串。
"""
input_str = sys.stdin.readline().strip()
full_char_set, used_char_set = input_str.split("@")
full_char_list = full_char_set.split(",")
used_char_list = used_char_set.split(",")
dic_1 = {item.split(":")[0]:item.split(":")[1] for item in full_char_list}
dic_2 = {item.split(":")[0]:item.split(":")[1] for item in used_char_list}
output_dic = { k: int(v)- int(dic_2.get(k,0)) for k, v in dic_1.items()}
print(','.join([f"{s}:{t}" for s, t in output_dic.items()]))
out = ""
for e, f in output_dic.items():
    out+=e+":"+str(f)+","
print(out[:-1])