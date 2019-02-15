from anymail.message import AnymailMessage
from django.template.loader import render_to_string
from typing import List


JOBS_DIGEST_EMAIL = 'HiPEAC Jobs <jobs@hipeac.net>'
RECRUITMENT_EMAIL = 'HiPEAC Recruitment <recruitment@hipeac.net>'
TEMPLATE_PATHS = {
    'events.registrations.created': '_emails/events/registrations_created.md.html',
    'events.registrations.payment_reminder': '_emails/events/registrations_payment_reminder.md.html',
    'events.registrations.reminder': '_emails/events/registrations_reminder.md.html',
    'events.sessions.reminder': '_emails/events/sessions_reminder.md.html',
    'recruitment.jobs.digest': '_emails/recruitment/jobs_digest.md.html',
    'recruitment.jobs.created': '_emails/recruitment/jobs_created.md.html',
    'recruitment.jobs.evaluation': '_emails/recruitment/jobs_evaluation.md.html',
    'recruitment.jobs.expiration_reminder': '_emails/recruitment/jobs_expiration_reminder.md.html',
    'users.members.non_eu.welcome': '_emails/users/members_non_eu_welcome.md.html',
    'users.members.welcome': '_emails/users/members_welcome.md.html',
    'users.profile.update_reminder': '_emails/users/profile_update_reminder.md.html',
}


class TemplateEmail:

    def __init__(self, *, template: str, subject: str, from_email: str, to: List[str], context_data: dict = {}) -> None:
        if template not in TEMPLATE_PATHS:
            raise ValueError(f'"{template}" is not registered.')

        template_path = TEMPLATE_PATHS[template]
        text_content = render_to_string(template_path, {**{'email_format': 'txt'}, **context_data})
        html_content = render_to_string(template_path, {**{'email_format': 'html'}, **context_data})

        if template.startswith('recruitment.'):
            to.append(RECRUITMENT_EMAIL)

        self.message = AnymailMessage(subject=subject, from_email=from_email, to=to, body=text_content)
        self.message.attach_alternative(html_content, 'text/html')

    def send(self):
        self.message.send()
