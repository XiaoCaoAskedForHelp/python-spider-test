import scrapy


class ImageSpider(scrapy.Spider):
    name = "image"
    # allowed_domains = ["magdeleine.co"]
    start_urls = ["https://magdeleine.co/page/2/"]

    url = 'https://magdeleine.co/page/%d/'
    page_num = 3
    def parse(self, response):
        div_list = response.xpath('//*[@id="primary"]/div/div[contains(@class,"photo-thumb")]')
        # print(div_list)

        for div in div_list:
            name = div.xpath('./figure/figcaption/div[1]/a/text()').extract_first()
            print(name)

        if self.page_num <= 5:
            print(self.page_num)
            new_url = format(self.url%self.page_num)
            self.page_num += 1
            yield scrapy.Request(url=new_url,callback=self.parse)
