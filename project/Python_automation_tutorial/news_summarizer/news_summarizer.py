from re import X
from bs4 import BeautifulSoup
from matplotlib.pyplot import text
from requests import get


# Creating a Function to Extract only Text from <P> Tags

def get_only_text(url):
    # Return the title and the text of the article at the specified url
    page =get(url)
    soup = BeautifulSoup(page.content, "lxml")
    text=' '.join(map(lambda p: p.text , soup.find_all('p')))
    # text = soup.text
    
    title = str(' '.join(soup.title.stripped_strings))
    return title,text

# Calling the function with the url
# print('vui long nhap duong link: ')
# x= input()
# text=get_only_text(x)
text = get_only_text('https://www.vox.com/2022/2/21/22936218/inflation-biden-midterms-democrats')

#number of worrds text
print(text[0]);
print(len(str.split(text[1])))