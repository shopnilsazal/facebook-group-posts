from celery.utils.log import get_task_logger
from .utils import save_fb_post_data
from celery import shared_task


logger = get_task_logger(__name__)


@shared_task
def task_save_fb_group_posts():
    save_fb_post_data()
    logger.info("Saved posts from Facebook Group.")

