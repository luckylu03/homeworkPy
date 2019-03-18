# Jason's textbooks are all out of order! Help him sort a list (ArrayList in java) 
# full of textbooks by subject, so he can study before the test.

def sorter(textbooks):
    return sorted(textbooks, key=lambda st: st.lower())