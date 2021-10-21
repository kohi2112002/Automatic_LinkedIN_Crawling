from scrape_linkedin import ConnectionScraper

li_at = 'AQEDATUwISoEpRnlAAABfIjZkOYAAAF8rOYU5k0AL0tyVGAWEkES0MJg62GfAl3vyFrRbr2UK6AgXuZfIcItubuHu43ukZm2_PfZvhCJ7BeaBVRAb3_eYn7Amj_Zp3RgA5vuNmyleF-F_ljX97J9PO1u'
with ConnectionScraper(cookie=li_at) as scraper:
    profile = scraper.scrape(user='hieu-mai-unsw')
print(profile)