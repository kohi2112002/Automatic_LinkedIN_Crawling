from scrape_linkedin import ProfileScraper, MyConnectionScraper

li_at = 'AQEDATUwISoEXezQAAABfLU_uQEAAAF82Uw9AVYAyHz-D67dKIndQiuKR4a319jms0no7G_xecrjpP3E3H-u8G6k5zz5_7jsUWe4Y-fny90c9nE03X0ytdap33u2o4lmYA6IE_W7JfgaG2IPeseJIleD'


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
