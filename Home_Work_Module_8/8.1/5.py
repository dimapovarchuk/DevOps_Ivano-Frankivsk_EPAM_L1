import emojis
def main():
    sentence = input("Input a Sentence: ")
    print(sentence)
    sentence = convert(sentence)
    print(sentence)


def convert(sentence):
    smile = emojis.encode(':smile:')
    pensive = emojis.encode(':pensive:')
    sentence = sentence.replace(":)", smile)
    sentence = sentence.replace(":(", pensive)
    return sentence


main()
