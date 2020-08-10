import xml.etree.ElementTree as et
import pandas as pd
import os
import re

################################################################################

class HtmlCleaner:
   def __init__(self):
      self.re_tags = re.compile("<.*?>") # HTML tags
      self.re_entities = re.compile("&([a-z0-9]+|#[0-9]{1,6}|#x[0-9a-f]{1,6});") # &xxx; entities
      self.re_nbsp = re.compile("&(nbsp|#160|#xA0|#xa0);") # &nbsp;
      self.re_amp = re.compile("&(amp|#38|#x26);") # &amp;
      self.re_quot = re.compile("&(quot|#34|#x22);") # &quot;
      self.re_apos = re.compile("&(apos|#39|#x27);") # &apos;
      self.re_lt = re.compile("&(lt|#60|#x3C|#x3c);") # &lt;
      self.re_gt = re.compile("&(gt|#62|#x3E|#x3e);") # &gt;
      self.re_agrave = re.compile("&(agrave|#224|#xE0|#xe0);")
      self.re_egrave = re.compile("&(egrave|#232|#xE8|#xe8);")
      self.re_eacute = re.compile("&(eacute|#233|#xE9|#xe9);")

   def clean_html(self, s):
      """
      Converts simple HTML to text. This is good enough for our purposes,
      as RSS files don't contain full HTML files, scripts, CSS, etc.
      """
      # Note: We only support US ASCII, generally no French, Italian, German,
      # Eastern European, etc. Exceptions: de'ja' vu, cre'me, cliche', voila'
      if s == "":
         return s
      s = self.re_tags.sub(" ", s) # remove tags
      s = self.re_nbsp.sub(" ", s) # &nbsp; to space
      s = self.re_amp.sub("&", s) # &amp; to &
      s = self.re_lt.sub("<", s) # &lt; to <
      s = self.re_gt.sub(">", s) # &gt; to >
      s = self.re_agrave.sub("\u00E0", s) # &agrave; to \xE0
      s = self.re_egrave.sub("\u00E8", s) # &egrave; to \xE8
      s = self.re_eacute.sub("\u00E9", s) # &eacute; to \xE9
      s = self.re_entities.sub('', s) # remove all remaining &xxx; entities
      s = ' '.join(s.split()) # replace multiple whitespaces with a single space
      return s

################################################################################

def validate_channel_title(channel_title, source, cat):
   sourcecat = source + "-" + cat
   valid =(sourcecat == "bbc-bus" and channel_title == "BBC News - Business") or \
          (sourcecat == "cnn-bus" and channel_title == "CNN.com - RSS Channel - Business") or \
          (sourcecat == "goo-bus" and channel_title == "Business - Latest - Google News") or \
          (sourcecat == "npr-bus" and channel_title == "Business : NPR") or \
          (sourcecat == "nyt-bus" and channel_title == "NYT > Business") or \
          (sourcecat == "wp-bus" and channel_title == "Business") or \
          (sourcecat == "bbc-ent" and channel_title == "BBC News - Entertainment & Arts") or \
          (sourcecat == "cnn-ent" and channel_title == "CNN.com - RSS Channel - Entertainment") or \
          (sourcecat == "goo-ent" and channel_title == "Entertainment - Latest - Google News") or \
          (sourcecat == "npr-al" and channel_title == "Arts & Life : NPR") or \
          (sourcecat == "npr-mov" and channel_title == "Movies : NPR") or \
          (sourcecat == "nyt-a" and channel_title == "NYT > Arts") or \
          (sourcecat == "nyt-s" and channel_title == "NYT > Fashion") or \
          (sourcecat == "wp-ent" and channel_title == "Arts & Entertainment") or \
          (sourcecat == "bbc-hea" and channel_title == "BBC News - Health") or \
          (sourcecat == "cnn-hea" and channel_title == "CNN.com - RSS Channel - App Health Section") or \
          (sourcecat == "goo-hea" and channel_title == "Health - Latest - Google News") or \
          (sourcecat == "npr-hea" and channel_title == "Health : NPR") or \
          (sourcecat == "nyt-hea" and channel_title == "NYT > Health") or \
          (sourcecat == "bbc-pol" and channel_title == "BBC News - UK Politics") or \
          (sourcecat == "cnn-pol" and channel_title == "CNN.com - RSS Channel - Politics") or \
          (sourcecat == "goo-pol" and channel_title == "Politics - Executive - Google News") or \
          (sourcecat == "npr-pol" and channel_title == "Politics : NPR") or \
          (sourcecat == "nyt-pol" and channel_title == "NYT > U.S. > Politics") or \
          (sourcecat == "wp-pol" and channel_title == "Politics") or \
          (sourcecat == "bbc-sci" and channel_title == "BBC News - Science & Environment") or \
          (sourcecat == "goo-sci" and channel_title == "Science - Latest - Google News") or \
          (sourcecat == "nat-sci" and channel_title == "Nature - Issue - nature.com science feeds") or \
          (sourcecat == "nyt-sci" and channel_title == "NYT > Science") or \
          (sourcecat == "sd-sci" and channel_title == "Latest Science News -- ScienceDaily") or \
          (sourcecat == "bbc-spo" and channel_title == "BBC Sport - Sport") or \
          (sourcecat == "espn-mlb" and channel_title == "www.espn.com - MLB") or \
          (sourcecat == "espn-nba" and channel_title == "www.espn.com - NBA") or \
          (sourcecat == "espn-ncf" and channel_title == "www.espn.com - NCF") or \
          (sourcecat == "espn-nfl" and channel_title == "www.espn.com - NFL") or \
          (sourcecat == "espn-nhl" and channel_title == "www.espn.com - NHL") or \
          (sourcecat == "espn-rpm" and channel_title == "www.espn.com - RPM") or \
          (sourcecat == "espn-soc" and channel_title == "www.espn.com - SOCCER") or \
          (sourcecat == "espn-spo" and channel_title == "www.espn.com - TOP") or \
          (sourcecat == "nba-spo" and channel_title == "Utah Jazz") or \
          (sourcecat == "nyt-spo" and channel_title == "NYT > Sports") or \
          (sourcecat == "wp-spo" and channel_title == "Sports") or \
          (sourcecat == "bbc-tec" and channel_title == "BBC News - Technology") or \
          (sourcecat == "cnn-tec" and channel_title == "CNN.com - RSS Channel - App Tech Section") or \
          (sourcecat == "goo-tec" and channel_title == "Technology - Latest - Google News") or \
          (sourcecat == "mw-tec" and channel_title == "Macworld") or \
          (sourcecat == "npr-tec" and channel_title == "Technology : NPR") or \
          (sourcecat == "nyt-tec" and channel_title == "NYT > Technology") or \
          (sourcecat == "pcw-tec" and channel_title == "PCWorld") or \
          (sourcecat == "ver-tec" and channel_title == "The Verge -  All Posts") or \
          (sourcecat == "wir-tec" and channel_title == "Feed: All Latest")



   if not valid:
      print("(" + sourcecat + "|" + channel_title + ")")
      raise Exception("Channel title doesn't match file name")

