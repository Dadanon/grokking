**Using of hashtables**

- _Using hashtables for search_


    phone_book = {}
    
    phone_book['Jenny'] = 8960435
    
    phone_book['Urgency'] = 112
    
    print(phone_book['Jenny']) # 8960435

Also IP adresses in WEB

- _Elimination of duplicates_


    voted = {}
    
    def can_vote(person):

        if voted.get(person):
            print("Kick them out!")
        else:
            voted[person] = True
            print("Let them vote!")
        
- _Caching_

If web-page is not in cash -> do some server work

Else -> load cached page