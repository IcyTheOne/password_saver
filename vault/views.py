from django.shortcuts import render
from users.models import SavedAccount

webSiteInfoList = [
    {
        'websiteName': 'LinkedIn.com',
        'websiteUrl': 'https://www.linkedin.com/https://www.linkedin.com/',
        'websiteImage': 'https://www.kinesisinc.com/wp-content/uploads/2020/04/linkedin-101-hero@2x.png',
        'emailSpecial': 'user_surname@hotmail.com',
        'usernameSpecial': 'Dimian',
        'passwordSpecial': 'saf3Sdsf?d@!dsK'
    },
    {
        'websiteName': 'Discord.com',
        'websiteUrl': 'https://www.discord.com',
        'websiteImage': 'https://fiverr-res.cloudinary.com/images/t_main1,q_auto,f_auto,q_auto,f_auto/gigs/134280614/original/9e46d93ff60530cf5f07118c6f961c68294179b9/create-an-icon-for-a-discord.jpg',
        'emailSpecial': 'user_surname@hotmail.com',
        'usernameSpecial': 'bobos',
        'passwordSpecial': 'sdf@kJ$LK12#?saL_S'
    },
    {
        'websiteName': 'YouTube.com',
        'websiteUrl': 'https://www.youtube.com',
        'websiteImage': 'https://9to5google.com/wp-content/uploads/sites/4/2018/09/youtube_logo_dark.jpg?quality=82&strip=all',
        'emailSpecial': 'user_surname@hotmail.com',
        'usernameSpecial': 'bobos',
        'passwordSpecial': 'sg$k@34LK12#?sm.8%kkj'
    }
]

# Create your views here.

def home(request):
    context = {
        'title':'Home',
        'webSiteInfoList': SavedAccount.objects.all()
    }
    return render(request, 'vault/home.html', context)