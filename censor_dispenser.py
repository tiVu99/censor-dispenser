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

