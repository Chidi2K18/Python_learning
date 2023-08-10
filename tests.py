import copy


# show in a list the idexes of capital letters in a string
def captialCheck(string):
    counter = 0
    indexes = []
    for i in string:
        counter += 1
        if i.isupper():
            indexes.append(counter)
    print(indexes)


# print(captialCheck("BoB"))
# print the middle letter in a string
def mid(string):
    mid_letter = len(string) / 2
    return string[int(mid_letter)]


# print(mid("bob"))

# count the number of ppl that are online in a dictionary
statuses = {
    "Alice": "online",
    "Bob": "offline",
    "Eve": "online",
}


def online_count(dict):
    counter = 0
    for x in dict.values():
        if x == "online":
            counter += 1
    return counter


# print(online_count(statuses))
# check if both parameters are numbers


# print(only_ints(-1, 999))
# calculate difference between largest and smallest in group

def largest_difference(list):
    largest = 0
    smallest = 100
    for i in list:
        if i > largest:
            largest = i
        if i < smallest:
            smallest = i
    return largest - smallest


test = [1, 2, 4]


def convert(num):
    converted = num
    return str(converted)


# print(convert(test))

# return the number you put in with commas to denote thousnads
def fromat_num(num):
    return ("{:,}".format(num))


# print(fromat_num(2000000))

# count the number of arguments used
def param_count(*args):
    counter = 0
    for i in args:
        counter += 1
    return counter


def convert(hours, minutes):
    return ((hours + minutes) * 60) * 60


# print(convert(1,10))

def numlength(num):
    convert = str(num)
    counter = 0
    for i in convert:
        counter += 1
    return counter


# print(numlength(2000))

# this is to test the enumerate methon
test = [["eat", "Drink"], ["Sleep", "Repeat"]]

new_test = copy.deepcopy(test)

new_test[0][1] = "Tea"


# print(test)
# print(new_test)


# for i in enumerate(test):
# print(i)

def countPairs(projectCosts, target):
    result_pairs = set()  # Use a set to store distinct pairs

    # Loop through each element in projectCosts. 'i' is the index of the current element.
    for i in range(len(projectCosts)):
        # For each index, loop through the elements in projectCosts. 'j' is the index of the subsequent element.
        for j in range(i + 1, len(projectCosts)):
            # Create a pair of the two costs, with the smaller one first and the larger one second.
            pair = (min(projectCosts[i], projectCosts[j]), max(projectCosts[i], projectCosts[j]))
            # If the absolute difference between the two project costs is equal to the target value,
            if abs(projectCosts[i] - projectCosts[j]) == target:
                # Add the pair to the set of result_pairs.
                # (sets dont allow dupes)
                result_pairs.add(pair)
    # print(result_pairs)
    return len(result_pairs)


projectCosts = [1, 5, 3, 4, 2]
target = 2
# print(countPairs(projectCosts, target))
# the goal here is to take the string and return the number of times any character in the string occurs
s = "aabbbccdde"
list(s)  # convert to list
testSet = set()  # create a set to hold the tuples
for i in s:  # index through the list
    pair = (i, s.count(i))  # create a tuple using the current index value as an element pair[0]
    # and the number of times it occurs in the string as the second element pair[1]
    testSet.add(pair)

answer_set = sorted(testSet, key=lambda x: x[1], reverse=True)
# key=lambda x: x[1]: this targets the second element of the tuple(the count of occurences)
# for c in answer_set[:3]:  # get the 3 most common occurences
# print the first and second element of each tuple in the format 'a 1'
# print(f'{c[0]} {c[1]}')

# the idea here is that you take a number, list all the numbers that came before it,
# square those numbers and print the results vertically(why vertically? IDK)
n = 10

all_Smaller_Numbers = list(range(n))  # create a list of all the numbers smaller than the input
# in this case 1,2,3,4,5,6,7,8,9
squared_Numbers = []
for i in all_Smaller_Numbers:  # index through the list
    squared_Numbers.append(pow(i, 2))  # append into the array the squared value of the current increment


# print(squared_Numbers)

# for c in squared_Numbers:
# print(f'{c}') #format the output vertically

