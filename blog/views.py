from django.shortcuts import render
from datetime import date

posts = [
    {
        "slug": "hike-in-the-mountains",
        "image": "mountains.jpg",
        "author": "Suraj",
        "date": date(2023, 7, 3),
        "title": "Mountain Hiking",
        "excerpt": "There's nothing like the views you get when hiking in the mountains! And I wasn't even prepared for what happened halfway through.",
        "content": """
            <p>Mountain hiking can be an intimidating experience. You're out there, surrounded by nature, with no one else around for miles. It's just you and the elements. But it doesn't have to be scary! Here are some tips to help you get started on your next adventure:</p>
            <ul>
                <li>Wear layers - this will help regulate your body temperature as you climb up or down mountainsides.</li>
                <li>Bring plenty of water - dehydration is one of the biggest dangers when hiking in high altitudes.</li>
                <li>Make sure you have enough food - if you're going on a long hike, make sure to pack snacks and meals that will keep your energy levels up.</li>
            </ul>
            """
    }
]

# Create your views here.

def starting_page(request):
    return render(request, "blog/index.html")

def posts(request):
    return render(request, "blog/all-posts.html")

def post_detail(request, slug):
    return render(request, "blog/post-detail.html")