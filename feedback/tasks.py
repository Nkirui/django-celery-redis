from celery.decorators import task
from celery.utils.log import get_task_logger

from feedback.emails import send_feedback_email
from feedback.emails import download_mp3
logger = get_task_logger(__name__)


@task(name="send_feedback_email_task")
def send_feedback_email_task(email, link):
    """sends an email when feedback form is filled successfully"""
    logger.info("Sent feedback email")
    return send_feedback_email(email, link)

@task(name="download_mp3_task")
def download_mp3_task(link):
    """download mp3  when feedback form is filled successfully"""
    logger.info("Mp3 is going to download")
    return download_mp3(link)