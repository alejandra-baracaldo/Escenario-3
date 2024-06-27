class count:
    def _init_(self,word):
        self.word=word

        def get_word():
            return self.word
        def set_word():
            self.word=word
    
    def total(self):
        self.word=input("escriba su palabra: ")
        dic={}
        for i in self.word:
            if not i in dic:
                dic[i]= 1 
            else: dic[i]= dic[i]+1
        print(dic)

word=str
fun=count()
fun.total()