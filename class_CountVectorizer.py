class CountVectorizer():
        def __init__(self):
            self.feauters = []
            
        def get_feature_names(self):
            return self.feauters
        
        def fit_transform(self, corpus):
            for words in corpus:
                words = words.lower().split() 
                for word in words:
                    if (word in self.feauters) is False:
                        self.feauters.append(word)
            count_words = []
            for i in range(len(corpus)):   
                a = []
                for word in self.feauters:
                    count_word = corpus[i].lower().count(word)
                    a.append(count_word)
                count_words.append(a)
            return count_words
        

       
