import scrapy

class CourtScraper(scrapy.Spider):
  name = 'cases'

  
  abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
  url= "https://courtconnect.courts.delaware.gov/cc/cconnect/ck_public_qry_cpty.cp_personcase_srch_details?backto=P&soundex_ind=&partial_ind=checked&last_name=a&last_name=a&first_name=&middle_name=&begin_date=08-AUG-2022&end_date=09-AUG-2022&case_type=ALL&id_code=&PageNo=1"
  start_urls = ["https://courtconnect.courts.delaware.gov/cc/cconnect/ck_public_qry_cpty.cp_personcase_srch_details?backto=P&soundex_ind=&partial_ind=checked&last_name=%s&last_name=%s&first_name=&middle_name=&begin_date=08-AUG-2022&end_date=09-AUG-2022&case_type=ALL&id_code=&PageNo=1" % (x,x) for x in abc]



  def parse(self,response):
    rows = response.xpath('/html/body/font[1]/table[2]/tr')
    for i in range(1,len(rows)):
      yield{
        'id': rows[i].xpath('td[1]/text()').extract()[0] ,
        'name':rows[i].xpath('td[2]/text()').extract()[0],
        'address':rows[i].xpath('td[3]/text()').extract()[0],
        'party type':rows[i].xpath('td[4]/text()').extract()[0],
        'party end date':rows[i].xpath('td[5]/text()').extract()[0],
        'filing date':rows[i].xpath('td[6]/text()').extract()[0],
        'case status':rows[i].xpath('td[7]/text()').extract()[0]
      }
    next_page = response.xpath('//a[contains(text(), "Next")]')
    if next_page is not None:
      yield response.follow( response.xpath('//a[contains(text(), "Next")]').attrib['href'], callback=self.parse)
      