"""
Activity Rank module
 get the most recommended modules for a user based on their likes
"""


if __name__ == "__main__":
    import sys
    if len(sys.argv) > 2:
        first = sys.argv[1]
        second = sys.argv[2]
        print first, second
    else:
        print "Improper usage"
