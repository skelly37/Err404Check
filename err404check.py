import sys, os, urllib.request

'''Error404 Check, as the name says, checks whether the website exists or displays Err404: Not Found

    Usage: create a txt file with one link per line, launch the script. File will be overwritten without invalid links'''

def main():
    #getting location of this script
    path = str(sys.argv[0])
    path = path.replace('err404check.py', '')

    input('''    temp.txt file will be overwritten without invalid links

            Press Enter to continue''')

    #variables needed to iterate over the links
    filer = open(path + 'temp.txt', 'r')
    line = filer.readline()
    count = 0
    existing_links = []

    #getting number of records to display the progress
    records = 0
    while line != '':
        records += 1
        line = filer.readline()
    filer.close()

    #starting the testing
    filer = open(path + 'temp.txt', 'r')
    line = filer.readline().strip()

    while line != '':
        #trying to open the website
        try:
            request = urllib.request.Request(line, headers={'User-Agent':'Mozilla/5.0'})
            site = urllib.request.urlopen(request)
            existing_links.append(line)
        except urllib.error.HTTPError:
            pass

        #displaying script's progress
        os.system('clear')
        count += 1
        print('Progress: ', count, '/', records, '  (', format((count/records)*100, '5.2f'), '%)', sep='' )
        print(bad_links)
        line = filer.readline().strip()

    filer.close()

    #overwrite the old file to remove links with Error404
    filew = open(path + 'temp.txt', 'w')
    for count in range (len(existing_links)):
        filew.write(existing_links[count] + '\n')

    filew.close()

main()
