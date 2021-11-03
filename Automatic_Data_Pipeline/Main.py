import DataExtract
import Crawling
import pandas as pd
# ex_name = 'khoi-do-3a2a1820a'

# Get all connections
my_conn = Crawling.get_my_connection()

# Extract to name and id dictionary
personal_connection_dict = DataExtract.extract_personal_connection(my_conn)

# Get id list 
id_list = DataExtract.extract_personal_id(personal_connection_dict)

# Get profile of all connection
all_conn_profile = Crawling.get_multiple_info(id_list)

# Extract personal information
per_info_dict = DataExtract.extract_personal_info(all_conn_profile)

# Convert personal information to DF to CSV
per_info_df = pd.DataFrame(per_info_dict)
per_info_df.to_csv('./Output_CSV/personal_info.csv')

# Extract personal skill
per_skill_dict = DataExtract.extract_personal_skill(all_conn_profile)

# Convert personal skill to DF to CSV
per_skill_df = pd.DataFrame(per_skill_dict)
per_skill_df.to_csv('./Output_CSV/personal_skills.csv')

# Extract personal job
per_job_dict = DataExtract.extract_personal_job(all_conn_profile)

# Convert personal job to DF to CSV
per_job_df = pd.DataFrame(per_job_dict)
per_job_df.to_csv('./Output_CSV/personal_jobs.csv')

# Extract personal edu
per_edu_dict = DataExtract.extract_personal_edu(all_conn_profile)

# Convert personal job to DF to CSV
per_edu_df = pd.DataFrame(per_edu_dict)
per_edu_df.to_csv('./Output_CSV/personal_edus.csv')

# Extract personal edu
per_interest_dict = DataExtract.extract_personal_interests(all_conn_profile)

# Convert personal job to DF to CSV
per_interest_df = pd.DataFrame(per_interest_dict)
per_interest_df.to_csv('./Output_CSV/personal_interests.csv')


