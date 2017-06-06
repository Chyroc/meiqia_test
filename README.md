# meiqia_test

## 思路
- 使用`scrapy`作为爬取工具，`jieba`作为分词工具
- 爬取虎扑最近30天nba新闻（`https://voice.hupu.com/nba`）
- 爬取球员信息（`https://nba.hupu.com/players`）
- 统计出现次数最多的100位球员

## 爬取虎扑最近30天nba新闻
- `cd hupu && scrapy crawl news`
