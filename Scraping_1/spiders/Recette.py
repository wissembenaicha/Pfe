# -*- coding: utf-8 -*-
import scrapy
import re

class RecetteSpider(scrapy.Spider):
    
    name = 'Recette'
    allowed_domains = ['www.marmiton.org']
    start_urls = ['https://www.marmiton.org/recettes/?type=boisson']

    def parse(self, response):
         Lien_Image = response.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "recipe-card__picture", " " ))]//img/@src').get()
         recette=response.xpath('//a[@class="recipe-card-link"]')
         for rec in recette:
             Link=rec.xpath('.//@href').get()
             yield scrapy.Request(url=Link , callback=self.parse_recette)

         next_page = response.xpath('//li[@class="next-page"]/a/@href').get()
         next_p = str('https://www.marmiton.org')+str(next_page)
        # #  ['https://www.marmiton.org']+next_page
         
         if next_page :
            yield scrapy.Request(url=next_p,callback=self.parse)
    def parse_recette(self,response):
        nom_Recette = response.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "main-title", " " ))]/text()').get()
        Nom_Ingrediant = response.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "ingredient", " " ))]/text()').getall()
        Quantite = response.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "recipe-ingredient-qt", " " ))]/text()').getall()
        # Etaps = response.css('normalize-space(//*[contains(concat( " ", @class, " " ), concat( " ", "recipe-preparation__list__item", " " ))] | //*[contains(concat( " ", @class, " " ), concat( " ", "af_al", " " ))]//li/text)').getall()
        Etaps = response.css('.recipe-preparation__list__item').getall()
        Ustensible = response.xpath('normalize-space(//*[contains(concat( " ", @class, " " ), concat( " ", "recipe-utensil__name", " " ))]/text())').getall()
        Type=response.xpath('normalize-space(//*[(@id = "sticky-desktop-only")]//*[contains(concat( " ", @class, " " ), concat( " ", "mrtn-tag", " " ))]/text())').getall()
        
        
        
        Temps = response.xpath('//span[@class="title-2 recipe-infos__total-time__value"]/text()').get()
        Nombre_de_personne = response.xpath('//span[@class="title-2 recipe-infos__quantity__value"]/text()').get()
        LF3=[]
        for i in range(len(Quantite)) :
            LF3.append(Quantite[i]+' '+Nom_Ingrediant[i])
        LF=[]
        for i in range(len(Etaps)):
            S=Etaps[i]
            S=S.replace('<li class=\"recipe-preparation__list__item\">\n\t\t\t','')
            S=S.replace('</a>','')
            S=S.replace('</span>','')
            S=S.replace('<br>\n','')
            S=S.replace('\t\t</li>','')
            S=re.sub('<a[^<]*>','',S)
            S=re.sub('<span[^<]*>','',S)
            
            LF.append(S)
        

        
        
      
        

        yield{
            'Nom de recette ' : nom_Recette,
            'Ingredients' : LF3,
            'Etaps' : LF,
            'Ustensibles' : Ustensible,
            'Types' : Type,
            'Temps' : Temps,
            'Nombre de personne' : Nombre_de_personne
        }

             


