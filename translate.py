import sys
import translator

def Main():

    if len(sys.argv) != 4:
        if sys.argv[1] == '-hc':
            print("\nhelp: \n \nThese are Translator commands: \n\n Translating FILE_1 with output in FILE_2: ")
            print("\n      ./trans [INPUT_FILE_NAME] [OUTPUT_FILE_NAME] [command]")
            print("\n Commands: \n")
            print("     [-lc] to translate from Latin to Cirilic\n\n")
            sys.exit(0)
        elif sys.argv[1] == '-v':
            print("translator version: 1.0.0")
            sys.exit(0)

    if sys.argv[3] == '-lc':
            trans= translator.Translate(sys.argv[1], sys.argv[2], "Serbian")
            trans.translate('Latin-to-Cirilic')
            print("\n\n ~ ~ ~ Succsesful translation ~ ~ ~ \n\n   Output file: " + sys.argv[2] +"\n\n")
            sys.exit(0)

    if sys.argv[3] == '-tr' and len(sys.argv) == 5:
        if sys.argv[4] == 'english' or sys.argv[4] == 'English':
            trans= translator.Translate(sys.argv[1],sys.argv[2], "English")
            trans.translate("Translate-to-English")
            print("\n\n Translated to english \n\n")
            sys.exit(0)


    print("\ntranslator: \n\n " + sys.argv[1] + " is not translator command. See help menu by using commands: \n\n"
                                                "  [-hc] for running with ./ "
                                                "\n  [-hp] for runnig with python\n\n")
    sys.exit(1)


if __name__ == '__main__':
    Main()