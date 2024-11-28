import scrapy

class JobzynSpider(scrapy.Spider):
    name = 'job'
    start_urls = ['https://www.jobzyn.com/fr/jobs']

    def parse(self, response):
        job_posts = response.css('a[href*="/fr/companies/"]')
        for job in job_posts:
            yield {
                'titre': job.css('h3::text').get().strip(),
                'employeur': job.css('p.text-muted-foreground::text').get().strip(),
                'categories': job.css('div.activities-tab div::text').getall(),
                'contrat': job.css('div.flex-row p::text').re_first(r'CDI|CDD|Stage|Freelance'),
                'teletravail': job.css('div.flex-row p::text').re(r'Télétravail :\s*(.+)'),
                'localisation': job.css('div.flex-row p::text').re_first(r'Casablanca|Rabat|Marrakech|.*'),
                'date_publication': job.css('p.absolute.bottom-4.right-6::text').get(default='').strip(),
                'lien': response.urljoin(job.attrib['href'])
            }

