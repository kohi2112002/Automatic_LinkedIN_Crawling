from scrape_linkedin import CompanyScraper
import pandas as pd

# LIST YOUR COMPANIES HERE
my_company_list = ['facebook', 'linkedin']

company_data = []

with CompanyScraper() as scraper:
    # Get each company's overview, add to company_data list
    for name in my_company_list:
        overview = scraper.scrape(company=name).overview
        overview['company_name'] = name
        company_data.append(overview)

# Turn into dataframe for easy csv output
df = pd.DataFrame(company_data)
df.to_csv('D:/Automatic_LinkedIN_Crawling/Output_Testing/out.csv', index=False)