from scrape_linkedin import scrape_in_parallel, CompanyScraper

companies = ['facebook', 'google', 'amazon', 'microsoft', ...]

li_at = 'AQEDATUwISoEXezQAAABfLU_uQEAAAF82Uw9AVYAyHz-D67dKIndQiuKR4a319jms0no7G_xecrjpP3E3H-u8G6k5zz5_7jsUWe4Y-fny90c9nE03X0ytdap33u2o4lmYA6IE_W7JfgaG2IPeseJIleD'

#Scrape all companies, output to 'companies.json' file, use 4 browser instances
scrape_in_parallel(
    scraper_type=CompanyScraper(cookie=li_at),
    items=companies,
    output_file="./Output_Testing/companies.json",
    num_instances=4
)