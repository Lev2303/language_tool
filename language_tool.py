import json
import sys
import random


def keysToValues(dic):
    wrong = 0
    right = 0
    keys = list(dic.keys())
    while True:
        tmpkey = random.choice(keys)
        print("{0}: {1}".format(len(keys), tmpkey))
        # print str(len(keys))+":", tmpkey
        values = dic[tmpkey]
        answ = input("Translation: ")
        if answ in values:
            print("True. {0}\n".format(values))  # fjf
            right += 1
            keys.remove(tmpkey)
        else:
            wrong += 1
            print("Wrong! {0}\n".format(values))
        if len(keys) < 1:
            input("\n\nNothing\nRight - {0}. Wrong - {1}".format(right, wrong))
            sys.exit()


def get_dict():
    result = {}
    with open("lec_1.txt.", encoding="utf-8") as f:
        for line in f:
            words = line.split('\t')
            if len(words) < 2:
                continue
            russian_words = words[1].split(" ")
            all_translates = []
            for russian_word in russian_words:
                clean_word = russian_word.strip().replace(",", "")
                if len(clean_word) > 0:
                    all_translates.append(clean_word)
            if len(all_translates) > 0:
                result[words[0]] = all_translates
    return result


def main():
    # with open("2000_words.json", "r", encoding="utf-8") as f:
    #     wordict = json.load(f)
    wordict = get_dict()
    mode = input("Choose mode:\n\t1:Word To Translation;\n\t2:Translation To Word.\n>> ");
    if mode == "2":
        wordict = {wordict[k]: k for k in wordict.keys()}
    elif mode == "":
        print("Exit")
        sys.exit()

    keysToValues(wordict)


if __name__ == "__main__":
    main()
