# meiqia_test

## 题目
分析虎扑nba频道最近1个月的新闻，找到最常出现的100个名字

## 思路
- 使用`scrapy`作为爬取工具，`jieba`作为分词工具
- 爬取虎扑最近30天nba新闻（`https://voice.hupu.com/nba`）
- 爬取球员信息（`https://nba.hupu.com/players`）
- 统计出现次数最多的100位球员

## 爬取虎扑最近30天nba新闻
- `cd hupu && scrapy crawl news`

## 爬取球员信息
- `cd hupu && scrapy crawl players`

## 统计出现次数最多的100位球员
- `python analyze.py && cat result.json`

## 不足
### 只分析了`https://nba.hupu.com/players`内出现的球员，而不是所有名字
没有这个词库，不好分词，所以就缩小了问题，改为找最常出现的100个球员名字

### 重名问题
叫`詹姆斯`的有很多人，没有区分分别是谁
应该对`詹姆斯`出现的文本进行分析，来解决这个问题
