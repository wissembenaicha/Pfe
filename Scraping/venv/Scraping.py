from selenium import webdriver
#open the Chrom browser and navigate the web page
def Scrap_Page(url_base):
    driver = webdriver.Chrome()
    driver.get(url_base)
    Ingredients =driver.find_elements_by_xpath('//li[@class="recipe-ingredients__list__item"]')
    Etaps = driver.find_elements_by_xpath('//li[@class="recipe-preparation__list__item"]')
    ustensiles= driver.find_elements_by_xpath('//li[@class="recipe-utensils__list__item"]')
    Type=driver.find_elements_by_xpath('//li[@class="mrtn-tag"]')
    temps=driver.find_elements_by_xpath('//span[@class="title-2 recipe-infos__total-time__value"]')
    nombre_personne=driver.find_elements_by_xpath('//span[@class="title-2 recipe-infos__quantity__value"]')
    print(Ingredients)
    num_ingredient = len(Ingredients)
    ListIngr=[]
    for i in range(num_ingredient):
        ListIngr.append(Ingredients[i].text)
    print(ListIngr)
    num_Etaps=len(Etaps)
    listEtap=[]
    for i in range(num_Etaps):
        listEtap.append(Etaps[i].text)
    print(listEtap)
    num_Ustensibles=len(ustensiles)
    listUstensible=[]
    for i in range(num_Ustensibles):
        listUstensible.append(ustensiles[i].text)
    print(listUstensible)
    num_Type=len(Type)
    listType=[]
    for i in range(num_Type):
        listType.append(Type[i].text)
    print(listType)
    Temps=temps[0].text
    print(Temps)
    nombre_Personne=nombre_personne[0].text
    print(f"{nombre_Personne}")