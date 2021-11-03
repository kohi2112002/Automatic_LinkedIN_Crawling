from scrape_linkedin import ProfileScraper, MyConnectionScraper

li_at = 'AQEDATUwISoEXH7JAAABfL-xKrsAAAF9CLUWyk0Azl2sm0E5aqF3gXdUjx6TXc8TUd-rRAu-WF7sI3dXVNn0K6M5yawloOm1xNNNGgm54MSG6o0UYaWLlE2-heihRqwWgVa4lM5XAWPqFdjYLbcxNqO0'


def get_one_info(_user):
    with ProfileScraper(cookie=li_at) as scraper:
        profile = scraper.scrape(user=_user)
        return profile.to_dict()

def get_multiple_info(_user_list):
    dict_lst = []
    for x in _user_list:
        dict_lst.append(get_one_info(x))
    return dict_lst

def get_my_connection():
    with MyConnectionScraper(cookie=li_at) as scrapper:
        _lst = scrapper.scrape()
    return _lst
