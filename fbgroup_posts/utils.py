from django.conf import settings
import requests

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
    :param content: Likes or Comments (str)
    :return: total likes or comments count (int)
    """
    url = "https://graph.facebook.com/v2.8/{0}/{1}/?access_token={2}&summary=true".format(post_id, content, token)
    r = requests.get(url)
    likes_data = r.json()
    return likes_data['summary']['total_count']

