def profile(name, age, lang1, lage2, lang3, lang4, lang5):
    print("이름 : {}\t나이 : {}\t".format(name, age), end = " ")
    # end = " "가 있다면 두 문장이 한 줄로
    print(lang1, lage2, lang3, lang4, lang5)

profile("유재석", 20, "Python", "Java", "C", "C++", "C#")

def profileVariable(name, age, *language):
    print("이름 : {}\t나이 : {}\t".format(name, age), end = " ")
    for lang in language:
        print(lang, end = " ")
    print()

profileVariable("김태호", 25, "C", "C++", "C#")
profileVariable("유재석", 20, "Python", "Java", "C", "C++", "C#")