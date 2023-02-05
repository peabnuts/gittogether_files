import requests


# Expects a string username
def get_user_languages(username):
    
    url = 'https://api.github.com/users/' + username + '/repos'
    payload = {'full_name': ''}
    
    # get the user's json data
    response = requests.get(url, data=payload)
    repos = response.json()
    
    # extract languages
    
    user_languages = set()
    user_lan = []
    occ = []

    
    for i in range(len(repos)):
        j = repos[i]['language']
       
        if j not in user_lan and j:
            user_lan.insert(i, j)
            occ.insert(i, 1)
            
        elif j:
            user_languages.add(j)
            ind = user_lan.index(j)
            occ[ind] = occ[ind] + 1
    
    occ_sorted = sorted(range(len(occ)),key=lambda user_lan:occ[user_lan],reverse=True)
    langs_sorted = [user_lan[i] for i in occ_sorted ]


    lang_str = ', '.join(langs_sorted)
    return lang_str


