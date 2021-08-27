from collections import Counter, defaultdict  # not loaded by default


# List of the data scientists network
users = [
    {'id': 0, 'name': 'Hero'},
    {'id': 1, 'name': 'Dunn'},
    {'id': 2, 'name': 'Sue'},
    {'id': 3, 'name': 'Chi'},
    {'id': 4, 'name': 'Thor'},
    {'id': 5, 'name': 'Clive'},
    {'id': 6, 'name': 'Hicks'},
    {'id': 7, 'name': 'Devin'},
    {'id': 8, 'name': 'Kate'},
    {'id': 9, 'name': 'Klein'},
]

# List of friendships between the scientists
friends_pairs = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (3, 4),
                 (4, 5), (5, 6), (5, 7), (6, 8), (7, 8), (8, 9)]

# Initialize the dict with and empty list for each user id:
friendships = {user['id']: [] for user in users}

# And loop over the friendship pairs ot populate it:
for i, j in friends_pairs:
    friendships[i].append(j)  # Add j as a friend of user i
    friendships[j].append(i)  # Add i as a friend of user j


def number_of_friends(user):
    """How many friends does the _user_ have?"""
    user_id = user['id']
    friends_ids = friendships[user_id]
    return len(friends_ids)


total_connections = sum(number_of_friends(user) for user in users)
assert total_connections == 24, f'The total connections must be 24, not {total_connections}'

num_users = len(users)  # length of the users list
avg_connections = total_connections / num_users

assert avg_connections == 2.4, f'The average connections must be 2.4, not {avg_connections}'

# Create a list (user_id, number_of_friends)
num_friends_by_id = [(user['id'], number_of_friends(user)) for user in users]

num_friends_by_id.sort(                             # Sort the list
    key=lambda id_and_friends: id_and_friends[1],   # by the num of friends
    reverse=True                                    # Greather to smaller
)


def foaf_ids_bad(user):
    """foaf is a short for 'friend of a friend' """
    return [foaf_id
            for friend_id in friendships[user['id']]
            for foaf_id in friendships[friend_id]]


# This is because we dont disting the current user
# and repeated friends
assert foaf_ids_bad(users[0]) == [0, 2, 3, 0, 1, 3]

assert friendships[0] == [1, 2]
assert friendships[1] == [0, 2, 3]
assert friendships[2] == [0, 1, 3]


def friend_of_friends(user):
    user_id = user['id']
    return Counter(
        foaf_id
        for friend_id in friendships[user_id]   # for each of my friends
        for foaf_id in friendships[friend_id]   # find their friends
        if foaf_id != user_id                   # who aren't me
        and foaf_id not in friendships[user_id]  # and not yet my friend

    )


# This means that the user with id = 3 Chi has
# 2 mutual friends with user 0, and 1 mutual friend with user 5
assert friend_of_friends(users[3]) == Counter({0: 2, 5: 1})


interests = [
    (0, "Hadoop"), (0, "Big Data"), (0, "HBase"), (0, "Java"),
    (0, "Spark"), (0, "Storm"), (0, "Cassandra"),

    (1, "NoSQL"), (1, "MongoDB"), (1, "Cassandra"), (1, "HBase"),
    (1, "Postgres"), (2, "Python"), (2, "scikit-learn"),
    (2, "scipy"), (2, "numpy"), (2, "statsmodels"), (2, "pandas"),

    (3, "R"), (3, "Python"), (3, "statistics"),
    (3, "regression"), (3, "probability"),

    (4, "machine learning"), (4, "regression"),
    (4, "decisiontrees"), (4, "libsvm"),

    (5, "Python"), (5, "R"), (5, "Java"), (5, "C++"),
    (5, "Haskell"), (5, "programming languages"),

    (6, "statistics"), (6, "probability"),
    (6, "mathematics"), (6, "theory"),

    (7, "machine learning"), (7, "scikit-learn"),
    (7, "Mahout"), (7, "neural networks"),

    (8, "neural networks"), (8, "deep learning"),
    (8, "Big Data"), (8, "artificial intelligence"),

    (9, "Hadoop"), (9, "Java"), (9, "MapReduce"), (9, "Big Data")
]


def data_scientists_who_like(target_interest):
    """Find the ids of all users who like the target interest."""
    return [user_id
            for user_id, user_interest in interests
            if user_interest == target_interest]


# Keys are interests, values are lists of user_ids with that interest
user_id_by_interest = defaultdict(list)

for user_id, interest in interests:
    user_id_by_interest[interest].append(user_id)

interest_by_user_id = defaultdict(list)

for user_id, interest in interests:
    interest_by_user_id[user_id].append(interest)


def most_common_interest_with(user):
    return Counter(
        interested_user_id
        for interest in interest_by_user_id[user['id']]
        for interested_user_id in user_id_by_interest[interest]
        if interested_user_id != user['id']
    )

assert most_common_interest_with(users[0]) == Counter({9: 3, 1: 2, 8: 1, 5: 1})


salaries_and_tenures = [(83000, 8.7), (88000, 8.1),
                        (48000, 0.7), (76000, 6),
                        (69000, 6.5), (76000, 7.5),
                        (60000, 2.5), (83000, 10),
                        (48000, 1.9), (63000, 4.2)]

def plot_salary_graph():
    from matplotlib import pyplot as plt

    x = [tenure[1] for tenure in salaries_and_tenures]
    y = [salary[0] for salary in salaries_and_tenures]

    plt.scatter(x, y)
    plt.title('Salary by Years Experience')
    plt.xlabel('Years Experience')
    plt.ylabel('Salary')
    plt.show()

# plot_salary_graph()

salary_by_tenure = defaultdict(list)

# Keys are years, values are lists of salaries
for salary, tenure in salaries_and_tenures:
    salary_by_tenure[tenure].append(salary)

# print(salary_by_tenure)

average_salary_by_tenure = {
    tenure: sum(salaries) / len(salaries)
    for tenure, salaries in salary_by_tenure.items()
}

# print(average_salary_by_tenure)

def tenure_bucket(tenure):
    if tenure < 2:
        return 'less than two'
    elif tenure < 5:
        return 'between two and five'
    else:
        return 'more thant five'

salary_by_tenure_bucket = defaultdict(list)

for salary, tenure in salaries_and_tenures:
    bucket = tenure_bucket(tenure)
    salary_by_tenure_bucket[bucket].append(salary)

average_salary_by_bucket = {
    tenure_bucket: sum(salaries) / len(salaries)
    for tenure_bucket, salaries in salary_by_tenure_bucket.items()
}

def predict_paid_or_unpaid(years_experience):
    if years_experience < 3.0:
        return "paid"
    elif years_experience < 8.5:
        return "unpaid"
    else:
        return "paid"


# Working with text
words_and_counts = Counter(word
                        for _, interest in interests
                        for word in interest.lower().split())

for word, count in words_and_counts.most_common():
    if count > 1:
        print(word, count)
