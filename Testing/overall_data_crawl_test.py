from scrape_linkedin import ProfileScraper

li_at = 'AQEDATOpMusDmh7gAAABfLW1lEMAAAF82cIYQ1YAdiUg4Hp1zC5AfhzU1WKilPKabdYM4466RPkvQmBFlHv4M-m2sgV8VfAXL8C-_onkR7fKg-O2AOkH08Eas6TDv8OdYD_W4Rt5WXvhodeqjbtpLkjK'
with ProfileScraper(cookie=li_at) as scraper:
    profile = scraper.scrape(user='khoi-do-3a2a1820a')
print(profile.to_dict()['skills'])