# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class TutorialItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass
class JobItem(scrapy.Item):
    # Définir les champs de l'item
    job_title = scrapy.Field()  # Titre du job
    company_name = scrapy.Field()  # Nom de l'entreprise
    job_description = scrapy.Field()  # Description du job
    location = scrapy.Field()  # Localisation
    contract_type = scrapy.Field()  # Type de contrat (CDI, CDD, etc.)
    education_level = scrapy.Field()  # Niveau d'études requis
    experience_level = scrapy.Field()  # Niveau d'expérience requis
    skills = scrapy.Field()  # Compétences clés
    posting_date = scrapy.Field()  # Date de publication de l'annonce
    job_url = scrapy.Field()  # URL de l'offre
    company_url = scrapy.Field()  # URL de la page de l'entreprise
    company_logo = scrapy.Field() 
