from pyecharts import options
from pyecharts.charts import Bar,Line,Grid,Pie
from pyecharts.globals import ThemeType
from pyecharts.options import *
from wz_preprocessing import *
bar = Bar()
line = Line()
bar_x_list = name_list
bar_y_list = quantity
bar.add_xaxis(bar_x_list)
bar.add_yaxis('top10交易金额的商品的交易数量',bar_y_list,yaxis_index=0)
bar.extend_axis()
bar.set_global_opts(
    xaxis_opts=AxisOpts(
        axislabel_opts=LabelOpts(
            interval=0,
            is_show=True,
            font_size=12,
            rotate=20,
            text_width=6,
            overflow="truncate"),
    ),
    title_opts=TitleOpts(title="新疆对乌兹别克斯坦交易金额出口数据分析"),
    toolbox_opts=ToolboxOpts(is_show=True),
    legend_opts=LegendOpts(is_show=True,pos_left="50%",pos_top="5%"),
)
grid = Grid(init_opts=InitOpts(width="1200px",height="700px",theme=ThemeType.MACARONS))
grid.add(bar, grid_opts=GridOpts(pos_left="50%", pos_right="0%"))

line_y_list = total
line.add_xaxis(bar_x_list)
line.add_yaxis('top10交易金额的商品的交易金额(万)',line_y_list,yaxis_index=1)
line.set_global_opts(
    xaxis_opts=AxisOpts(axislabel_opts=LabelOpts(
            interval=0,
            is_show=False,
            font_size=12,
            rotate=20,
            text_width=6,
            overflow="truncate")),
    yaxis_opts=AxisOpts(
        name='交易数量',
        position='right',
        is_show=True
    ),
    legend_opts=LegendOpts(is_show=True,pos_left="70%",pos_top="5%"),
)
grid.add(line, grid_opts=GridOpts(pos_left="50%", pos_right="0%"))



pie = Pie(init_opts=InitOpts(theme=ThemeType.BUILTIN_THEMES))
pie.add('top10交易金额的商品内部占比',
        [i for i in zip(bar_x_list, proportion_list)],
         center=['20%','40%'],
        radius=["40%","60%"],
        label_opts=LabelOpts(
            interval=0,
            is_show=True,
            font_size=12,
            formatter='{b}:{c}%',
            position="outer"
        ),
)
pie.set_global_opts(
        legend_opts=LegendOpts(type_="scroll", pos_left="35%", pos_bottom='10%',orient="vertical"),
    )

grid.add(pie,grid_opts=GridOpts())
grid.render("新疆对乌兹别克斯坦交易金额出口数据分析.html")
