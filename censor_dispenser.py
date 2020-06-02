# These are the emails you will be censoring. The open() function is opening the text file that the emails are contained in and the .read() method is allowing us to save their contexts to the following variables:
email_one = open("email_one.txt", "r").read()
email_two = open("email_two.txt", "r").read()
email_three = open("email_three.txt", "r").read()
email_four = open("email_four.txt", "r").read()


# Write a function
# that can censor a specific word or phrase from a body of text,
# and then return the text.
def censor_one(input_text, phrase):
    censor = ""

    for i in range(0, len(phrase)):
        if phrase[i] == " ":
            censor += " "
        else:
            censor += "*"

    return input_text.replace(phrase, censor)


# print(censor_one(email_one, "learning algorithms"))

# Write a function
# that can censor not just a specific word or phrase
# from a body of text, but a whole list of words and phrases,
# and then return the text.
proprietary_terms = ["she", "personality matrix", "sense of self",
                     "self-preservation", "learning algorithm", "her", "herself"]


def censor_two(input_text, phrase_list):
    for phrase in phrase_list:
        censor = ""
        for i in range(0, len(phrase)):
            if phrase[i] == " ":
                censor += " "
            else:
                censor += "*"

        input_text = input_text.replace(phrase, censor)

    return input_text


# print(censor_two(email_two, proprietary_terms))

# Write a function
# that can censor any occurrence of a word from the “negative words” list after any “negative” word has occurred twice,
# as well as censoring everything from the list from the previous step as well and use it to censor email_three.
negative_words = ["concerned", "behind", "danger", "dangerous", "alarming",
                  "alarmed", "out of control", "help", "unhappy", "bad", "upset",
                  "awful", "broken", "damage", "damaging", "dismal", "distressed",
                  "distressed", "concerning", "horrible", "horribly", "questionable"]


def censor_three(input_text, phrase_list, negative_words):
    for word in negative_words:
        if input_text.count(word) >= 2:
            phrase_list.append(word)
    for phrase in phrase_list:
        censor = ""
        for i in range(0, len(phrase)):
            if phrase[i] == " ":
                censor += " "
            else:
                censor += "*"

        input_text = input_text.replace(phrase, censor)

    return input_text


# print(censor_three(email_three, proprietary_terms, negative_words))

# Write a function 
# that censors not only all of the words from the negative_words and proprietary_terms lists, 
# but also censor any words in email_four that come before AND after a term from those two lists.
punct_mark = [",", "!", "?", ".", "%", "/", "(", ")"]


def censor_four(input_text, censored_list):
    input_text_words = []

    for x in input_text.split(" "):
        x1 = x.split("\n")
        for word in x1:
            input_text_words.append(word)
    # print(input_text_words)

    for i in range(0, len(input_text_words)):
        checked_word = input_text_words[i].lower()
        for x in punct_mark:
            checked_word = checked_word.strip(x)

        if checked_word in censored_list:

            # Censoring the targeted word
            word_target = input_text_words[i]
            censor = ""

            for x in punct_mark:
                word_target = word_target.strip(x)
            for x in range(0, len(word_target)):
                censor = censor + "*"
            input_text_words[i] = input_text_words[i].replace(word_target, censor)

            # Censoring the word before the targeted word
            word_before = input_text_words[i - 1]
            censor_before = ""

            for x in punct_mark:
                word_before = word_before.strip(x)
            for x in range(0, len(word_before)):
                censor_before = censor_before + "*"
            input_text_words[i - 1] = input_text_words[i - 1].replace(word_before, censor_before)

            # Censoring the word after the targeted word
            word_after = input_text_words[i + 1]
            censor_after = ""

            for x in punct_mark:
                word_after = word_after.strip(x)
            for x in range(0, len(word_after)):
                censor_after = censor_after + "*"
            input_text_words[i + 1] = input_text_words[i + 1].replace(word_after, censor_after)

    return " ".join(input_text_words)


censored_list = proprietary_terms + negative_words

# print(censor_four(email_four, censored_list))
