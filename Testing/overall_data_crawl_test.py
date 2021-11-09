from scrape_linkedin import ProfileScraper

li_at = 'AQEDATUwISoEXH7JAAABfL-xKrsAAAF9CLUWyk0Azl2sm0E5aqF3gXdUjx6TXc8TUd-rRAu-WF7sI3dXVNn0K6M5yawloOm1xNNNGgm54MSG6o0UYaWLlE2-heihRqwWgVa4lM5XAWPqFdjYLbcxNqO0'
with ProfileScraper(cookie=li_at) as scraper:
    profile = scraper.scrape(user='khoi-do-3a2a1820a')
print(profile.to_dict()['experiences'])