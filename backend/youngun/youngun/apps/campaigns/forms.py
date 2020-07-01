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

        if not file_csv is None:

            fld = file_csv.read()
            print(file_csv.read().decode("utf-8"))
            parsed_fl = fld.decode("utf-8")
            posts_list = parsed_fl.split("\n")
            posts_list = [x for x in posts_list if x]
            print(posts_list)

            for post in posts_list:
                print(post)
                p_obj, created = Post.objects.get_or_create(
                    campaign=self.instance, url=post)

                p_obj.platform = "in"

                # p_obj.campaign = self
                # p_obj.save()

            if commit:
                m.save()

            return m
