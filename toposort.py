import roman

text = []
result = []

def start():
    ascii = """
░█████╗░████████╗░██╗░░░░░░░██╗  ██╗░░░░░██╗░░░██╗██╗░░░░░██╗░░░██╗░██████╗██╗
██╔══██╗╚══██╔══╝░██║░░██╗░░██║  ██║░░░░░██║░░░██║██║░░░░░██║░░░██║██╔════╝██║
██║░░██║░░░██║░░░░╚██╗████╗██╔╝  ██║░░░░░██║░░░██║██║░░░░░██║░░░██║╚█████╗░██║
██║░░██║░░░██║░░░░░████╔═████║░  ██║░░░░░██║░░░██║██║░░░░░██║░░░██║░╚═══██╗╚═╝
╚█████╔╝░░░██║░░░░░╚██╔╝░╚██╔╝░  ███████╗╚██████╔╝███████╗╚██████╔╝██████╔╝██╗
░╚════╝░░░░╚═╝░░░░░░╚═╝░░░╚═╝░░  ╚══════╝░╚═════╝░╚══════╝░╚═════╝░╚═════╝░╚═╝"""
    print(ascii)
    print("SOLUSI 144 SKS ANDA")



def add(file):
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
    for i in range(len(text)):
        for j in range(len(text[i])):
            if(text[i][j] == deleted):
                text[i].pop(j)
                break


def main():
    start()
    filename = input("Masukkan file kuliah :")
    try:
        file = open(f"{filename}", "r")
        add(file)   
        while(len(text) != 0):
            temp = []
            idx = []
            for i in range(len(text)):
                if(len(text[i]) == 1):
                    temp.append(text[i][0])
                    idx.append(i)

            for i in range(len(idx)-1, -1, -1):
                text.pop(idx[i])

            for i in range(len(temp)):
                deleteClass(temp[i])
            result.append(temp)
        output()
    except:
        print("No File Found")
    print("Semoga cepat lulus~")
    print("Enter to close..")
    input()


def output():
    count = 1
    for semester in result:
        print("Semester", roman.toRoman(count), ":")
        for i in range(len(semester)):
            print("-", semester[i])
        count += 1

if __name__ == "__main__":
    main()