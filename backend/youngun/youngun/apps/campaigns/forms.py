import csv

from django import forms
from django.contrib import messages
from django.utils.html import format_html

from .tasks import bulk_upload_csv

from .models import Campaign
from youngun.apps.content.models import Post


class ImportPostForm(forms.ModelForm):
    import_posts_csv = forms.FileField(allow_empty_file=True, required=False)
    # link_to_in_posts = forms.URLField(
    #     label="Instagram Posts", max_length=400, required=False)

    # def __init__(self, *args, **kwargs):
    #     super(ImportPostForm, self).__init__(*args, **kwargs)
    #     obj = kwargs["instance"]
    #     link = "/admin/content/instagrampost/?campaign__name=" + obj.name
    #     p_name = format_html('<a href="{}">{}</a>', link, obj.name)
    #     self.fields['link_to_in_posts'].initial = link
    #     print(kwargs)
    #     print(type(kwargs))
    #     print(kwargs.keys())
    #     print(kwargs["instance"].brand)

    class Meta:
        model = Campaign
        fields = [
            'name',
            # 'link_to_in_posts',
            'status',
            'import_posts_csv',
            'twitter_collection_url',
            'in_stories_google_photos_album_url',
            'in_stories_fetch_ctrl',
            'fb_stories_google_photos_album_url',
            'fb_stories_fetch_ctrl',
            'tw_stories_google_photos_album_url',
            'tw_stories_fetch_ctrl',
            'particaipating_profiles',
            'unique_content_pieces',
            'approved_content_pieces',

            'in_posts',
            # 'live_in_posts_cnt',

            'in_stories',
            # 'live_in_stories_cnt',

            'fb_posts',
            # 'live_fb_posts_cnt',

            'fb_stories',
            # 'live_fb_stories_cnt',

            'tw_posts',
            # 'live_tw_posts_cnt',

            'tw_stories',
            # 'live_tw_stories_cnt',

            'in_engagement',
            'tw_engagement',
            'fb_engagement',
            'in_reach',
            'tw_reach',
            'fb_reach'
        ]

        widgets = {
            'name': forms.TextInput(attrs={'readonly': 'readonly'}),
            'status': forms.TextInput(attrs={'readonly': 'readonly'}),
            # 'name': forms.TextInput(attrs={'readonly': 'readonly', 'disabled': 'disabled'}),
        }

    def gen_link_to_in_posts(self, obj):
        link = "/admin/content/instagrampost/?campaign__name=" + obj.name
        return format_html('<a href="{}">{}</a>', link, obj.name + "Posts")

    def save(self, commit=True, *args, **kwargs):
        m = super(ImportPostForm, self).save(commit=False)
        print(self.cleaned_data)
        file_csv = self.cleaned_data["import_posts_csv"]

        if not file_csv is None:

            fld = file_csv.read()
            parsed_fl = fld.decode("utf-8")
            posts_list = parsed_fl.split("\n")
            posts_list = [x for x in posts_list if x]
            posts_list = [x.replace("\n", "") for x in posts_list]
            posts_list = [x.replace("\r", "") for x in posts_list]
            print(posts_list)

            bulk_upload_csv(posts_list, self.instance.id)

        if commit:
            m.save()

        return m

        # print("%d Posts Added" % cnt)
