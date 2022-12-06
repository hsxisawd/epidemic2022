# epidemic2022
## 项目介绍：
个人毕业设计项目，本次项目对疫情数据进行整合清洗，使用Django+vue3+mysql前后分离的形式，将疫情数据数据进行动 态可视化。设计了“全国累计病例”、“全国省份新增疫情数据 Top10柱形图 ”、“全国新增疫情数据 Top10 柱形 图”、“全国各省中高风险地区数据折线图”、“全国各省各市新增疫情情况动态饼图功”、“全国各省各市中高风险地区 数据动态折线图”、“全国各省疫情数据动态地图”和“全国各省各市疫情数据动态滚动表”’八个图表功能

## 项目架构：

2020epidemic --- 爬虫程序文件

epidemic2022 --- Django后端项目
    
webindex     --- Vue+echarts前端可视化项目

## 项目技术：
1. 使用Python requests库爬取腾讯新闻疫情数据信息
2. 使用Python PyMysql库将数据分别存入MySQL数据库对应的数据表中
3. 使用Python Pandas库对数据进行数据清洗和数据处理分析
4. 使用Python web开发框架Django开发设计API数据接口
5. 使用web开发框架Vue3搭建每个功能模块组件
6. 使用axios请求后端数据接口
7. 使用Echarts图表组件创建数据图表
