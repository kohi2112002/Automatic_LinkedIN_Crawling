_keys = ['name', 'headline', 'company', 'school', 'summary', 'location', 'followers',
'email', 'phone', 'connected', ]

def personalINDO_Dict_initialize():
    info = {"name": [],"company": [], "school": [], "headline": [], 'location': [],
    "followers": [], "summary": [], "email": [], "phone": [], "connected":[]}
    return info

def myConnect_Dict_initialize():
    info = {'name' : [], 'id' : []}
    return info

def skill_Dict_initialize():
    info = {'name' : [], "skills" : [], "endorsement" : []}
    return info

def job_Dict_initialize():
    info = {'name' : [], 'job name' : [], 'time range' : []}
    return info

def Edu_Dict_inintialize():
    info = {'name' : [], 'edu name' : [], 'degree' : [], 'field study' : [], 'time range' : [], 'grade' : []}
    return info

def Interest_Dict_initialize():
    info = {'name' : [], 'interests' : []}
    return info

def extract_personal_info(info_dict_lst):
    info = personalINDO_Dict_initialize()
    for x in info_dict_lst:
        personal_info = x['personal_info']
        for i in _keys:
            if i in personal_info:
                info[i].append(personal_info[i])
            else:
                info[i].append("Missing")
    return info      

def extract_personal_connection(connect_dict_lst):
    _dict = myConnect_Dict_initialize()
    for x in connect_dict_lst:
        _dict['name'].append(x['name'])
        _dict['id'].append(x['id'])
    return _dict

def extract_personal_id(name_id_dict):
    return name_id_dict['id']

def extract_personal_skill(info_dict_lst):
    info = skill_Dict_initialize()
    for x in info_dict_lst:
        personal_info = x['personal_info']
        personal_skill = x['skills']
        for i in personal_skill:
            info['name'].append(str(personal_info['name']))
            info['skills'].append(str(i['name']))
            info['endorsement'].append(str(i['endorsements']))
    return info      

def extract_personal_job(info_dict_lst):
    info = job_Dict_initialize()
    for x in info_dict_lst:
        job_lst = x['experiences']['jobs']
        name = x['personal_info']['name']
        for i in job_lst:
            info['name'].append(str(name))
            info['job name'].append(str(i['title']))
            info['time range'].append(str(i['date_range']))
        return info

def extract_personal_edu(info_dict_lst):
    info = Edu_Dict_inintialize()
    for x in info_dict_lst:
        edu_lst = x['experiences']['education']
        name = x['personal_info']['name']        
        for i in edu_lst:
            info['name'].append(str(name))
            info['edu name'].append(str(i['name']))
            info['degree'].append(str(i['degree']))
            info['field study'].append(str(i['field_of_study']))
            info['time range'].append(str(i['date_range']))
            info['grade'].append(str(i['grades']))            
    return info

def extract_personal_interests(info_dict_lst):
    info = Interest_Dict_initialize()
    for x in info_dict_lst:
        name = x['personal_info']['name']
        interest_lst = x['interests']
        info['name'].append(name)
        info['interests'].append(' '.join(interest_lst))
    return info
