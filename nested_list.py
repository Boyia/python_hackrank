if __name__ == '__main__':
    fulllist = []
    
    def takeSecond(elem):
        return elem[1]

    for _ in range(int(input())):
        name = input()
        score = float(input())
        grade = [name,score]
        fulllist.append(grade)
        fulllist.sort(key=takeSecond)
    
    for i in fulllist:
        if takeSecond(i) == fulllist[1][1]:
            print(takeSecond(i))
            
        
