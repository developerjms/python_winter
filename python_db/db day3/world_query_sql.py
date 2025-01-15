# city insert sql
def insert_city_query():
    return """
INSERT INTO Country (code, Name, Continent, Region, SurfaceArea, Population, LocalName, GovernmentForm, Code2) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);

INSERT INTO City (Name, CountryCode, District, Population) VALUES (%s, %s, %s, %s);
    """
    
def insesrt_all_query():
        return """
INSERT INTO Country (code, Name, Continent, Region, SurfaceArea, Population, LocalName, GovernmentForm, Code2) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);

INSERT INTO City (Name, CountryCode, District, Population) VALUES (%s, %s, %s, %s);

INSERT INTO countrylanguage (countryCode, Language, IsOfficial, Percentage)
VALUES (%s, %s, %s, %s);
    """
    
def select_city_country_query():
    return """
SELECT *
FROM City c1
JOIN Country c2 ON c1.CountryCode = c2.Code
where c1.countrycode = %s;
    """
    
def select_country_languege():
        return """
SELECT *
FROM country c1, city c2, countrylanguage c3
WHERE c1.Code = c2.CountryCode
AND c1.Code = c3.CountryCode
AND c1.Name=%s
AND c2.CountryCode=%s;
    """
    
def select_population():
    return"""
    select * from city c1, country c2
    where (c2.Code = c1.CountryCode)
    and (c2.Population between %s and %s);
    """

def update_city_country_query():
    return """
    update city c1
    join country c2 ON c1.CountryCode = c2.Code
    SET c1.population=%s, c1.district=%s
    where c1.name=%s and c2.code=%s
    """
    
