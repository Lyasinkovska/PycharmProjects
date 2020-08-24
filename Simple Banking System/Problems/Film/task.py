import sys
msg = sys.stdin.readlines()
movie = msg[0].rstrip("\n")
director = msg[1].rstrip("\n")
year = msg[2].rstrip("\n")
print("{} (dir. {}) came out in {}".format(movie, director, year))