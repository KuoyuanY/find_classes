from BeautifulSoup import BeautifulSoup
import urllib2
import sys



def main():
    #python parse.py -s fall -y 2018 -c DSHS,DVUP
    #-s : season, eg. fall, spring, summer, winter
    #-y : year, eg. 2018, 2019, etc
    #-c : gen ed categories, eg. DVUP, DSHS, etc. SEPARATED BY comma
    # if any gen ed is okay, enter all for -c
    argc = len(sys.argv)
    if argc < 7:
        sys.exit("insufficient arguments...")
    else:
        try:
            season = switch(sys.argv[2])
        except:
            sys.exit("please enter a correct value for season")

        year = sys.argv[4]
        geneds = sys.argv[6].split(",")

        first_gened = geneds[0]


        url = 'https://app.testudo.umd.edu/soc/gen-ed/' + year + season + '/' + first_gened

        try:
            response = urllib2.urlopen(url)
        except:
            sys.exit("are you sure you entered the year and geneds correctly?\nare those values valid?")
        
        html = response.read()
        print(html)
        parsed_html = BeautifulSoup(html)
        #print parsed_html.body.find('div', attrs={'class':'toc'})

def switch(season):
    return {
        'fall': '08',
        'summer': '05',
        'spring': '01',
    }[season.lower()]

if __name__ == "__main__":
    main()
