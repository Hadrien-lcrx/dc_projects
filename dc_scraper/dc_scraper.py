from bs4 import BeautifulSoup
from collections import OrderedDict

def scraper(page):
    """
    This function takes in the page showing all DataCamp courses, and outputs
    a dictionary containing a list of course titles, urls, technologies and
    instructors. This dictionary can then be use to create a DataFrame, and
    exported to a csv.
    """

    # Initialize empty lists
    titles = []
    urls = []
    techs = []
    instructors = []

    # Start scraper and get course blocks
    soup = BeautifulSoup(page, 'html')
    div = soup.findAll("div", { "class": "course-block"})

    # Loop over all courses
    for element in div:
        a = element.find("a", { "class": "course-block__link"})

        # Get url
        url = 'https://www.datacamp.com' + a.get('href')

        # Get tech
        if a.contents[1].get("class")[1] == 'course-block__technology--r':
            tech = 'R'
        elif a.contents[1].get("class")[1] == 'course-block__technology--python':
            tech = 'Python'
        elif a.contents[1].get("class")[1] == 'course-block__technology--sql':
            tech = 'SQL'
        elif a.contents[1].get("class")[1] == 'course-block__technology--git':
            tech = 'Git'
        elif a.contents[1].get("class")[1] == 'course-block__technology--shell':
            tech = 'Shell'

        # Get title
        title = [element.get_text() for element in a.select("h4")][0]

        # Get instructor
        instructor_div = element.find("div", { "class": "course-block__author-body"})
        instructor = [element.get_text() for element in instructor_div.select("p")][0]

        # Write information in lists
        titles.append(title)
        urls.append(url)
        techs.append(tech)
        instructors.append(instructor)

    # Write ordered dictionary and return it
    courses = OrderedDict({'Course': titles,
                           'URL': urls,
                           'Tech': techs,
                           'Instructor': instructors})

    return courses
