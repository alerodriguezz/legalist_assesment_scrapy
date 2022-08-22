# legalist_assesment_scrapy
Scrapes multiple court pages using scrapy.



To start clone this repo into the ide of your choice.
I recommend running this in a python virtual environment. This can be done using virtualenv or the virtual environment library of your choice.

To start a virtual environment using virtualenv type these commands in your terminal.
To instantiate your environment...

```
virtualenv venv
```
To activate it...
```
. venv/bin/activate
```

install the necessary packages by using 
```
pip3 install -r requirements.txt
```

to run the program...

make sure that you cd into the scrapy directory person_case
```
cd person_case
```

once you are in, run the command
```
scrapy crawl cases
```

use this command to see a visual of the data that was pulled 
```
scrapy crawl cases -O sample.json
```

**Important** in order to ***adjust data timeframe*** traverse into the directory legalist_assesment_scrapy/person_case/person_case/spiders/scraper_1.py and edit the variables ***start*** and ***end*** found in the list comprehension ***start_urls*** in line 8.  NOTE: dates MUST be in DD-MON-YYYY format
```
start_urls = ["https://courtconnect.courts.delaware.gov/cc/cconnect/ck_public_qry_cpty.cp_personcase_srch_details?backto=P&soundex_ind=&partial_ind=checked&last_name={i}&last_name={i}&first_name=&middle_name=&begin_date={start}&end_date={end}&case_type=ALL&id_code=&PageNo=1".format(i=x,start="08-AUG-2022",end="09-AUG-2022") for x in abc]

```

## architecture

I kept things minimal for this scraper and used only **scrapy** for the entire piepline. scrapy retrieved, parsed, and relayed the information to the **sqlite3** file myData_1.db that is output once the program finishes running.

