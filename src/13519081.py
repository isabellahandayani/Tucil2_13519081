import roman

text = []
result = []

def start():
    # Mencetak Logo Program
    # KAMUS LOKAL
    # ascii = string

    # ALGORITMA

    ascii = """
 █████╗ ████████╗ ██╗       ██╗  ██╗     ██╗   ██╗██╗     ██╗   ██╗ ██████╗██╗
██╔══██╗╚══██╔══╝ ██║  ██╗  ██║  ██║     ██║   ██║██║     ██║   ██║██╔════╝██║
██║  ██║   ██║    ╚██╗████╗██╔╝  ██║     ██║   ██║██║     ██║   ██║╚█████╗ ██║
██║  ██║   ██║     ████╔═████║   ██║     ██║   ██║██║     ██║   ██║ ╚═══██╗╚═╝
╚█████╔╝   ██║     ╚██╔╝ ╚██╔╝   ███████╗╚██████╔╝███████╗╚██████╔╝██████╔╝██╗
 ╚════╝    ╚═╝      ╚═╝   ╚═╝    ╚══════╝ ╚═════╝ ╚══════╝ ╚═════╝ ╚═════╝╚═╝"""
    print(ascii)
    print("SOLUSI 144 SKS ANDA")



def add(file):
    # Menyimpan masukan dari file ke dalam list text
    # Implementasi DAG dalam struktur data list of list

    # KAMUS LOKAL
    # string : string
    # row : array of string

    # ALGORITMA
    for kelas in (file):
        string = ""
        row = []
        for i in range(len(kelas)):
            if(kelas[i] == "," or kelas[i] == "."):
                row.append(string)
                string = ""
            elif(kelas[i] != "," and kelas[i] != "." and kelas[i] != " " and kelas[i] != "\n"):
                string = string + kelas[i]
        text.append(row)

def deleteClass(deleted):
    # Menghapus mata kuliah yang tidak memiliki prerequisite
    # (busur menuju mata kuliah deleted = 0)
    # dari busur mata kuliah lain

    # ALGORITMA
    for i in range(len(text)):
        for j in range(len(text[i])):
            if(text[i][j] == deleted):
                text[i].pop(j)
                break


def main():
    # Program utama

    # KAMUS
    # filename : string
    
    #ALGORITMA
    start()
    filename = input("Masukkan file kuliah :")
    try:
        file = open(f"../test/{filename}", "r")
        add(file)
        if isCyclic():
            toposort()
            output()
        else:
            print("Format masukan salah, graf siklik!")
    except:
        print("No File Found")
    print("Semoga cepat lulus~~")
    print("Enter to close..")
    input()


def isCyclic():
    found = False
    for i in range(len(text)):
        if len(text[i]) == 1 :
            found = True
    return found

def output():
    # Mencetak hasil topological sort ke layar

    # KAMUS LOKAL
    # count : int

    # ALGORITMA
    count = 1
    for semester in result:
        print("Semester", roman.toRoman(count), ":", end="")
        print(semester[0], end="")
        for i in range(1, len(semester)):
            print(",", semester[i], end="")
        print("\n")
        count += 1

def toposort():
    # Melakukan topological sorting secara rekursif
    
    # KAMUS LOKAL
    # temp : array of string
    # idx : array of int

    # ALGORITMA
    if(len(text) == 0): # Basis
        pass
    else: # Rekursi
        temp = []
        idx = []
        for i in range(len(text)):
            if(len(text[i]) == 1): # Derajat masuk = 0
                temp.append(text[i][0])
                idx.append(i)

        # Menghapus semua mata kuliah dengan derajat masuk = 0
        for i in range(len(idx)-1, -1, -1): 
            text.pop(idx[i])

        # Menghapus mata kuliah derajat 0 dari prerequisite
        for i in range(len(temp)): 
            deleteClass(temp[i])
        result.append(temp)
        toposort()



if __name__ == "__main__":
    main()