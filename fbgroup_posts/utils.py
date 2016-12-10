from django.conf import settings
import requests
from .models import Post

# Facebook API
access_token = settings.FB_APP_ID + '|' + settings.FB_APP_SECRET
post_limit = settings.FB_POST_LIMIT


def get_fb_group_feed_url(group_id, token, limit):
    """
    Get Group Feed URL
    :param group_id: FB Group Id (str)
    :param token: Access Token (str)
    :param limit: Post Limit (int)
    :return: URL (str)
    """
    fields = ['message', 'permalink_url', 'id', 'from', 'created_time']
    return "https://graph.facebook.com/v2.8/{0}/feed/?fields={1}&access_token={2}&limit={3}".format(
        group_id, ','.join(fields), token, limit)


def get_fb_total_count(post_id, token, content):
    """
    Get likes or comments counts
    :param post_id: FB Post Id (str)
    :param token: Access Token (str)
    :param content: likes or comments (str)
    :return: total likes or comments count (int)
    """
    url = "https://graph.facebook.com/v2.8/{0}/{1}/?access_token={2}&summary=true".format(post_id, content, token)
    r = requests.get(url)
    likes_data = r.json()
    return likes_data['summary']['total_count']


def save_fb_post_data():
    url = get_fb_group_feed_url(settings.FB_GROUP_ID, access_token, post_limit)
    r = requests.get(url)
    group_posts = r.json()
    for post in group_posts['data']:
        like_count = get_fb_total_count(post['id'], access_token, 'likes')
        comment_count = get_fb_total_count(post['id'], access_token, 'comments')
        message = post['message'] if 'message' in post else 'Shared Post'

        if not Post.objects.filter(post_id=post['id']).exists():
            post_data = Post(
                post_id=post['id'],
                created_time=post['created_time'],
                from_name=post['from']['name'],
                permalink=post['permalink_url'],
                message=message,
                likes=like_count,
                comments=comment_count
            )

            post_data.save()
        else:
            post_update = Post.objects.get(post_id=post['id'])
            post_update.likes = like_count
            post_update.comments = comment_count
            post_update.save()

