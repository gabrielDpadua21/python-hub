PATH_LETTERS = "./letters/"
FILE_NAMES = "names.txt"
FILE_LETTERS = "letter.txt"


def get_names():
    names = []
    try:
        with open(FILE_NAMES, "r") as file:
            names = file.readlines()
    except FileNotFoundError:
        print("File not found")
    return names


def get_letter():
    letter = []
    try:
        with open(FILE_LETTERS, "r") as file:
            letter = file.readlines()
    except FileNotFoundError:
        print("File not found")
    return letter


def create_letters(names, letter):
    for name in names:
        with open(PATH_LETTERS + name.strip() + ".txt", "a") as file:
            for line in letter :
                if "[cat]" in line:
                    line = line.replace("[cat]", name)
                file.write(line)


if __name__ == '__main__':
    print("Mail Merger")
    names = get_names()
    letter = get_letter()
    create_letters(names, letter)
    