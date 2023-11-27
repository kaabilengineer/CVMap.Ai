
import numpy as np
import nltk as nlp

class SubjectiveTest:

    def __init__(self, data, noOfQues):

        self.question_pattern = [
            "Explain in detail ",
            "Explain in short ",
            "Ellaborate ",
            "What do you mean by ",
            "Explain with Example what is ",
            "Explain with real life example what is "
        ]

        self.grammar = r"""
            CHUNK: {<NN>+<IN|DT>*<NN>+}
            {<NN>+<IN|DT>*<NNP>+}
            {<NNP>+<NNS>*}
        """
        self.summary = data
        self.noOfQues = noOfQues

    
    @staticmethod
    def word_tokenizer(sequence):
        word_tokens = list()
        for sent in nlp.sent_tokenize(sequence):
            for w in nlp.word_tokenize(sent):
                word_tokens.append(w)
        return word_tokens

    def generate_questions(self):
        sentences = nlp.sent_tokenize(self.summary)
        cp = nlp.RegexpParser(self.grammar)
        question_list = []

        for sentence in sentences:
            tagged_words = nlp.pos_tag(nlp.word_tokenize(sentence))
            tree = cp.parse(tagged_words)
            for subtree in tree.subtrees():
                if subtree.label() == "CHUNK":
                    temp = ""
                    for sub in subtree:
                        temp += sub[0]
                        temp += " "
                    temp = temp.strip()
                    temp = temp.upper()
                    rand_num = np.random.randint(0, len(self.question_pattern))
                    question = self.question_pattern[rand_num] + temp + "?"
                    question_list.append(question)

        return question_list[:self.noOfQues]
