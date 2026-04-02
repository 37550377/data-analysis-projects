import pandas as pd
import pymysql
from my_opts import *
# 连接数据库
coon = pymysql.connect(
    host = 'localhost',
    user = 'root',
    passwd = '123456',
    database='xjnd',
    charset = 'utf8',
    port = 3306
)

# 提取信息
curses = coon.cursor()
curses.execute('use xjnd')
curses.execute('select `商品名称`,`第一数量`,`人民币` from wzbk')
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

# 按照top10商品交易总金额排序
top10_info = df_data.sort_values(by='交易额',ascending=False,inplace=False).reset_index().iloc[:10]
# print(top10_info)

# 加入新列top10商品在总金额中占比
top10_info['金额占比'] = round((top10_info['交易额']/top10_info['交易额'].sum())*100,2)
# print(top10_info)

# 商品名处理
name_list = []
for x in top10_info['商品名称']:
    if x == '未精梳单纱，棉≥85％，125分特≤细度＜192.31分特':
        name = '未精192'
        name_list.append(name)
    else:
        name = x[:2] + x[-2:]
        name_list.append(name)

# print(name_list)
name_list = name_list[::-1]
# 可视化需求 名称,数量,金额,占比
proportion_list = top10_info["金额占比"].tolist()[::-1]
total = round((top10_info['交易额']/10000),2).tolist()[::-1]
quantity = top10_info["数量"].tolist()[::-1]
