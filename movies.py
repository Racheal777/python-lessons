favorite_movies = []

num = 5
new_movie = ""
# the number of times a user has to input the movie
for i in range(num):

    # if the favorist list is greater than 0, then subtract the 1 form the number and display it
    if len(favorite_movies) > 0:
        new_movie = input(f"Add {num - i}. more > ")
    else:
        # else just enter this heading with a new line saying add the count more
        new_movie = input(f"Enter Your {num} favorite movies\nAdd {num - i}. more > ")
    # add the movie to the end of the list and convert all movies to lowercase
    favorite_movies.append(new_movie.lower())

print(favorite_movies)

# display all movies using the range and the length
print(f"Your favorite movies are ")
for i in range(len(favorite_movies)):
    print(f" {i+1}. {favorite_movies[i]}")

# get an input to remove the movie
removed_movie = input('Type a movie you want to remove > ')

removed_movie.lower()
# if movie entered, change it to lower case and check if its in the favorite movie
if removed_movie in favorite_movies:
    # if movie is in the list, remove it
    favorite_movies.remove(removed_movie)
    # and print the movie you have removed
    print(f"Your {removed_movie} movie has been removed from your favorite list")

    #else print the movie is not in the list
else:
    print(f"The {removed_movie} movie is not in the favorite list")

print(f"Your updated favorite movies are ")
for i in range(len(favorite_movies)):
    print(f" {i+1}. {favorite_movies[i]}")

