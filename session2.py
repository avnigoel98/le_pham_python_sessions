# string functions

#       01234
name = "Aditi"

# print(len(name))



# story = "once upon a time..."
# #        012345
# email = "avni@gmail.com"

#print(email.endswith("com"))

#print(email.count("a"))

# print(story.capitalize())

# print(email.find("hello")) # returns -1 if the string is not prsent
# print(email.find("gmail")) # it returns 5 as g is coming at 5th location or index


# caption  = '''developing writers can often benefit from examining an essay, a paragraph, or even a sentence to determine what makes it effective. On the following pages are several paragraphs for you to evaluate on your own, along with the Writing Center's explanation.

# Note: These passages are excerpted from actual student papers and retain the original wording. Some of the sentences are imperfect, but we have chosen these passages to highlight areas in which the author was successful.

# Thanks to the students who provided their writing for this page of our website. Do you have a discussion post, paper, or other writing assignment that you are particularly proud of? We would love to use it as a sample. Contact us at writingsupport@mail.waldenu.edu if you would like to share.'''



# print(caption.count("the"))

# print(caption.capitalize())

# email = "avni@gmail.com"

# print(email.replace("avni", "harry"))


# \n - escape character for next line
# \t - escape character for tab space

# story= "Once upon a time. \nThe python is a \tprogamming language"

# print(story)



# # Write a program to fill in a letter template given below with name and date

# letter = '''
#             Dear <|NAME|>
#                  You are selected!
#             <|DATE|> 
#         '''


# # Write a program to detect double spaces in a string
# "this is a    string"

# # replace that double space with single space

#        0123456789
# str = "this   is a string"

# ans = str.find("  ")

# print(ans)

# ans1  = str.replace("   " , " ")

# print(ans1)


# # Write a program to format the following letter using escape characters

letter = "Dear Harry, this python course is nice.Thanks"
print(letter)

print("------------------------------------------------------")
letter = "Dear Harry,\n\tthis python course is nice.\nThanks"
print(letter)

# escape characters
# \n - next line
# \t - tab space

