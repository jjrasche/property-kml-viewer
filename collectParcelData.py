import csv
from fuzzywuzzy import fuzz

# f = open('testParcelData_Lowll_4-25.csv', 'r')
reader = 0

def sameAddress(addr1, addr2):
    streetNum1 = addr1[0:4]
    streetNum2 = addr2[0:4]
    streetNumCompare = fuzz.ratio(streetNum1, streetNum2)

    wholeCompare = fuzz.token_set_ratio(addr1, addr2)
    return streetNumCompare == 100 and wholeCompare > 70
    # if (streetNumCompare == 100 and wholeCompare < 80):
    #     print addr1 + ' : ' + addr2 + ' : ' +  str(streetNumCompare) + ':' + str(wholeCompare) + ' : ' +  str(streetNumCompare == 100 and wholeCompare > 7)

def writeKMLLine(parcelData):
    style = '#rental' if parcelData[10] == True else '#homeOwner'
    str = '\t\t<Placemark>\n\t\t\t<styleUrl>{0}</styleUrl>\n\t\t\t<name>{1}</name>\n\t\t\t<Point>\n\t\t\t\t<coordinates>{2},0</coordinates>\n\t\t\t</Point>\n\t\t</Placemark>\n'\
        .format(style, parcelData[0] + ' : ' + parcelData[1] + ' : ' + parcelData[7], parcelData[2])
    # kmlFile.write(str)
    return str


with open('testParcelData_Lowell_4-25.csv', 'r+w') as csvFile:
    reader = csv.reader(csvFile, delimiter=',', quotechar='"')
    for row in reader:
        t = row
        homeOwner = sameAddress(row[1], row[4])
        t[10] = False if homeOwner else True
        print(writeKMLLine(t))


# ['41-20-02-354-035', '151 S WEST AVE SE', '-85.350078', ' 42.930317', 'KROHN ALBERT', '151 WEST ST S NE LOWELL', ' MI 49331', '0.30', 'ACTIVE', '401 - RESIDENTIAL - IMPROVED', 'False', '48', '763', 'True']
# ['41-20-02-354-035', '151 S WEST AVE SE', '"-85.350078', ' 42.930317"', 'KROHN ALBERT', '"151 WEST ST S NE LOWELL', ' MI 49331"', '0.30', 'ACTIVE', '401 - RESIDENTIAL - IMPROVED', 'True', '"48', '763"', 'True']
