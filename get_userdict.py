import pandas as pd

if __name__ == '__main__':
    # 南开相关名词 nk
    nk = pd.read_csv("data/csv/NK.csv")
    # 教师 pp
    person = pd.read_csv("data/csv/person_all.csv")

    nk = nk['name']
    nk = [n.strip() + " 15 nk\n" for n in nk]

    pp = person['name']
    pp = [p.strip() + " 15 pp\n" for p in pp]

    with open("data/userdict.txt", "w", encoding="utf-8") as fw:
        fw.writelines(nk)
        fw.writelines(pp)
