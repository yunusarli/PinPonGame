class FileRead(object):
    def __init__(self,file):
        self.file = file
        self.liste = list()
    def read(self):
        with open(self.file,"r") as file:
            gecici = file.readlines()
        for i in gecici:
            i = i.strip("\n")
            self.liste.append(i)
        return self.liste
    def add(self,item):
        kume = set()
        kume.add(item)
        with open(self.file,"a+") as file:
            for i in kume:
                file.write(str(i)+"\n")
    def clear(self):
        f = open(self.file, 'r+')
        f.truncate(0)
        self.liste.clear()
    def highest(self):

        highest_table = set()
        file = self.read()
        for i in file:
            highest_table.add(int(i))
        return max(highest_table)


if __name__=="__main__":
    myFile = FileRead("scores.txt")

    print(myFile.highest())
