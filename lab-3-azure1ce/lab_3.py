# Lab 3
# Replace "WRITE CODE HERE" with your python code and remove the "pass" statement


# ----------------- Question 1 -----------------
def count_vowels(sentence: str) -> int:
    i = 0
    for words in sentence:
        if words.lower() in ["a","e","i","o","u"]:
            i+=1
    return i

# invoke the function with relevant args of your choice
# WRITE CODE HERE
count_vowels("woshinidie")

# ----------------- Question 2 -----------------
def check_palindrome(word: str) -> bool:
    # prepare a return flag and set a default value as false
    palindrome_flag = False
    #if the string include something strange, replace it with nothing
    trimed_word = word.replace(" ","").replace("'","")
    #trimed_word = ''.join(filter(str.isalpha, word))
    pointer_count = 0
    for alphabet in trimed_word:
        if alphabet == trimed_word[len(trimed_word)-1-pointer_count]:
            pointer_count += 1
        else:
            return palindrome_flag
    palindrome_flag = True
    return palindrome_flag


# invoke the function with relevant args of your choice
# WRITE CODE HERE
check_palindrome("abcd1 32 1dcba")

# ----------------- Question 3 -----------------
def email_id_filter(inbox_email_ids: list) -> (int, int):
    valid_count = 0
    invalid_count = 0
    for email_ids in inbox_email_ids:
        if email_ids.split("@")[1] in ["isi.edu","usc.edu"]:
            valid_count += 1
        else:
            invalid_count += 1
    return valid_count, invalid_count


# invoke the function with relevant args of your choice
# WRITE CODE HERE
email_id_filter(["xyz@usc.edu","qwerty@yahoo.com", "example@isi.edu", "test@gmail.com",
"dsci510@usc.edu"] )
