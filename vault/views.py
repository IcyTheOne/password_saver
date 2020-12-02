from django.shortcuts import render

webSiteInfoList = [
    {
        'website':'LinkedIn.com',
        'img_source':'https://www.kinesisinc.com/wp-content/uploads/2020/04/linkedin-101-hero@2x.png',
        'url':'https://www.linkedin.com/https://www.linkedin.com/',
        'email':'user_surname@hotmail.com',
        'username':'Dimian',
        'password':'saf3Sdsf?d@!dsK'
    },
    {
        'website':'Discord.com',
        'img_source':'https://fiverr-res.cloudinary.com/images/t_main1,q_auto,f_auto,q_auto,f_auto/gigs/134280614/original/9e46d93ff60530cf5f07118c6f961c68294179b9/create-an-icon-for-a-discord.jpg',
        'url':'https://www.discord.com',
        'email':'user_surname@hotmail.com',
        'username':'bobos',
        'password':'sdf@kJ$LK12#?saL_S'
    },
    {
        'website':'YouTube.com',
        'img_source':'https://9to5google.com/wp-content/uploads/sites/4/2018/09/youtube_logo_dark.jpg?quality=82&strip=all',
        'url':'https://www.youtube.com',
        'email':'user_surname@hotmail.com',
        'username':'bobos',
        'password':'sg$k@34LK12#?sm.8%kkj'
    }
]

# Create your views here.

def home(request):
    context = {
        'title':'Home',
        'webSiteInfoList': webSiteInfoList
    }
    return render(request, 'vault/home.html', context)