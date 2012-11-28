"""
Activity Rank module
 get the most recommended modules for a user based on their likes
"""


"""
Each activity, with all of its categories
the set of categories we are trying to match
    possibly weighted?

"""



if __name__ == "__main__":
    import sys
    if len(sys.argv) > 2:
        first = sys.argv[1]
        second = sys.argv[2]
        print first, second
    else:
        print "Improper usage"
