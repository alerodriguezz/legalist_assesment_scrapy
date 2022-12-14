# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import sqlite3

class PersonCasePipeline:
  def __init__(self):
    self.con = sqlite3.connect('myData_1.db')
    self.cur = self.con.cursor()
    self.create_table()
  def create_table(self):
    self.cur.execute("""CREATE TABLE IF NOT EXISTS cases(
    id BLOB PRIMARY KEY,
    name TEXT,
    address TEXT,
    party_type TEXT,
    party_end_date TEXT,
    filing_date TEXT,
    case_status TEXT
    )""")
    
  def process_item(self, item, spider):
    self.cur.execute("""INSERT OR IGNORE INTO cases VALUES(?,?,?,?,?,?,?)""",(item['id'],item['name'],item['address'],item['party type'],item['party end date'],item['filing date'],item['case status']))
    self.con.commit()
    return item
