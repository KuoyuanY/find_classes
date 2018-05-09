# find_classes
Finds easiest gen ed classes from UMD schedule website

## setup
git clone this repository
```
git clone https://github.com/yellgreniff/find_classes.git
```
cd into it
```
cd find_classes
```
download python3 first

then install beautifulSoup4 using pip/pip3

## usage
```
python3 parse.py -s fall -y 2018 -c DSHU,DVUP
```
-s represents semester, values: fall, winter, summer, spring

-y represents year

-c represents gen ed categories(separated by comma, no space)
