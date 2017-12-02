from django.shortcuts import render_to_response,render
from imdb.models import *
from django.db.models import F
from django.http import HttpResponse,HttpResponseServerError
import json
from django.http import QueryDict
# Create your views here.

def has_admin_permission(user_id):
	is_admin = Group.objects.get(name="admin").user_set.filter(id=user_id).exists()
        return is_admin


def movies(request):
	if request.method == 'GET':	
		queryset = list(MoviesInfo.objects.all().annotate(genre=F('genres__genre'),genre_id=F('genres__id')).\
			extra(select={'release_on':"CONVERT(DATE_FORMAT(CONVERT_TZ(movies_info.release_on,'+00:00','+05:30'),'%%Y-%%m-%%d %%r'), CHAR)"}).\
			values('id','genre_id','popularity','director','imdb_score','name','genre','release_on'))
		return HttpResponse(json.dumps(queryset))
	if request.method == 'POST':
		if has_admin_permission(request.POST.get('user_id')):
			mv_id = request.POST.get('id')
			genre_id = request.POST.get('genre_id')
			
			if mv_id and genre_id:

				mvs = MoviesInfo.objects.get(id = mv_id)
				if request.POST.get('popularity') :
					mvs.popularity = request.POST.get('popularity')
				if request.POST.get('director'):
					mvs.director = request.POST.get('director')
				if request.POST.get('imdb_score'):
					mvs.imdb_score = request.POST.get('imdb_score')
				if request.POST.get('name'):
					mvs.name = request.POST.get('name')
				if request.POST.get('release_on'):
					mvs.release_on = request.POST.get('release_on')
				mvs.admin_id = request.POST.get('user_id')
				
				genre_obj = GenreInfo.objects.get(id = genre_id)
				if request.POST.get('genre'):
					genre_obj.genre = request.POST.get('genre')
				
				mvs.save()
				genre_obj.save()
				return HttpResponse("Details Updated successfully")
			else:
				return HttpResponse("No id and genre_id found")
		else:
			return HttpResponseServerError("Not Authorised")

	if request.method == 'PUT':
		req = QueryDict(request.body)
		if has_admin_permission(req.get('user_id')):
			mv_id = req.get('id')
			genre_id = req.get('genre_id')

			if mv_id and genre_id:

				mvs = MoviesInfo()
				mvs.popularity = req.get('popularity')
				mvs.director = req.get('director')
				mvs.imdb_score = req.get('imdb_score')
				mvs.name = req.get('name')
				mvs.release_on = req.get('release_on')
				mvs.admin_id = req.get('user_id')
				mvs.save()
				
				genre_obj = GenreInfo()
				genre_obj.movie = mvs
				genre_obj.genre = req.get('genre')
				genre_obj.save()
				
				return HttpResponse("Details saved successfully")
			else:
				return HttpResponse("No id and genre_id found")
		else:
			return HttpResponseServerError("Not Authorised")

	if request.method == 'DELETE':
		req = QueryDict(request.body)
		if has_admin_permission(req.get('user_id')):
			mv_id = req.get('id')

			if mv_id :
				mvs = MoviesInfo.objects.get(id = mv_id)
				mvs.delete()
				
				return HttpResponse("Details Deleted successfully")
			else:
				return HttpResponse("No id and genre_id found")
		else:
			return HttpResponseServerError("Not Authorised")

def search_movie(request):
	"""
	This view return the result for the search on name i.e on movies name "
	"""
	if request.method == 'GET':	
		name = request.GET.get('name', None)
		if name is not None:
			queryset = list(MoviesInfo.objects.filter(name__contains=name).annotate(genre=F('genres__genre'),genre_id=F('genres__id')).\
                        extra(select={'release_on':"CONVERT(DATE_FORMAT(CONVERT_TZ(movies_info.release_on,'+00:00','+05:30'),'%%Y-%%m-%%d %%r'), CHAR)"}).\
			values('id','genre_id','popularity','director','imdb_score','name','genre','release_on'))
		else:
			queryset = None
		return HttpResponse(json.dumps(queryset))
