import csv

from django import forms
from django.contrib import messages

from .models import Campaign
from youngun.apps.content.models import Post


class ImportPostForm(forms.ModelForm):
    import_posts_csv = forms.FileField(allow_empty_file=True, required=False)

    class Meta:
        model = Campaign
        fields = [
            'name',
            'brand',
            'status',
            'import_posts_csv',
            'particaipating_profiles',
            'unique_content_pieces',
            'approved_content_pieces',
            'in_posts', 'live_in_posts',
            'in_stories',
            'live_in_stories',
            'fb_posts',
            'live_fb_posts',
            'fb_stories',
            'live_fb_stories',
            'tw_posts',
            'tw_stories',
            'live_tw_posts',
            'live_tw_stories',
        ]

    def save(self, commit=True, *args, **kwargs):
        m = super(ImportPostForm, self).save(commit=False)
        print(self.cleaned_data)
        file_csv = self.cleaned_data["import_posts_csv"]

        cnt = 0

        if not file_csv is None:

            fld = file_csv.read()
            parsed_fl = fld.decode("utf-8")
            posts_list = parsed_fl.split("\n")
            posts_list = [x for x in posts_list if x]
            print(posts_list)

            for post in posts_list:
                p_obj, created = Post.objects.get_or_create(
                    campaign=self.instance, url=post)
                if created:
                    cnt = cnt + 1

                if "facebook.com" in post:
                    p_obj.platform = "fb"
                    if "/video/" in post:
                        p_obj.post_type = "video"
                    else:
                        p_obj.post_type = "post"
                elif "instagram.com" in post:
                    p_obj.platform = "in"
                    p_obj.embed_code = ""
                elif "twitter.com" in post:
                    p_obj.platform = "tw"
                    p_obj.embed_code = ""

                p_obj.save()

            if commit:
                m.save()

            return m

        print("%d Posts Added" % cnt)
