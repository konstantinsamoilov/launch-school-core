import random

TOPICS = [
    "Naming conventions: legal vs. idiomatic, illegal vs. non-idiomatic",
    "Type coercions: explicit (e.g., using int(), str()) and implicit",
    "Numbers",
    "Strings",
    "f-strings",
    "String methods: capitalize, swapcase, upper, lower",
    "String methods: isalpha, isdigit, isalnum, islower, isupper, isspace",
    "String methods: strip, rstrip, lstrip, replace",
    "String methods: split, find, rfind",
    "Boolean vs. truthiness",
    "None",
    "Ranges",
    "List and dictionary syntax",
    "List methods: list.append(), list.pop(), list.reverse()",
    "Dictionary methods: dict.keys(), dict.values(), dict.items(), dict.get()",
    "Slicing (strings, lists, tuples)",
    "Arithmetic operators: +, -, *, /, //, %, **",
    "List and string operators: +",
    "Comparison operators: ==, !=, <, >, <=, >=",
    "Logical operators: and, or, not",
    "Identity operators: is, is not",
    "Operator precedence",
    "Mutability and immutability",
    "Pass by object reference",
    "Variables: naming conventions",
    "Variables: initialization, assignment, and reassignment",
    "Variables: scope",
    "Variables: global keyword",
    "Variables: variables as pointers",
    "Variables: variable shadowing",
    "Conditionals",
    "Loops: for",
    "Loops: while",
    "The len() function",
    "print() and input()",
    "Exceptions (when they will occur and how to handle them)",
    "Functions: definitions and calls",
    "Functions: return values",
    "Functions: parameters vs. arguments",
    "Functions: nested functions",
    "Functions: output vs. return values, side effects",
    "Expressions and statements",
]

NUM_TOPICS = len(TOPICS)

MAX_PAIRS = (NUM_TOPICS * (NUM_TOPICS - 1)) // 2
# Topics, multiplied by all the other topics,
# divided by 2 because we don't need the reverse order of pairs
# (only need A & B, not B & A).

topic_scores = {}
for topic in TOPICS:
    topic_scores[topic] = 0

more_difficult = {}
for topic in TOPICS:
    more_difficult[topic] = 0

less_difficult = {}
for topic in TOPICS:
    less_difficult[topic] = 0
# (These could be dict comprehensions, but that's more a 110 thing.)

uncompared_pairs = []

for i in range(len(TOPICS)):
    for j in range(i + 1, len(TOPICS)):
        topic1 = TOPICS[i]
        topic2 = TOPICS[j]
        uncompared_pairs.append((topic1, topic2))
# Creating every possible pairing.

random.shuffle(uncompared_pairs)

topics_so_far = []

compared_pairs = set()

def get_score_and_comparisons(compared_topic):
    score_of_topic = topic_scores[compared_topic]
    comparisons_of_topic = more_difficult[compared_topic] + less_difficult[compared_topic]
    return (score_of_topic, comparisons_of_topic)
    # Compare topics first by score, and if tied,
    # by the number of times the user has compared them.

def prompt(message):
    print(f"~~> {message}")

print("")
prompt("I'll give you two randomized topics from the PY109 study guide,")
prompt("and you pick the one that's more difficult.")
print("")
prompt("After comparing a few, you'll see 6-8 of your most difficult topics,")
prompt("always including the two you've just compared with an asterisk '*', ")
prompt("and a '(0/0)' counter, for how often a topic was more/less difficult.")
print("")
prompt("Every comparison pair is unique.")
prompt("There are 42 topics and 861 comparison pairs.")
prompt("When you quit with 'q', you'll see all the topics you've compared.")
print("")

for topic1, topic2 in uncompared_pairs:
    if topic1 not in topics_so_far:
        topics_so_far.append(topic1)
    if topic2 not in topics_so_far:
        topics_so_far.append(topic2)

    print(f"1. {topic1}")
    print(f"2. {topic2}")
    user_input = input("> Enter 1, 2, or 'q' to quit: ")

    while user_input not in ['1', '2', 'q']:
        print("~~> Invalid. Please enter 1, 2, or 'q'.")
        user_input = input("> Enter 1, 2, or 'q' to quit: ")

    if user_input == 'q':
        break

    if user_input == '1':
        topic_scores[topic1] += 1
        topic_scores[topic2] -= 1
        more_difficult[topic1] += 1
        less_difficult[topic2] += 1
    elif user_input == '2':
        topic_scores[topic2] += 1
        topic_scores[topic1] -= 1
        more_difficult[topic2] += 1
        less_difficult[topic1] += 1

    print("")

    pair = tuple(sorted((topic1, topic2)))
    compared_pairs.add(pair)

    topics_so_far.sort(key=get_score_and_comparisons, reverse=True)
    topics_to_print = topics_so_far[:6]

    if topic1 not in topics_to_print:
        topics_to_print.append(topic1)

    if topic2 not in topics_to_print:
        topics_to_print.append(topic2)

    topics_to_print.sort(key=get_score_and_comparisons, reverse=True)
    # Only printing 6-8 topics to keep the output readable:
    # 6 most difficult topics + the 2 topics the user has just compared,
    # if they are not in the top 6.

    for topic_to_print in topics_to_print:
        score = topic_scores[topic_to_print]
        more = more_difficult[topic_to_print]
        less = less_difficult[topic_to_print]

        if topic_to_print in (topic1, topic2):
            asterisk_or_space = '* '
        else:
            asterisk_or_space = '  '

        print(f"{asterisk_or_space}{score} ({more}/{less}): {topic_to_print}")

    print("")

print("")
print("~~> Full ranking:")
print("")

if not compared_pairs:
    print("~~> No topics were ranked.")
else:
    full_sorted_topics = sorted(topics_so_far, key=get_score_and_comparisons, reverse=True)

    for topic in full_sorted_topics:
        score = topic_scores[topic]
        more = more_difficult[topic]
        less = less_difficult[topic]
        print(f"{score} ({more}/{less}): {topic}")

    print("")

    if len(compared_pairs) == MAX_PAIRS:
        print("~~> You've compared everything to everything else!")

    difficult_topics = []

    for topic in full_sorted_topics:
        if topic_scores[topic] > 0:
            difficult_topics.append(topic)

    if (len(full_sorted_topics) > 2 and
        len(difficult_topics) >= 2 and
        (topic_scores[full_sorted_topics[1]] > topic_scores[full_sorted_topics[2]])):
        print(f"~~> Most difficult: 1. {difficult_topics[0]}. 2. {difficult_topics[1]}. You got this.")
    # This is not necessary and requires 3 checks and looks confusing,
    # but when there are two topics with a positive difficulty score,
    # that also have a higher score than the other topics,
    # I wanted to print a message highlighting those.

    elif len(difficult_topics) >= 1:
        print(f"~~> Keep focusing on {difficult_topics[0]}. You got this.")
     # For any other situation when any topic has a positive difficulty score.

    elif len(difficult_topics) == 0:
        print("~~> No topic is more difficult than any other. You got this.")
        print("~~> Feel free to rank topics again, if you want more info.")