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

## architecture

I kept things minimal for this scraper and used only **scrapy** for the entire piepline. scrapy retrieved, parsed, and relayed the information to the **sqlite3** file myData_1.db that is output once the program finishes running.