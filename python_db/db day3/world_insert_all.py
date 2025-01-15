def collect_country_data():
    # code = input("Enter country code: ")
    # name = input("Enter country name: ")
    # continent = input("Enter country continent: ")
    # region = input("Enter country region: ")
    # surface_area = int(input("Enter country surfacearea: "))
    # population = int(input("Enter country population: "))
    # local_name = input("Enter country localname: ")
    # government_form = input("Enter country governmentform: ")
    # code2 = input("Enter country code2: ")
    # return (code, name, continent, region, surface_area, population, local_name, government_form, code2)
    code = 'MSJ'
    name = 'Moon State'
    continent = 'Oceania'
    region = 'Moon Region'
    surface_area = 1000000
    population = 99999
    local_name = 'Moon'
    government_form = 'Federal Republic'
    code2 = 'MS'
    return (code, name, continent, region, surface_area, population, local_name, government_form, code2)

def collect_city_data():
    # name = input("Enter country code: ")
    # country_code = input("Enter country code: ")
    # district = input("Enter country code: ")
    # population = int(input("Enter country code: "))
    # return (name, country_code, district, population)
    
    name = 'Moon'
    country_code = 'MSJ'
    district = 'MSJ City'
    population = 99999
    return (name, country_code, district, population)

def collect_country_language_data():
    # countryCode = input("Enter countryCode: ")
    # Language = input("Enter Language: ")
    # IsOfficial = input("Enter IsOfficial: ")
    # Percentage = float(input("Enter Percentage: "))
    # return (country_code, language, is_official, percentage)
    
    country_code = 'MSJ'
    language = 'Hangul'
    is_official = 'T'
    percentage = 12.7
    return (country_code, language, is_official, percentage)

def collect_country_languege_date():
    city_name = 'South Korea'   # input('city name:')
    country_code = 'KOR'        # input('country name:')
    return (city_name, country_code)