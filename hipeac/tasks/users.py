from celery.decorators import periodic_task
from celery.schedules import crontab

from hipeac.tools.notifications.events import RegistrationPendingNotificator
from hipeac.tools.notifications.users import ResearchTopicsPendingNotificator


@periodic_task(run_every=crontab(minute='*/5'))
def process_user_notifications():
    RegistrationPendingNotificator().process_data()
    ResearchTopicsPendingNotificator().process_data()