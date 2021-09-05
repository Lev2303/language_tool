import json


result = {}
with open("D:\git\English\new_words01092021", encoding="utf-8") as f:
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



with open("2000_words.json", "w", encoding="utf-8") as f:
    json.dump(result, f)