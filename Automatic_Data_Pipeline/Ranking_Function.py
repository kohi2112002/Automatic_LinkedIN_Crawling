
def Ranking_by_MEAN(_skills_dict_):
    endorse_lst = [int(x.replace('+','')) for x in _skills_dict_['endorsement']]
    return sum(endorse_lst) / len(endorse_lst)

def Extract_Endorsement_Full_Report(_dataframe = None, path = None):
    if _dataframe:
        lst = [int(x.replace('+','')) for x in _dataframe['endorsement'].tolist()]
        return sum(lst) / len(lst)
    if path:
        import pandas as pd
        _df = pd.read_csv(path)
        lst = [int(x.replace('+','')) for x in _df['endorsement'].tolist()]
        return sum(lst) / len(lst)

def Ranking_by_Wetight_Rating(_skills_dict_, minimum_vote = 2):
    m = minimum_vote
    v = len(_skills_dict_['endorsement'])
    R = Ranking_by_MEAN(_skills_dict_)
    C = Extract_Endorsement_Full_Report(path = './Output_CSV/personal_skills.csv')
    f1 = (v/(v+m))*R
    f2 = (m/(m+v))*C
    return f1 + f2


# testing 
ex_name = 'mikahdang'
import Crawling, DataExtract
my_info = Crawling.get_one_info(ex_name)
print(Ranking_by_Wetight_Rating(DataExtract.extract_personal_skill([my_info])))




