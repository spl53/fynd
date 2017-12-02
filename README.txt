# fynd
movies details based on restfull api

# Insert Json data
for i in aa:
    ms = MoviesInfo.objects.create(popularity = i['99popularity'], director=i['director'], imdb_score = i['imdb_score'], name=i['name'],release_on = datetime.now(),admin_id = 1)
    for each in i['genre']:
       GenreInfo.objects.create(movie=ms, genre = each)

#INSTALL PACKAGE

1. pip install django==1.10


URLS:

movies details
1. localhost:8000/imdb/movies/
	1.1 GET request to fetch the result 
	1.2 POST Request to update the movies details 
		PARAMS: required = {'user_id':<admin id >,'id':<movie_id>,'genre_id':<genre_id>}
			optional = {any field whichever is required to update}
	1.3 PUT Request to add new entry of movies
		PARAMS: All field required 
			{
			"name": "The Godfather",
			"popularity": 92,
			"director": "Francis Ford Coppola",
			"imdb_score": 9.2,
			"genre": "Crime",
			"genre_id": 34,
			"id": 11,
			"release_on": "2017-11-13 11:18:57 PM",
			"user_id":<admin user's id>
		       },
	1.4 DELETE Request to delete the movies info
		PARAMS: required {user_id:<admin user's id ,id:<movie id>}



# serch the movie by name
2. localhost:8000/imdb/search_movie?name=The
	PARAM: {name: <matching name of movies>} 
