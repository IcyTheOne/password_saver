from django.shortcuts import render
from .models import SavedAccount

webSiteImages = [
    {
        'websiteName': 'linkedin',
        'websiteImageUrl': 'https://www.kinesisinc.com/wp-content/uploads/2020/04/linkedin-101-hero@2x.png'
    },
    {
        'websiteName': 'Discord.com',
        'websiteImageUrl': 'https://fiverr-res.cloudinary.com/images/t_main1,q_auto,f_auto,q_auto,f_auto/gigs/134280614/original/9e46d93ff60530cf5f07118c6f961c68294179b9/create-an-icon-for-a-discord.jpg',
    },
    {
        'websiteName': 'YouTube.com',
        'websiteImageUrl': 'https://9to5google.com/wp-content/uploads/sites/4/2018/09/youtube_logo_dark.jpg?quality=82&strip=all',
    }
]

# Create your views here.

def home(request):
    context = {
        'title':'Home',
        'webSiteInfoList': SavedAccount.objects.all(),
        'webSiteImages':webSiteImages
    }
    return render(request, 'vault/home.html', context)