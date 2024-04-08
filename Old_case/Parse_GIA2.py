from sdamgia import SdamGIA
from termcolor import colored
from tqdm import tqdm
from time import sleep


class GIA():
    def __init__(self, mode, subject, request):
        self.subject=subject
        self.request=request
        self.mode=mode
        self.out=[]
        self.nums=str()
        self.gia=SdamGIA()
     
    def searching(self):
        self.out=[]
        for i in tqdm(self.nums, desc="Сбор данных", ncols=100):
            reply=self.gia.get_problem_by_id(subject, i)
            number=reply['id']
            topic=reply["condition"]["text"].replace("\xad", "")
            ans=reply["answer"]
            self.out.append((number, topic, ans))
            
    def output(self):
        try:
            match mode:
                case "test":
                    ls=self.gia.get_test_by_id(self.subject, self.request)
                    if len(ls)!=0:
                        s=" ".join(ls)
                        print(colored(s, color="light_cyan"))
                        check=input(colored("Введи ID теста/ов\nНапример так:'1111' .... .....\nИли напиши так 'all' чтобы получить ответы на все задания в тесте\n", color="light_cyan"))
                        if check=="all":
                            self.nums=s.split(' ')
                        else:
                            self.nums=check.split(' ')
                        self.searching()
                    else:
                        print(colored("Такого варианта не найдено", color="red"))
                case "task":
                    ls=self.gia.search(self.subject, self.request)
                    if len(ls)!=0:
                        s=" ".join(ls)
                        self.nums=s.split(" ")
                        self.searching()
                    else:
                        print(colored("Такого задания не найдено", color="red"))
            print(colored('------------------------------------------------------------------------', color="light_cyan")) 
            for number, topic, ans in self.out:
                print(colored("ID: ", color="green"), number)
                print(colored("Содержание:", color="green"), topic)
                print(colored(f"Ответ: {ans}", color="green", attrs=["bold"]))
                print(colored('------------------------------------------------------------------------', color="light_cyan")) 
                sleep(0.5)
        except:
            print(colored("Что-то пошло не так", color="red"))
                
if __name__=="__main__":
    print(colored("*********GIA PARSER********", color='light_cyan', attrs=['bold']))
    while True:
        mode=input(colored("Выбери мод: Поиск по ID теста(test) или поиск по содержание задания(task)\n", color="light_cyan"))
        subject = input(colored("Введи предмет: ", color="light_cyan"))
        request = input(colored("Введи ID теста или содержание задачи: ", color="light_cyan"))
        # print(colored('------------------------------------------------------------------------', color="light_cyan")) 
        parser=GIA(mode, subject, request)
        parser.output()
