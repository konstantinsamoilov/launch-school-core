# fix instant 'q': 
# Keep focusing on {full_sorted_topics[0]} (and all the other stuff)!
# Keep focusing on {full_sorted_topics[0]} (and all the other stuff)!

# fix 'q':
# Keep focusing on {full_sorted_topics[0]} (and all the other stuff)!
# numbers and variables: variables as pointers are the most difficult right now!
# Who knew? Probably you already knew. Anyway, you got this.
# numbers and variables: variables as pointers are the most difficult right now!
# Who knew? Probably you already knew. Anyway, you got this.
# ...

# ---

# ~ What to study next? PY109 study guide difficulty ranker ~

# Since we should compare any particular topic against others at least ~3 times
# to have meaningful output, the comparison pairs are totally randomized.
# So maybe you'll see a topic 4 times before you see
# some other topic at all, but I think that's ok here...

# A pair of two topics that have been compared
# will not be compared again against one another.

# I thought about lightly editing the study guide
# for this program, but left it as is, for familiarity.

# It would've been nice to do a single key press, without enter, but that's not PY101-109 stuff.

import random

TOPICS = [
    "naming conventions: legal vs. idiomatic, illegal vs. non-idiomatic",
    "type coercions: explicit (e.g., using int(), str()) and implicit",
    "numbers",
    "strings",
    "f-strings",
    "string methods: capitalize, swapcase, upper, lower",
    "string methods: isalpha, isdigit, isalnum, islower, isupper, isspace",
    "string methods: strip, rstrip, lstrip, replace",
    "string methods: split, find, rfind",
    "boolean vs. truthiness",
    "None",
    "ranges",
    "list and dictionary syntax",
    "list methods: list.append(), list.pop(), list.reverse()",
    "dictionary methods: dict.keys(), dict.values(), dict.items(), dict.get()",
    "slicing (strings, lists, tuples)",
    "Arithmetic operators: +, -, *, /, //, %, **",
    "String operators: +",
    "List operators: +",
    "Comparison operators: ==, !=, <, >, <=, >=",
    "Logical operators: and, or, not",
    "Identity operators: is, is not",
    "operator precedence",
    "mutability and immutability",
    "pass by object reference",
    "variables: naming conventions",
    "variables: initialization, assignment, and reassignment",
    "variables: scope",
    "variables: global keyword",
    "variables: variables as pointers",
    "variables: variable shadowing",
    "conditionals and loops: for",
    "conditionals and loops: while",
    "the len() function",
    "print() and input()",
    "exceptions (when they will occur and how to handle them)",
    "Functions: definitions and calls",
    "Functions: return values",
    "Functions: parameters vs. arguments",
    "Functions: nested functions",
    "Functions: output vs. return values, side effects",
    "expressions and statements",
]

topic_scores = {topic: 0 for topic in TOPICS}
more_difficult = {topic: 0 for topic in TOPICS}
less_difficult = {topic: 0 for topic in TOPICS}

topics_so_far = []

compared_pairs = set() 

NUM_TOPICS = len(TOPICS) # NUM_TOPICS and MAX_PAIRS weren't constants at first but Pylint correctly said that they should be.

MAX_PAIRS = (NUM_TOPICS * (NUM_TOPICS - 1)) // 2 # Topics, multiplied by all the other topics (topics - 1), divided by 2 because we don't want to consider the reverse order (we only need A & B, not B & A too).

def get_score(topic):
    return topic_scores[topic]

def prompt(message):
    print(f"~~> {message}")

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
prompt("Hi. I'll give you two randomized topics from the PY109 study guide... ")
prompt("And you tell me which one is more difficult right now!")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
prompt("After comparing a few, you'll see 6-8 of your most difficult topics,")
prompt("always including the two you've just compared with an asterisk '*', ")
prompt("and a '(0/0)' counter, showing how many times a topic was more/less difficult.")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
prompt("Every comparison pair is unique. There are 861 comparisons.")
prompt("There are 41 topics, so each topic has 40 comparisons.")
prompt("If you quit with 'q', you'll see all the topics you've compared.")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

