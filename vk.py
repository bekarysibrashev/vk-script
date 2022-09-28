import vk_api

#Скрипт который автоматизирует отписки от всех групп в ВК
#Автоотписка от всех групп 

session = vk_api.VkApi(token='?') # Вместо ? ввести токен от вк
vk = session.get_api()

def get_groups(user_id):
    get = session.method("groups.get", {"user_id": user_id})
    # print(get["items"])
    return get["items"]    


group_list = get_groups(???) # Вместо ??? ввести ID своей страницы

for i in group_list:
    # print(i)
    session.method("groups.leave", {"group_id": i})
        

get_groups(???) # Вместо ??? ввести ID своей страницы