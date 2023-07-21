from django.shortcuts import render

posts = [
	{
		'author':'John',
		'title':'Blog 1',
		'content': 'First Blog Content',
		'date_posted': 'June 26, 2023'
	},
	{
		'author':'Tom',
		'title':'Blog 2',
		'content': 'Second Blog Content',
		'date_posted': 'June 27, 2023'
	}
]

# Create your views here.
def home(request):
	context = {
		'posts' : posts
	}
	return render(request, 'blog/home.html', context)
    
def about(request):
	return render(request, 'blog/about.html', {'title':'about'})