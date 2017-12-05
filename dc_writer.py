import pandas as pd
from dc_scraper import scraper
from urllib.request import urlopen

page = urlopen('https://www.datacamp.com/courses/all')

# Get course dictionary
course_dict = scraper(page)

# Create dataframe
df = pd.DataFrame(course_dict)

# Export to csv
df.to_csv('DC_Courses.csv')
