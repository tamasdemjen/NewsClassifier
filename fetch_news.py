import urllib.request
from datetime import datetime

datetime_str = datetime.now().strftime("%m%d%H")

urllib.request.urlretrieve("http://rss.cnn.com/rss/cnn_business.rss", "bus/cnn-bus-" + datetime_str + ".xml")
urllib.request.urlretrieve("http://rss.cnn.com/rss/cnn_allpolitics.rss", "pol/cnn-pol-" + datetime_str + ".xml")
urllib.request.urlretrieve("http://rss.cnn.com/rss/cnn_tech.rss", "tec/cnn-tec-" + datetime_str + ".xml")
urllib.request.urlretrieve("http://rss.cnn.com/rss/cnn_health.rss", "hea/cnn-hea-" + datetime_str + ".xml")
urllib.request.urlretrieve("http://rss.cnn.com/rss/cnn_showbiz.rss", "ent/cnn-ent-" + datetime_str + ".xml")
urllib.request.urlretrieve("http://feeds.washingtonpost.com/rss/business?itid=lk_inline_manual_45", "bus/wp-bus-" + datetime_str + ".xml")
urllib.request.urlretrieve("http://feeds.washingtonpost.com/rss/politics?itid=lk_inline_manual_2", "pol/wp-pol-" + datetime_str + ".xml")
urllib.request.urlretrieve("http://feeds.washingtonpost.com/rss/entertainment?itid=lk_inline_manual_53", "ent/wp-ent-" + datetime_str + ".xml")
urllib.request.urlretrieve("http://feeds.washingtonpost.com/rss/sports?itid=lk_inline_manual_29", "spo/wp-spo-" + datetime_str + ".xml")
urllib.request.urlretrieve("https://feeds.npr.org/1006/rss.xml", "bus/npr-bus-" + datetime_str + ".xml")
urllib.request.urlretrieve("https://feeds.npr.org/1014/rss.xml", "pol/npr-pol-" + datetime_str + ".xml")
urllib.request.urlretrieve("https://feeds.npr.org/1019/rss.xml", "tec/npr-tec-" + datetime_str + ".xml")
urllib.request.urlretrieve("https://feeds.npr.org/1128/rss.xml", "hea/npr-hea-" + datetime_str + ".xml")
urllib.request.urlretrieve("https://feeds.npr.org/1008/rss.xml", "ent/npr-al-" + datetime_str + ".xml")
urllib.request.urlretrieve("https://feeds.npr.org/1045/rss.xml", "ent/npr-mov-" + datetime_str + ".xml")
urllib.request.urlretrieve("http://feeds.sciencedaily.com/sciencedaily", "sci/sd-sci-" + datetime_str + ".xml")
urllib.request.urlretrieve("http://feeds.nature.com/nature/rss/current", "sci/nat-sci-" + datetime_str + ".xml")
urllib.request.urlretrieve("https://www.wired.com/feed", "tec/wir-tec-" + datetime_str + ".xml")
urllib.request.urlretrieve("https://www.macworld.com/index.rss", "tec/mw-tec-" + datetime_str + ".xml")
urllib.request.urlretrieve("https://www.pcworld.com/index.rss", "tec/pcw-tec-" + datetime_str + ".xml")
urllib.request.urlretrieve("https://www.theverge.com/rss/index.xml", "tec/ver-tec-" + datetime_str + ".xml")
urllib.request.urlretrieve("https://rss.nytimes.com/services/xml/rss/nyt/Business.xml", "bus/nyt-bus-" + datetime_str + ".xml")
urllib.request.urlretrieve("https://rss.nytimes.com/services/xml/rss/nyt/Politics.xml", "pol/nyt-pol-" + datetime_str + ".xml")
urllib.request.urlretrieve("https://rss.nytimes.com/services/xml/rss/nyt/Technology.xml", "tec/nyt-tec-" + datetime_str + ".xml")
urllib.request.urlretrieve("https://rss.nytimes.com/services/xml/rss/nyt/Science.xml", "sci/nyt-sci-" + datetime_str + ".xml")
urllib.request.urlretrieve("https://rss.nytimes.com/services/xml/rss/nyt/Health.xml", "hea/nyt-hea-" + datetime_str + ".xml")
urllib.request.urlretrieve("https://rss.nytimes.com/services/xml/rss/nyt/Arts.xml", "ent/nyt-a-" + datetime_str + ".xml")
urllib.request.urlretrieve("https://rss.nytimes.com/services/xml/rss/nyt/Style.xml", "ent/nyt-s-" + datetime_str + ".xml")
urllib.request.urlretrieve("https://rss.nytimes.com/services/xml/rss/nyt/Sports.xml", "spo/nyt-spo-" + datetime_str + ".xml")
urllib.request.urlretrieve("https://www.nba.com/jazz/rss.xml", "spo/nba-spo-" + datetime_str + ".xml")
urllib.request.urlretrieve("http://feeds.bbci.co.uk/news/business/rss.xml", "bus/bbc-bus-" + datetime_str + ".xml")
urllib.request.urlretrieve("http://feeds.bbci.co.uk/news/politics/rss.xml", "pol/bbc-pol-" + datetime_str + ".xml")
urllib.request.urlretrieve("http://feeds.bbci.co.uk/news/technology/rss.xml", "tec/bbc-tec-" + datetime_str + ".xml")
urllib.request.urlretrieve("http://feeds.bbci.co.uk/news/science_and_environment/rss.xml", "sci/bbc-sci-" + datetime_str + ".xml")
urllib.request.urlretrieve("http://feeds.bbci.co.uk/news/health/rss.xml", "hea/bbc-hea-" + datetime_str + ".xml")
urllib.request.urlretrieve("http://feeds.bbci.co.uk/news/entertainment_and_arts/rss.xml", "ent/bbc-ent-" + datetime_str + ".xml")
urllib.request.urlretrieve("http://feeds.bbci.co.uk/sport/rss.xml?edition=uk", "spo/bbc-spo-" + datetime_str + ".xml")
urllib.request.urlretrieve("https://news.google.com/news/rss/headlines/section/topic/BUSINESS?ned=us&hl=en", "bus/goo-bus-" + datetime_str + ".xml")
urllib.request.urlretrieve("https://news.google.com/news/rss/headlines/section/topic/POLITICS?ned=us&hl=en", "pol/goo-pol-" + datetime_str + ".xml")
urllib.request.urlretrieve("https://news.google.com/news/rss/headlines/section/topic/TECHNOLOGY?ned=us&hl=en", "tec/goo-tec-" + datetime_str + ".xml")
urllib.request.urlretrieve("https://news.google.com/news/rss/headlines/section/topic/SCIENCE?ned=us&hl=en", "sci/goo-sci-" + datetime_str + ".xml")
urllib.request.urlretrieve("https://news.google.com/news/rss/headlines/section/topic/HEALTH?ned=us&hl=en", "hea/goo-hea-" + datetime_str + ".xml")
urllib.request.urlretrieve("https://news.google.com/news/rss/headlines/section/topic/ENTERTAINMENT?ned=us&hl=en", "ent/goo-ent-" + datetime_str + ".xml")
urllib.request.urlretrieve("https://www.espn.com/espn/rss/news", "spo/espn-spo-" + datetime_str + ".xml")
urllib.request.urlretrieve("https://www.espn.com/espn/rss/nfl/news", "spo/espn-nfl-" + datetime_str + ".xml")
urllib.request.urlretrieve("https://www.espn.com/espn/rss/nba/news", "spo/espn-nba-" + datetime_str + ".xml")
urllib.request.urlretrieve("https://www.espn.com/espn/rss/mlb/news", "spo/espn-mlb-" + datetime_str + ".xml")
urllib.request.urlretrieve("https://www.espn.com/espn/rss/nhl/news", "spo/espn-nhl-" + datetime_str + ".xml")
urllib.request.urlretrieve("https://www.espn.com/espn/rss/rpm/news", "spo/espn-rpm-" + datetime_str + ".xml")
urllib.request.urlretrieve("https://www.espn.com/espn/rss/soccer/news", "spo/espn-soc-" + datetime_str + ".xml")
urllib.request.urlretrieve("https://www.espn.com/espn/rss/ncf/news", "spo/espn-ncf-" + datetime_str + ".xml")
