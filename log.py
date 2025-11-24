import os
import shutil
import subprocess
import statistics
import pandas as pd

def Average(Mylist): 
    return sum(Mylist) / len(Mylist)

def Median(Mylist): 
    return statistics.median(Mylist)

#methods that we added logging to 
#deleteRepo mining.py
def deleteRepo(dirName, type_):
    print(':::' + type_ + ':::Deleting ', dirName)
    try:
        if os.path.exists(dirName):
            shutil.rmtree(dirName)
          #log-structure change-repo deleted
    except OSError:
        print('Failed deleting, will try manually')


#cloneRepo mining.py
def cloneRepo(repo_name, target_dir):
    cmd_ = "git clone " + repo_name + " " + target_dir 
    try:
       subprocess.check_output(['bash','-c', cmd_]) 
      #log-structure change-repo cloned
    except subprocess.CalledProcessError:
       print('Skipping this repo ... trouble cloning repo:', repo_name)

#getDevEmailForCommit mining.py
def getDevEmailForCommit(repo_path_param, hash_):
    author_emails = []

    cdCommand         = "cd " + repo_path_param + " ; "
    commitCountCmd    = " git log --format='%ae'" + hash_ + "^!"
    command2Run = cdCommand + commitCountCmd

    author_emails = str(subprocess.check_output(['bash','-c', command2Run]))
    author_emails = author_emails.split('\n')
    # print(type(author_emails)) 
    author_emails = [x_.replace(hash_, '') for x_ in author_emails if x_ != '\n' and '@' in x_ ] 
    author_emails = [x_.replace('^', '') for x_ in author_emails if x_ != '\n' and '@' in x_ ] 
    author_emails = [x_.replace('!', '') for x_ in author_emails if x_ != '\n' and '@' in x_ ] 
    author_emails = [x_.replace('\\n', ',') for x_ in author_emails if x_ != '\n' and '@' in x_ ] 
    try:
        author_emails = author_emails[0].split(',')
        author_emails = [x_ for x_ in author_emails if len(x_) > 3 ] 
        # print(author_emails) 
        author_emails = list(np.unique(author_emails) )
    except IndexError as e_:
        #log-failed to split author emails
        pass
    return author_emails  

#reportProp report.py
def reportProp( res_file ):
    res_df = pd.read_csv(res_file) 
    # log-external security risk reading from an external file
    fields2explore = ['DATA_LOAD_COUNT', 'MODEL_LOAD_COUNT', 'DATA_DOWNLOAD_COUNT',	'MODEL_LABEL_COUNT', 'MODEL_OUTPUT_COUNT',	
                      'DATA_PIPELINE_COUNT', 'ENVIRONMENT_COUNT', 'STATE_OBSERVE_COUNT',  'TOTAL_EVENT_COUNT'
                     ]
                     
    for field in fields2explore:
        field_res_list = res_df[res_df['CATEGORY'] == field ]   
        prop_val_list = field_res_list['PROP_VAL'].tolist() 
        print(prop_val_list)
        average_prop_metric = Average(prop_val_list)        
        print('CATEGORY:{}, AVG_PROP_VAL:{}'.format( field, average_prop_metric  ))
        print('-'*50)     
        median_prop_metric = Median(prop_val_list)        
        print('CATEGORY:{}, MEDIAN_PROP_VAL:{}'.format( field, median_prop_metric  ))
        print('-'*50)          

#reportDensity report.py
def reportDensity( res_file ):
    res_df = pd.read_csv(res_file) 
    # log-external security risk reading from an external file
    fields2explore = ['DATA_LOAD_COUNT', 'MODEL_LOAD_COUNT', 'DATA_DOWNLOAD_COUNT',	'MODEL_LABEL_COUNT', 'MODEL_OUTPUT_COUNT',	
                      'DATA_PIPELINE_COUNT', 'ENVIRONMENT_COUNT', 'STATE_OBSERVE_COUNT',  'TOTAL_EVENT_COUNT'
                     ]
                     
    for field in fields2explore:
        field_res_list = res_df[res_df['CATEGORY'] == field ]   
        density_val_list = field_res_list['EVENT_DENSITY'].tolist() 
        average_density_metric = Average(density_val_list)        
        print('CATEGORY:{}, AVG_PROP_VAL:{}'.format( field, average_density_metric  ))
        print('-'*50)     
        median_density_metric = Median(density_val_list)        
        print('CATEGORY:{}, MEDIAN_PROP_VAL:{}'.format( field, median_density_metric  ))
        print('-'*50) 



if __name__=='__main__':
    print('logging')