################################################################################

def get_child_text(node, name):
   try:
      text = next(node.iter(name)).text
      if not isinstance(text, str):
         return ""
      else:
         return text
   except StopIteration:
      return ""

def merge_cat(prev_cat, new_cat):
   """
   Order: hea pol sci tec spo bus ent
   hea > pol; health realted to politics => that's still about health (example: congressman dies of coronavirus; flu vaccine offered to people)
   hea > ent; health related to entertainment => that's still about health
   hea > spo; health related to sports => that's still about health (example: exercise)
   hea > sci/tec; science/tech related to health => that's still about health (example: gene editing, fitness apps)
   pol > bus; business realted to politics => that's still about politics (example: coronavirus aid; small business bailout)
   pol > spo; sports realted to politics => that's still about politics (example: Trump playing golf)
   pol > ent; entertainment realted to politics => that's still about politics (example: George Floyd art)
   sci > tec; tech realted to science => that's still about science (example: mission to Mars)
   ent > tec; tech realted to entertainment => that's still about tech (example: entertainment apps)
   spo > ent; movie about sports => we'll categorize it as sports (example: a movie about hockey, football)
   tec > bus; business realted to tech => that's still about tech (example: Apple, Ford release products)
   bus > ent; business realted to entertainment => that's still about business (example: museum layoffs are about layoffs, not about art; Lord & Taylor bankruptcy is financial, not style)
   business is a catch-all phrase, almost anything can be categorized as business, but business only really wins over entertainment, otherwise we could call everything a business
   """
   if new_cat == "hea" or prev_cat == "hea":
      return "hea"
   elif new_cat == "pol" or prev_cat == "pol":
      return "pol"
   elif new_cat == "sci" or prev_cat == "sci":
      return "sci"
   elif new_cat == "tec" or prev_cat == "tec":
      return "tec"
   elif (new_cat in ["spo", "mlb", "nba", "ncf", "nfl", "nhl", "rpm", "soc"]) or (prev_cat in ["spo", "mlb", "nba", "ncf", "nfl", "nhl", "rpm", "soc"]):
      return "spo"
   elif new_cat == "bus" or prev_cat == "bus":
      return "bus"
   else:
      return "ent"

