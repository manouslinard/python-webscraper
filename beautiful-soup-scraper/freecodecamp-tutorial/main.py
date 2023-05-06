from bs4 import BeautifulSoup

with open('home.html', 'r') as html_file:
    content = html_file.read()
    # print(content)
    soup = BeautifulSoup(content, 'lxml')

    course_cards = soup.find_all('div', class_='card')  # takes all div elements with class 'card'.
    for course in course_cards:
        course_name = course.h5.text    # gets the text of selected h5.
        course_price = course.a.text.split()[-1]    # same here but with anchor - gets directly the price.

        print(f'{course_name} costs {course_price}')
