# Assignment 0 - Python Programming

* Full Mark: **100** (**5%** of the course assessment scheme)
* Deadline: 20th January, 2018
* Submission: Put all the functions in one singel Python script file with the name `asgn0_<student_id>.py` (e.g. `asgn0_12345678.py`). Submit the file to eLearn.

### Problem 1 (10 Marks)

Write a function `problem_1` that returns the number of integers that are divisble by 7 but not a multiple of 3 between two given non-zero integers `a` and `b` (including `a` and `b`). For example, if `a = 10` and `b = 30`, it should return `2` as there are two integers (14 and 28) that satisfy the above condition.

    :::python
    def problem_1(a, b):
        num = 0
        ...
        return num


### Probelm 2 (10 Marks)

Write a function `problem_2` that returns the sum of `n + nnn + nnnnn` given that `n` is a positive single-digit number (i.e. n can be `0` to `9`). For example, if `n = 8`, then the function should return `8 + 888 + 88888 = 89784`. You should also check that `n` is a single digit, if not you should simply return `0`.

    :::python
    def problem_2(n):
        result = 0
        ...
        return result


### Problem 3 (20 Marks)

Write a function `problem_3` that, given a list `nums` of integers, returns the largest of the sums of all three consecutive numbers in the list. For example, if `nums = [1, 3, -2, 4, 8, -9, 0, 5]`, the sums of all three consecutive numbers are `2, 5, 10, 3, -1, -4`. Therefore the function should return `10`.

    :::python
    def problem_3(nums):
        max_sum = 0
        ...
        return max_sum


### Problem 4 (20 Marks)

Write a function `problem_4` that sorts the words in a sentence. For example, if the input to the function is `"the chinese university of hong hong"`, the output of the function should be the string `"chinese hong kong of the university"`. The words should be sorted in ascending order of their ASCII values. You can assume that only alphabets and space will be present in the input string.

    :::python
    def problem_4(sentence):
        ouput = ""
        ...
        return output


### Problem 5 (20 Marks)

Write a function `problem_5` that counts the number of occurrence of each word in a given string, and then return a list of the the **5** most frequent words along with their counts. Please note that you should convert all alphabets into lowercases first. You can assume that words are separated by **spaces**, and you do not have to remove any other symbols from the words. For example, if the input is the following paragraph:

    :::python
    paragraph = """
        The Transmission Control Protocol (TCP) is one of the main protocols of the Internet protocol suite. It originated in the initial network implementation in which it complemented the Internet Protocol (IP). Therefore, the entire suite is commonly referred to as TCP/IP. TCP provides reliable, ordered, and error-checked delivery of a stream of octets between applications running on hosts communicating by an IP network. Major Internet applications such as the World Wide Web, email, remote administration, and file transfer rely on TCP. Applications that do not require reliable data stream service may use the User Datagram Protocol (UDP), which provides a connectionless datagram service that emphasizes reduced latency over reliability.
    """

The output of the function should be the following:

    :::python
    [(8, 'the'), (4, 'protocol'), (4, 'of'), (3, 'internet'), (3, 'applications')]

The function should be named `problem_05` as follows:

    :::python
    def problem_5(sentence):
        ouput = []
        ...
        return output


### Problem 6 (20 Marks)

Write a function `problem_6` that reads a CSV file and convert the data into a Python dictionary. The input to the function is the **absolute path to the CSV file**, and the output should be **a list of dictionary objects**. For example, if the content of the CSV file is as follows:

    hkid,sex,dob,location
    A123456(1),M,1985-10-20,Mongkok
    B234567(2),F,1990-02-12,Shatin

The output of the function should be the following:

    :::python
    [
        {"hkid": "A123456(1)", "sex": "M", "dob": "1985-10-20", "location": "Mongkok"},
        {"hkid": "B234567(2)", "sex": "F", "dob": "1990-02-12", "location": "Shatin"}
    ]

That is, the keys of the dictionaries are the column names in the CSV file; and the values are the values found in each record. Note that the first line of the CSV file contains the column names.

You can assume that fields are separated by commas, and no comma will appear in the content of a cell.

    :::python
    def problem_6(path_to_file):
        ouput = []
        ...
        return output
