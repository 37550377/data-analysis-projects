import random
import pandas as pd
import pymysql
from my_opts import *
# 连接数据库
coon = pymysql.connect(
    host = 'localhost',
    user = 'root',
    passwd = '123456',
    database='xjhs',
    charset = 'utf8',
    port = 3306
)

#=========验证数据===========
# 提取信息
curses = coon.cursor()
curses.execute('use xjhs')
curses.execute('select `商品名称`,`第一数量`,`人民币` from oddc')
raw_trade = curses.fetchall()
coon.close()

#转换成dataframe
df_trade = pd.DataFrame(raw_trade,columns=['商品名称','数量','交易额'])
# print(df_trade.head(),df_trade.info(),df_trade.shape)
# 2 交易额 127 non - null object         交易额是object单独处理

# 正则剔除
df_trade['交易额'] = df_trade['交易额'].str.strip().str.replace(r'\D','',regex=True).astype('int64')

# 十个月数据统计
df_data = df_trade.groupby('商品名称').agg({'数量':'sum','交易额':'sum'}).reset_index()

pd.set_option('display.max_rows', None)
# 未知数据分布用iqr
fiqr_num = iqr_false(df_data,"数量",1.5,3)
# print(fiqr_num)

# 数量非iqr内商品过于多，抽样调查
random.seed(42)
n_rows = len(fiqr_num)
random_index_n = random.sample(range(n_rows),10)
# print(fiqr_num.iloc[random_index_n])
#                               商品名称       数量        交易额
# 2539    设计为仅使用发光二极管（LED）光源的圣诞树用的灯串   360794    8599359
# 479                   其他棉制针织或钩编的手套  4342036   11643964
# 163                以塑料片或纺织材料作面的手提包  2528201  147455074
# 973                          单喇叭音箱   730673   44458788
# 936                  化纤制盥洗及厨房用织物制品  3744742   13281837
# 895   加工中密度板，密度＞0.8g/cm3，5mm＜厚≤9mm   593068    2785188
# 565                       其他电热理发器具  1318237   54080289
# 463                      其他材料制活动房屋  1753193   17556806
# 2730         镁、钙或铬单项或合计＞50%的耐火砖、瓦等   803021    6992529
# 2070                熔断器，线路电压≤1000V   499014     958697


# 数值不在iqr范围内的数量信息和金额信息，求单价
table_n = iqr_false(df_data,"交易额",1.5,3).copy()
num = iqr_false(df_data,"交易额",1.5,3)['数量']
money = iqr_false(df_data,"交易额",1.5,3)['交易额']
table_n['单价'] = (money.to_numpy()/num.to_numpy()).astype('int64')
# print(table_n[['商品名称','单价']])

# 金额非iqr内商品过于多，抽查10条查看，做标记
m_rows = len(table_n)
random_index_m = random.sample(range(m_rows),10)
# print(table_n[['商品名称','单价']].iloc[random_index_m])

#                                                    商品名称       单价
# 533                                               其他玻璃杯       24
# 140           仅装有点燃式活塞内燃发动机的小客车（9座及以下），1000cc＜排量≤1500cc    78089
# 1088  同时装有点燃式活塞内燃发动机及驱动电动机的主要用于载人的越野车（4轮驱动），1000cc＜排...   251332
# 1041                                   合成纤维制染色其他针织或钩编织物        8
# 994                  厚度小于1.5毫米的涂漆或涂塑的铁或非合金钢平板轧材，宽≥600mm        4
# 684                                   其他节日或娱乐用品，包括魔术道具等       26
# 485                                  其他橡胶或塑料制外底及鞋面的过踝鞋靴       61
# 2561                                         贱金属制铰链（折叶）       21
# 429                                   其他有接头电导体，额定电压≤80V       34
# 2871                                             龙门式起重机  1300636

# ==============核实数据完毕===============
