from youngun.apps.campaigns.models import Campaign


def update_campaign_livecnt():
    for camp in Campaign.objects.all():
        if camp:
            camp.live_fb_posts = camp.get_facebook_posts.count()
            camp.live_in_posts = camp.get_instagram_posts.count()
            camp.live_tw_posts = camp.get_twitter_posts.count()

            camp.live_fb_stories = camp.get_facebook_stories.count()
            camp.live_in_stories = camp.get_instagram_stories.count()
            camp.live_tw_stories = camp.get_twitter_stories.count()

            camp.save()