# this is correct and hackerrank is wrong
# the idea here is to determine if a given year is a leap year
def is_leap(year):
    leap = False
    # Write your logic here
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                leap = True
            else:
                leap = True
    return leap


# print(is_leap(2100))
# the idea here is that you have to find the first number in the array(arr) that is less than the input(n)
# the hard part was that say you sort it and its [6,6,5] the answer you would have to give is 5
# so you then have to convert the array to a set to remove duplicates
# then sort it so that it is in decending order and get the first second element
# n = int(input())
# arr = map(int, input().split())
# no_dupes = list(set(arr))
# sorted_Array = sorted(no_dupes, reverse=True)
# print(sorted_Array[1])

students = [['Harry', 20], ['Berry', 20], ['Tina', 19], ['Akriti', 19], ['bob', 21]]
newList = list(students)
# print(students)
test_list = set()
for i in newList:
    name = i[0]
    # print(name)
    score = i[1]
    # print(score)
    pair = (name, score)
    test_list.add(pair)
# print(test_list)
sortedtest_list = sorted(test_list, key=lambda x: x[0])
# print(sortedtest_list)
sorted_sorted = sorted(sortedtest_list, key=lambda x: x[1])
# print(sorted_sorted)
answer_list = []
for i, j in sorted_sorted:
    answer_list.append(j)
    # print(answer_list)
sorted(answer_list, reverse=True)
# print(answer_list)
lowest_score = float((answer_list[1]))


# for i,j in sorted_sorted:
# if j == lowest_score:
# print(i)
# print(sortedtest_list[1][0])

def maskify(cc):
    tomask = list(cc)
    tomask[:-4] = ['#'] * len(tomask[:-4])  # make it so that all but the last 4 elements in the list
    # are hashes
    if len(cc) < 1:
        return ''
    if all(str(item).isdigit() for item in cc):
        # step 1: convert the list to a string, why because 'isdigit()' only works with strings
        # step 2: 'all' looks at the whole list using the loop
        # step 3: isdigit returns true or false based on if *all* the elements(item) in the list are digits
        result = ''.join(cc)  # concatenates all elements in the list into a string
        return result
    return ''.join(tomask)


# for reference below is a condensed version of what you did
# def maskify(cc):
# return "#"*(len(cc)-4) + cc[-4:]
# "#"* - this will make it so that the hash string is repeated as many times as needed
# so what happens next is that hash is repeated by the length of the list - 4
# then the hashes are concatenated to the remaining 4 elements in the list
# note the first set of digits are not being changed but replaced altogether
# print(str(maskify('SF$SDfgsd2eA')))


# the goal here was to take a number and if the number was more than 2 digits long return the sum of the
# numbers that comprised the sum e.g. input = 11 the output should be 2 because 1 + 1
# the real challenge here is what happens when your input number has lots of digits e.g. 233784
# you must return the smallest possible sum
# so 2 + 3 + 3 + 7 + 8 + 4 = 27
# next you would do 2 + 7 = 9 and this would be your smallest sum

def digital_root(n):
    total = sum(int(digit) for digit in str(n))
    index = []
    if len(str(total > 1)):
        for i in str(total):
            index.append(int(i))
        return sum(index)
    return total


# the idea above works to the extent of not having more than 2 digits to sum

# the solution below uses a while loop instead of a for loop to get down to the smallest possible value
def digital_root(n):
    total = sum(int(digit) for digit in str(n))
    while len(str(total)) > 1:
        total = sum(int(i) for i in str(total))
    return total


# print(digital_root(11))

def solution(s):
    yes = list(s)
    counter = 0
    output = []
    b = 0  # remember this is the current index in the loop
    while b < len(yes):
        j = yes[b]
        if b + 1 < len(yes):
            k = yes[b + 1]
        else:
            k = '_'
        print(k)
        output.append(j + k)
        b += 2
    return output


# print(solution("asdfads"))

def duplicate_count(text):
    # Your code goes here
    counter = 0
    for i in text:
        print((i, text.count(i)))
        if text.count(i) > 1:
            counter += 1
    return counter


print(duplicate_count("abcdeaa"))
