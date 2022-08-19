import scrapy

class CourtScraper(scrapy.Spider):
  name = 'cases'
  abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
  #list comprehension feeds urls of cases from a to 
  #fill in start and end variables with desired start and end dates respectively. NOTE: dates MUST be in DD-MON-YYYY format as shown in the sample dates I have put
  start_urls = ["https://courtconnect.courts.delaware.gov/cc/cconnect/ck_public_qry_cpty.cp_personcase_srch_details?backto=P&soundex_ind=&partial_ind=checked&last_name={i}&last_name={i}&first_name=&middle_name=&begin_date={start}&end_date={end}&case_type=ALL&id_code=&PageNo=1".format(i=x,start="08-AUG-2022",end="09-AUG-2022") for x in abc]



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
      