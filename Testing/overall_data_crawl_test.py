from scrape_linkedin import ProfileScraper

li_at = 'AQEDATUwISoEpRnlAAABfIjZkOYAAAF8rOYU5k0AL0tyVGAWEkES0MJg62GfAl3vyFrRbr2UK6AgXuZfIcItubuHu43ukZm2_PfZvhCJ7BeaBVRAb3_eYn7Amj_Zp3RgA5vuNmyleF-F_ljX97J9PO1u'
with ProfileScraper(cookie=li_at) as scraper:
    profile = scraper.scrape(user='khoi-do-3a2a1820a')
print(profile.to_dict()['interests'])