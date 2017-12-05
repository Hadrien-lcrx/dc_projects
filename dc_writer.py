import pandas as pd
from dc_scraper import scraper
from urllib.request import urlopen
from pprint import pprint

page = urlopen('https://www.datacamp.com/courses/all')

course_dict = scraper(page)
df = pd.DataFrame(course_dict)

df.to_csv('DC_Courses.csv')
