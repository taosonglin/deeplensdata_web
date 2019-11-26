from pyecharts.charts import Bar
from random import randrange

bar=Bar()
bar.add_xaxis(["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"])
bar.add_yaxis("商家A", [randrange(0, 100) for _ in range(6)])
bar.add_yaxis("商家B", [randrange(0, 100) for _ in range(6)])
# bar.set_global_opts(Title="Bar-基本示例")

bar.render('../templates/test.html')