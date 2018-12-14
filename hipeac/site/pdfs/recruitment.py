from django.template.defaultfilters import date as date_filter

from hipeac.tools.pdf import PdfResponse, Pdf


class JobsPdfMaker:

    def __init__(self, *, jobs, filename: str, as_attachment: bool = False):
        self._response = PdfResponse(filename=filename, as_attachment=as_attachment)
        self.jobs = jobs
        self.make_pdf()

    def make_pdf(self):
        with Pdf() as pdf:
            for job in self.jobs:
                location = []
                if job.location:
                    location.append(job.location)
                if job.country:
                    location.append(job.country.name)

                pdf.add_note(f'Find more on our web: hipeac.net/jobs/{job.id}')
                if job.institution:
                    pdf.add_image(job.institution.images['th'], 'th')
                    pdf.add_text(f'<strong>{job.institution.name}</strong>', 'h4')
                pdf.add_text(', '.join(location), 'h4')
                pdf.add_spacer()
                pdf.add_text(job.title, 'h1')
                pdf.add_text(f'<strong>Deadline</strong>: {date_filter(job.deadline)}', 'ul_li')
                pdf.add_text(f'<strong>Career levels</strong>: {job.get_metadata_display("career_levels")}', 'ul_li')
                pdf.add_text(f'<strong>Keywords</strong>: {job.get_metadata_display("topics")}', 'ul_li')
                pdf.add_spacer()
                pdf.add_text(job.description, 'markdown')
                pdf.add_page_break()

            self._response.write(pdf.get())

    @property
    def response(self) -> PdfResponse:
        return self._response
