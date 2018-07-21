from summarizer.src.summarizer.algo.summ import Summ
from summarizer.src.summarizer.summarizer import summarizer


def main():
    with open("../../texts/DonQuixote.txt") as f:
        inputText = f.readlines()[0]

    summarizer.text = inputText
    summarizer.algo = Summ.TEXT_RANK
    summarizer.percentage = 0.5

    print(summarizer.summarize())
    print(summarizer.schematize())


if __name__ == "__main__":
    main()
