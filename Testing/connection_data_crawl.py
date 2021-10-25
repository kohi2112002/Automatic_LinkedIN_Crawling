from scrape_linkedin import ConnectionScraper

li_at = 'AQEDATUwISoEXezQAAABfLU_uQEAAAF82Uw9AVYAyHz-D67dKIndQiuKR4a319jms0no7G_xecrjpP3E3H-u8G6k5zz5_7jsUWe4Y-fny90c9nE03X0ytdap33u2o4lmYA6IE_W7JfgaG2IPeseJIleD'
with ConnectionScraper(cookie=li_at) as scraper:
    profile = scraper.scrape(url = 'https://www.linkedin.com/in/khoi-do-3a2a1820a/')
print(profile)