while True:
    if len(compared_pairs) >= MAX_PAIRS:
        prompt("You've compared everything to everything else! Wow.")
        break

    while True: # Sometimes I have empty lines between interconnected blocks of code, like in this nested loop, because it's easier for me to read.
        topic1 = random.choice(TOPICS)
        topic2 = random.choice(TOPICS)

        if topic1 == topic2: # another option is: while topic1 == topic2:
            continue #                                topic2 = random.choice(TOPICS)

        pair = tuple(sorted((topic1, topic2)))

        if pair not in compared_pairs:
            break

    if topic1 not in topics_so_far:
        topics_so_far.append(topic1)
    if topic2 not in topics_so_far:
        topics_so_far.append(topic2)

    prompt(f"1. {topic1}")
    prompt(f"2. {topic2}")
    user_input = input("> Enter 1, 2, or 'q' to quit: ")

    while user_input not in ['1', '2', 'q']:
        print("Nothing else, sorry! Please enter 1, 2, or 'q'.")
        user_input = input("> Enter 1, 2, or 'q' to quit: ")

    if user_input == 'q':
        break

    if user_input == '1':
        topic_scores[topic1] += 1
        topic_scores[topic2] -= 1
        more_difficult[topic1] += 1
        less_difficult[topic2] += 1
        print("-------------------------------------------------------------------")
    elif user_input == '2':
        topic_scores[topic2] += 1
        topic_scores[topic1] -= 1
        more_difficult[topic2] += 1
        less_difficult[topic1] += 1
        print("-------------------------------------------------------------------")

    compared_pairs.add(pair)

    sorted_topics = sorted(topics_so_far, key=get_score, reverse=True)

    top_six = sorted_topics[:6]

    topics_to_print = list(top_six)

    if topic1 not in topics_to_print:
        topics_to_print.append(topic1)
    if topic2 not in topics_to_print:
        topics_to_print.append(topic2)

    for topic_to_print in topics_to_print:
        score = topic_scores[topic_to_print]
        more = more_difficult[topic_to_print]
        less = less_difficult[topic_to_print]

        asterisk = '* ' if topic_to_print in (topic1, topic2) else ' '

        print(f"{asterisk}{score} ({more}/{less}): {topic_to_print}")

    print("-------------------------------------------------------------------")

print("Full ranking:")

if not topics_so_far:
    print("No topics were ranked. How could you...")
else:
    full_sorted_topics = sorted(topics_so_far, key=get_score, reverse=True) # We populate this list in the same way we populated sorted_topics, but we need to create it (or initialize sorted_topics before the main while loop) because we'd get a NameError (variable not created yet) here otherwise.

    for topic in full_sorted_topics:
        score = topic_scores[topic]
        more = more_difficult[topic]
        less = less_difficult[topic]
        print(f"{score} ({more}/{less}): {topic}")

    print("-------------------------------------------------------------------")

    most_difficult_topics = []

    for topic in full_sorted_topics: # LSBot suggested a list comprehension but I'm not as familiar with those, so I'm using this.
        if topic_scores[topic] > 0:
            most_difficult_topics.append(topic)

        if len(most_difficult_topics) >= 2: # (If there are at least two topics with positive difficulty values, print those.)
            hardest1 = full_sorted_topics[0]
            hardest2 = full_sorted_topics[1]
            print(f"{full_sorted_topics[0]} and {full_sorted_topics[1]} are the most difficult right now!")
            print("Who knew? Probably you already knew. Anyway, you got this.")

        elif len(full_sorted_topics) >= 1: # (For any other case, as long as any items were ranked.)
            hardest1 = full_sorted_topics[0]
            print("Keep focusing on {full_sorted_topics[0]} (and all the other stuff)!")