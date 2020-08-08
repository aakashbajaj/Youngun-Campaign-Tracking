from youngun.apps.content.models import InstagramPost, TwitterPost, FacebookPost


def extract_username_from_posts():
    for post in InstagramPost.objects.all():
        if post.embed_code.startswith("<blockquote"):
            start_idx = post.embed_code.index("(@")
            if start_idx > 0:
                end_idx = post.embed_code[start_idx:].index(")")
                post.post_username = post.embed_code[start_idx +
                                                     2:end_idx+start_idx]

                post.save()
