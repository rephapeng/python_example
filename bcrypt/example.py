import bcrypt
password = "phapengmarupeng"
# Hash a password for the first time, with a certain number of rounds
hashed = bcrypt.hashpw(password, bcrypt.gensalt(15))
hashed = "$2b$15$1h4xXNkmMPzYqmlIE2zRbeP6JM14Srli8BBY/ATUw/FT0iQNJ3hs."
# Check that a unhashed password matches one that has previously been
#   hashed
if bcrypt.hashpw(password, hashed) == hashed:
   print("It Matches!")
else:
    print("It Does not Match :(")