class RSSAggregator:
   def __init__(self):
      self.news_arr = []
      self.guids = dict() # key: guid string; value: new_arr index
      self.guidsCats = dict() # key: guid string; value: set of catogories

   def read(self, pathname, source, cat):
      root = et.parse(pathname).getroot()
      #print(root.tag)
      if root.tag == "rss":
         channel = next(root.iter("channel"))
         channel_title = get_child_text(channel, "title")
         validate_channel_title(channel_title, source, cat)
         #print(channel_title)

         for item in channel.findall("item"):
            title = html_cleaner.clean_html(get_child_text(item, "title"))
            desc = html_cleaner.clean_html(get_child_text(item, "description"))
            link = get_child_text(item, "link")
            guid = get_child_text(item, "guid")
            date = get_child_text(item, "pubDate")
            #print(title + "; " + date)
            #print(desc)
            if guid not in self.guidsCats.keys():
               self.guidsCats[guid] = { cat }
            else:
               self.guidsCats[guid].add(cat)
            if guid not in self.guids.keys():
               self.guids[guid] = len(self.news_arr)
               self.news_arr.append([title, desc, link, guid, date, source, cat])
            else:
               index = self.guids[guid]
               if self.news_arr[index][3] != guid:
                  raise Exception("Internal index error")
               old_cat = self.news_arr[index][6]
               self.news_arr[index][6] = merge_cat(self.news_arr[index][6], cat)
               new_cat = self.news_arr[index][6]
               #if new_cat != old_cat:
               #   print("%s > %s" % (new_cat, old_cat))

      elif root.tag == "{http://www.w3.org/2005/Atom}feed":
         channel_title = get_child_text(root, "{http://www.w3.org/2005/Atom}title")
         validate_channel_title(channel_title, source, cat)
         #print(channel_title)

         for item in root.findall("{http://www.w3.org/2005/Atom}entry"):
            title = html_cleaner.clean_html(get_child_text(item, "{http://www.w3.org/2005/Atom}title"))
            desc = html_cleaner.clean_html(get_child_text(item, "{http://www.w3.org/2005/Atom}content"))
            link = get_child_text(item, "{http://www.w3.org/2005/Atom}link")
            guid = get_child_text(item, "{http://www.w3.org/2005/Atom}id")
            date = get_child_text(item, "{http://www.w3.org/2005/Atom}published")
            #print(title + "; " + date)
            #print(desc)
            if guid not in self.guids.keys():
               self.guids[guid] = len(self.news_arr)
               self.news_arr.append([title, desc, link, guid, date, source, cat])
            else:
               index = self.guids[guid]
               if self.news_arr[index][3] != guid:
                  raise Exception("Internal index error")
               old_cat = self.news_arr[index][6]
               self.news_arr[index][6] = merge_cat(self.news_arr[index][6], cat)
               new_cat = self.news_arr[index][6]
               #if new_cat != old_cat:
               #   print("%s > %s" % (new_cat, old_cat))

   def check_ambiguities(self):
      # Ambiguity: the same article is classified as multiple categories
      for guid, cats in self.guidsCats.items():
         if len(cats) > 1:
            cats_str = ""
            for cat in cats:
               if len(cats_str) > 0:
                  cats_str += " "
               cats_str += cat
            print("Ambiguity: (%s)(%d)(%s)" % (guid, len(cats), cats_str));

################################################################################


html_cleaner = HtmlCleaner()
rss_aggregator = RSSAggregator()

for (dirpath, dirnames, filenames) in os.walk("."):
   for filename in filenames:
      pathname = os.path.join(dirpath, filename)
      if filename.endswith(".xml"):
         #print(pathname)
         parts = filename.split("-")
         source = parts[0]
         cat = parts[1]

         rss_aggregator.read(pathname, source, cat)
# rss_aggregator.check_ambiguities()

#pathname = "bus/bbc-bus-072715.xml"
#pathname = "ent/cnn-ent-072717.xml"
#pathname = "tec/ver-tec-072715.xml"
#filename = os.path.basename(pathname)
#parts = filename.split("-")
#source = parts[0]
#cat = parts[1]

#rss_aggregator.read(pathname)

news_df = pd.DataFrame(rss_aggregator.news_arr, columns = ["title", "desc", "link", "guid", "date", "source", "cat"])
print(news_df.head())
print(news_df.shape)

"""
We don't need that many categories, we can reduce them to 6:
bus: business
pol: politics
tec: technology
hea: health
ent: entertainment, movies, art, style, fashion, lifestyle
spo: sports
"""
fewer_cats = { 
   'al': 'ent',
   'mov': 'ent',
   'a': 'ent',
   's': 'ent',
   'mlb': 'spo',
   'nba': 'spo',
   'ncf': 'spo',
   'nfl': 'spo',
   'nhl': 'spo',
   'rpm': 'spo',
   'soc': 'spo' }
news_df = news_df.replace({ "cat": fewer_cats })
news_df = news_df.drop(columns=["link", "guid", "date"])
news_df.to_csv('news.csv', index=False)
