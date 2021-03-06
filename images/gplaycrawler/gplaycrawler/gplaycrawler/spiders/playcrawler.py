from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from gplaycrawler.items import GplaycrawlerItem
import urlparse

class MySpider(CrawlSpider):
  name = "playcrawler"
  allowed_domains = ["play.google.com"]
  start_urls = ["https://play.google.com/store/apps/"]
  rules = [Rule(LinkExtractor(allow=(r'apps',),deny=(r'reviewId')),follow=True,callback='parse_link')]
    	# r'page/\d+' : regular expression for http://isbullsh.it/page/X URLs
    	#Rule(LinkExtractor(allow=(r'apps')),follow=True,callback='parse_link')]
    	# r'\d{4}/\d{2}/\w+' : regular expression for http://isbullsh.it/YYYY/MM/title URLs
  def abs_url(url, response):
      """Return absolute link"""
      base = response.xpath('//head/base/@href').extract()
      if base:
        base = base[0]
      else:
        base = response.url
      return urlparse.urljoin(base, url)
    
  def parse_link(self,response):
      # hxs = Selector(response)
      root_titles = response.xpath('/html')
      items = []

      # if "Preregister" in response

      for titles in root_titles:
        print(titles)
        item = GplaycrawlerItem()
        item["Link"] = response.request.url
        item['Package'] = item["Link"][46:]
        item["Item_name"] = ''.join(titles.xpath('//*[@itemprop="name"]/span/text()').extract())
        item["Updated"] = ''.join(titles.xpath('//*[@class="htlgb"]/text()')[0].extract())
        item["Author"] = ''.join(titles.xpath('//*[@itemprop="author"]/a/span/text()').extract())
        item["Filesize"] = ''.join(titles.xpath('//*[@class="htlgb"]/text()')[1].extract())
        item["Downloads"] = ''.join(titles.xpath('//*[@class="htlgb"]/text()')[2].extract())
        item["Version"] = ''.join(titles.xpath('//*[@class="htlgb"]/text()')[3].extract())
        item["Compatibility"] = ''.join(titles.xpath('//*[@class="htlgb"]/text()')[4].extract())
        item["Content_rating"] = ''.join(titles.xpath('//*[@class="htlgb"]/text()')[5].extract())
        item["Author_link"] = ''.join(titles.xpath('//*[@class="T32cc UAO9ie"]/a/@href')[0].extract())
##        item["Author_link_test"] = titles.xpath('//*[@class="content contains-text-link"]/a/@href').extract()
        item["Genre"] = ''.join(titles.xpath('//*[@itemprop="genre"]/text()').extract())
        item["Price"] = ''.join(titles.xpath('//*[@class="price buy id-track-click"]/span[2]/text()').extract())
        item["Rating_value"] = ''.join(titles.xpath('//*[@class="score"]/text()').extract())
        item["Review_number"] = ''.join(titles.xpath('//*[@class="reviews-num"]/text()').extract())
        item["Description"] = ''.join(titles.xpath('//*[@class="id-app-orig-desc"]//text()').extract())
        item["IAP"] = ''.join(titles.xpath('//*[@class="htlgb"]/text()')[7].extract())
        item["Developer_badge"] = ''.join(titles.xpath('//*[@class="badge-title"]//text()').extract())
        item["Physical_address"] = ''.join(titles.xpath('//*[@class="content physical-address"]/text()').extract())
        item["Video_URL"] = ''.join(titles.xpath('//*[@class="play-action-container"]/@data-video-url').extract())
        item["Developer_ID"] = ''.join(titles.xpath('//*[@itemprop="author"]/a/@href').extract())
        items.append(item)
        yield item
      

