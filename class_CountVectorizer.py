class CountVectorizer():
        def __init__(self, lowercase=True):
            self.lowercase = lowercase
            #self._vocabulary = corpus
        
        def get_feature_names(self, corpus):
            all_words = []
            for words in corpus:
                words = words.lower().split() 
                for word in words:
                    if (word in all_words) is False:
                        all_words.append(word)
            return all_words
        
        def fit_transform(self, corpus):
            all_words = []
            for words in corpus:
                words = words.lower().split() 
                for word in words:
                    if (word in all_words) is False:
                        all_words.append(word)
            count_words = []
            for i in range(len(corpus)):   
                a = []
                for word in all_words:
                    count_word = corpus[i].lower().count(word)
                    a.append(count_word)
                count_words.append(a)
            return count_words
                
       