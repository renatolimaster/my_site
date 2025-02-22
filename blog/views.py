from datetime import date
from django.shortcuts import render

all_posts = [
    {
    "slug": "hike-in-the-mountains",
    "image": "mountains.jpg",
    "author": "Yours Truly",
    "date": date(2021, 7, 21),
    "title": "Mountain Hiking",
    "excerpt": "There's nothing like hiking in the mountains!...",
    "content": """
      Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
      aperiam est praesentium, quos iste consequuntur nemo exercitationem
      repellat debitis possimus neque solve
      Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
      aperiam est praesentium, quos iste consequuntur nemo exercitationem
      repellat debitis possimus neque soluta, id asperiores perferendis
      dolorem assumenda distinctio.
    """
    },
    {
    "slug": "programming-is-fun",
    "image": "coding.jpg",
    "author": "Cristiane Lima",
    "date": date(2022, 3, 10),
    "title": "Programming Is Great!",
    "excerpt": "Did you ever spend hours searching that one error in your code?...",
    "content": """
      Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
      aperiam est praesentium, quos iste consequuntur nemo exercitationem
    """
    },
    {
    "slug": "into-the-woods",
    "image": "woods.jpg",
    "author": "Yours Truly",
    "date": date(2020, 8, 5),
    "title": "Woods",
    "excerpt": "There's nothing like the views you get when hiking in the mountains! And I wasn't even prepared for what happened whilst I was enjoying the view!",
    "content": """
      Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
      aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
      velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

      Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
      aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
      velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

      Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
      aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
      velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.
    """
    },
    {
    "slug": "travel-essentials",
    "image": "travel.jpg",
    "author": "renato lima",
    "date": date(2021, 12, 15),
    "title": "Traveling",
    "excerpt": "Traveling is so much fun, but it can be stressful too!...",
    "content": """
      Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
      aperiam est praesentium, quos iste consequuntur nemo exercitationem
      repellat debitis possimus neque soluta, id asperiores perferendis
      dolorem assumenda distinctio.
      Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
      """,      
      "excerpt": "There's nothing like the views you get when hiking in the mountains! And I wasn't even prepared for what happened whilst I was enjoying the view!",
      "content": """
      Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
      aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
      velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.""",
    },
]

def get_date(post):
    return post['date']

# Create your views here.
def starting_page(request):
    sorted_posts = sorted(all_posts, key=get_date)
    latest_posts = sorted_posts[-3:]
    context = {
        "posts": latest_posts,
    }
    return render(request, "blog/index.html", context)

def posts(request):
     
    context = {
        "all_posts": all_posts,
    }
    return render(request, "blog/all-posts.html", context) 

def post_detail(request, slug):    
    post = next((post for post in all_posts if post["slug"] == slug), None)    
    if post is not None:
        context = {
            "post": post,
        }
        return render(request, "blog/post-detail.html", context)
    else:
        return render(request, "404.html")
