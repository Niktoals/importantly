from sdamgia import SdamGIA
from termcolor import *


class GIA():
    def __init__(self, subject, request):
        self.subject=subject
        self.request=request
        self.gia=SdamGIA()

    def search_by_task(self):
        ls=self.gia.search(subject, request)
        if len(ls)!=0:
            dict_of_answers=dict().fromkeys(ls)
            for i in ls:
                reply=self.gia.get_problem_by_id(subject, i)
                dict_of_answers[i]=reply["answer"]
                print(colored("ID: ", color="green"), reply['id'])
                print(colored("Содержание:", color="green"), reply["condition"]["text"].replace("\xad", ""))
                print(colored('------------------------------------------------------------------------', color="light_cyan")) 
            id_task=input(colored("Чтобы получить ответ, посмотри содержание задания и выбери подходящее написав его ID: ", color="light_cyan"))
            ans=dict_of_answers[id_task]
            print(colored(f"Ответ: {ans}", color="green", attrs=["bold"]))
            print(colored('------------------------------------------------------------------------', color="light_cyan")) 
        else:
            print(colored("Таких задач не найдено", color="red"))
            return 0
     
    def search_by_test(self):
        ls=self.gia.get_test_by_id(subject, request)
        if len(ls)!=0:
            s=" ".join(ls)
            print(colored(s, color="light_cyan"))
            nums=input(colored("Введи ID теста/ов\nНапример так:'1111' .... .....\nИли напиши так 'all' чтобы получить ответы на все задания в тесте\n", color="light_cyan"))
            if nums=="all":
                nums=ls
            else:
                nums=nums.split(' ')
            for i in nums:
                reply=self.gia.get_problem_by_id(subject, i)
                ans=reply["answer"]
                print(colored("ID: ", color="green"), reply['id'])
                print(colored("Содержание:", color="green"), reply["condition"]["text"].replace("\xad", ""))
                print(colored(f"Ответ: {ans}", color="green", attrs=["bold"]))
                print(colored('------------------------------------------------------------------------', color="light_cyan")) 
        else:
            print(colored("Такого варианта не найдено", color="red"))
            return 0

if __name__=="__main__":
    print(colored("*********GIA PARSER********", color='light_cyan', attrs=['bold']))
    while True:
        mode=input(colored("Выбери мод: Поиск по ID теста(test) или поиск по содержание задания(task)\n", color="light_cyan"))
        subject = input(colored("Введи предмет: ", color="light_cyan"))
        request = input(colored("Введи ID теста или содержание задачи: ", color="light_cyan"))
        print(colored('------------------------------------------------------------------------', color="light_cyan")) 
        parser=GIA(subject, request)
        try:
            match mode:
                case "test":
                    parser.search_by_test()
                case "task":
                    parser.search_by_task()
        except:
            print(colored("Что-то пошло не так", color="red"))



    