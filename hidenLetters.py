from tkinter import *
import screenGame



window = screenGame.window


def update_dict(dict_to_update,dic):
    """
    :param dict_to_update: a dict that need to be update and contained the new dict
    :param dic: the new dict that need to add to the other dict
    :return: dict_to_update
    """
    for letter in dic:
        if letter.upper() not in dict_to_update.keys():
            dict_to_update[letter] = dic[letter]
        else:
            for i in dic[letter]:
                dict_to_update[letter].append(i)
    return dict_to_update



def len_secret_letters(word):
    """
    this function checks if there is more than one word and the length of the word,
    for organise the each word in one lines according to the length of the words.
    :return: dic the keys is the letters ,the value is the x&y positions.
    """
    y = 100
    x = 160
    counter = 200
    dic = {}
    print(len(word))
    if len(word) > 9:
        if " " in word: #check if there is more than 1 words
            list_word = word.split(" ")
            for i in range(len(list_word)):
                if i != len(list_word)-1:
                    if len(list_word[i]+list_word[i+1]) >= 9:
                        number_line = (secret_letters(list_word[i], x, y, counter))
                        new_dic = update_dict(dic,number_line)
                        dic = new_dic
                        y += 100
                        counter += 360
                else:

                    number_line = secret_letters(list_word[i], x, y, counter)
                    new_dic = update_dict(dic,number_line)
    elif len(word) < 7:
        new_dic = secret_letters(word, 200, y, counter)
    else:
        new_dic = secret_letters(word, x, y, counter)


    return new_dic



def secret_letters(word,x,y,counter):

    letter_in_secret_word = {}
    for i in range(len(word)):
        if counter < 550:
            x += 40
            # p = i

            if word[i] != " ":
                p = Label(window, text="_", bg="white", font=("ariel"))
                p.place(x=x, y=y)

                if word[i].upper() not in letter_in_secret_word.keys():
                    letter_in_secret_word[word[i].upper()] = [(x, y)]
                else:
                    letter_in_secret_word[word[i].upper()].append((x,y))
            else:
                p = Label(window, text=" ")
                p.place(x=x, y=y)

        elif counter > 550 and counter < 910:
            x += 40
            if word[i] != " ":
                p = Label(window, text="_", bg="white", font=("ariel"))
                p.place(x=x, y=y)
                if word[i].upper() not in letter_in_secret_word.keys():
                    letter_in_secret_word[word[i].upper()] = [(x, y)]
                else:
                    letter_in_secret_word[word[i].upper()].append((x, y))
            else:
                p = Label(window, text=" ")
                p.place(x=x, y=y)
        else:
            x+=40
            if word[i] != " ":
                p = Label(window, text="_", bg="white", font=("ariel"))
                p.place(x=x, y=y)
                if word[i].upper() not in letter_in_secret_word.keys():
                    letter_in_secret_word[word[i].upper()] = [(x,y)]
                else:
                    letter_in_secret_word[word[i].upper()].append((x, y))
            else:
                p = Label(window, text=" ")
                p.place(x=x, y=y)

    return letter_in_secret_word

#
# def secret_letters():
#
#     first_line = 200
#     second_line = 200
#     third_line = 200
#
#     letter_in_secret_word = {}
#     for i in range(len(word)):
#         if first_line < 550:
#             first_line += 40
#             p = i
#
#             if word[i] != " ":
#                 p = Label(window,text="_",bg="white",font=("ariel"))
#                 p.place(x=first_line, y=100)
#
#                 if word[i].upper() not in letter_in_secret_word.keys():
#                     letter_in_secret_word[word[i].upper()]=[(first_line,100)]
#                 else:
#                     letter_in_secret_word[word[i].upper()].append((first_line, 100))
#             else:
#                 p = Label(window, text=" ")
#                 p.place(x=first_line, y=100)
#
#         elif first_line>550 and first_line<910:
#             first_line += 40
#             second_line += 40
#             if word[i] != " ":
#                 p = Label(window, text="_", bg="white", font=("ariel"))
#                 p.place(x=second_line, y=200)
#                 # exec('d{}=Label(window,text="_",bg="white",font=("arial",20))'.format(i))
#                 # exec('d{}.place(x={},y={})'.format(i, z, 200))
#                 if word[i].upper() not in letter_in_secret_word.keys():
#                     letter_in_secret_word[word[i].upper()] = [(second_line,200)]
#                 else:
#                     letter_in_secret_word[word[i].upper()].append((second_line, 200))
#             else:
#                 p = Label(window, text=" ")
#                 p.place(x=second_line, y=200)
#         else:
#             third_line += 40
#             if word[i] != " ":
#                 p = Label(window, text="_", bg="white", font=("ariel"))
#                 p.place(x=third_line, y=300)
#                 # exec('d{}=Label(window,text="_",bg="white",font=("arial",20))'.format(i))
#                 # exec('d{}.place(x={},y={})'.format(i, z, 200))
#                 if word[i].upper() not in letter_in_secret_word.keys():
#                     letter_in_secret_word[word[i].upper()] = [(third_line,300)]
#                 else:
#                     letter_in_secret_word[word[i].upper()].append((third_line, 300))
#             else:
#                 p = Label(window, text=" ")
#                 p.place(x=third_line, y=300)
#
#     return letter_in_secret_word


