import random
import time

def sortTab(toSort):
    tab = toSort
    changed = True

    while changed :
        changed = False
        for i in range(0,len(tab)-1):
            if tab[i]>tab[i+1] :
                tab[i],tab[i+1] = tab[i+1],tab[i]
                if not changed :
                    changed = True

    return tab

def randomTab(size):
    tab = []
    for i in range(0,size):
        tab.append(random.randint(1,99))
    return tab

def main():
    while(True):
        file = open('sortedLists.txt', 'a+')
        file.write('[')
        tabToSort = randomTab(10)
        str1 = ','.join(str(e) for e in tabToSort)
        file.write(str1)

        file.write('] -> [')
        
        sortedTab = sortTab(tabToSort)
        str2 = ','.join(str(e) for e in sortedTab)
        file.write(str2)

        file.write('] \n')
        file.close()
        time.sleep(30)

if __name__ == '__main__':
    main()
    


