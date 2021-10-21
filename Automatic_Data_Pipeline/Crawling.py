from scrape_linkedin import ProfileScraper, MyConnectionScraper

li_at = 'AQEDATUwISoEpRnlAAABfIjZkOYAAAF8rOYU5k0AL0tyVGAWEkES0MJg62GfAl3vyFrRbr2UK6AgXuZfIcItubuHu43ukZm2_PfZvhCJ7BeaBVRAb3_eYn7Amj_Zp3RgA5vuNmyleF-F_ljX97J9PO1u'


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
