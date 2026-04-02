"""
此文件存放个人数据处理函数
"""

def three_c_false(x,y):
    '''
    x: pd.DataFrame
    y: Columns
    return: 非3c范围内内容的行
    '''
    mean =  x[y].to_numpy().mean()
    std = x[y].to_numpy().std()
    upper = mean + 3*std
    lower = mean - 3*std
    return x[(x[y]>=upper) | (x[y]<=lower)]
    
def iqr_false(x,y,z=1.5,q=1.5):
    '''
    x: pd.DataFrame
    y:  columns
    z: lower 的 z倍iqr
    q: upper 的 q倍iqr
    :return:  非iqr范围内内容的行
    '''
    q1 = x[y].quantile(0.25)
    q3 = x[y].quantile(0.75)
    iqr = q3 - q1
    lower = q1 - z*iqr
    upper = q3 + q*iqr
    return x[(x[y]>=upper) | (x[y]<=lower)]

def re_int_false(x,y,z):
    """
    剔除列中非数字部分，转换目标类型
    x:pd.DataFrame
    y:columns
    z:需要转换的类型，在astype里面
    :return: 列中数字部分
    """
    return x[y].str.strip().str.replace(r'\D', '', regex=True).astype(z).copy()
