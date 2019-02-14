import argparse


def NumbersInText(number_file, text_file, output_name):
    number_f = open("Numbers/{}".format(number_file), "r")
    number = number_f.read()
    number = number.replace('.', '')

    text_f = open("Text/{}".format(text_file), "r", encoding="utf8")
    text = text_f.read()
    text_words = text.split()

    output_f = open('Output/{}'.format(output_name), 'w')

    text_len = len(text_words)
    count = 0
    digit_counter = 0

    while count < text_len - 10:
        digit = int(number[digit_counter])
        count += digit
        output_f.write(str(text_words[count + 1]) + ' ')
        digit_counter += 1

    number_f.close()
    text_f.close()
    output_f.close()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-n", "--number",
                        help="Path to the file containing the number")
    parser.add_argument("-t", "--text",
                        help="Path to the text file ")
    parser.add_argument("-o", "--output",
                        help="Path and name for the output file")
    args = parser.parse_args()
    NumbersInText(args.number, args.text, args.output)


main()
