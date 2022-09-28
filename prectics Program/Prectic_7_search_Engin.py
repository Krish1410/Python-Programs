from time import time

def mach(qurey,sentence):
    Words1=qurey.split(" ")
    Words2=sentence.split(" ")
    match_words=0
    for word1 in Words1:
        for word2 in Words2:
            if word1.lower()==word2.lower():
                match_words+=1
    return match_words

if __name__ == "__main__":
    sentences=["Python is Greate",
               "Krish is Greate",
               "Krish love Computer",
               "Krish Dose not know tamil",
               "Subscribe Teach India chanel in you tube",
               "How Are you",
               "What are you doing",
               "python is programing lang",
               "who are you?",
               "I am Learn coding frome Harry",
               "code with herry is best codin learing chanel",
               "youtube bigest pletform of vloging"
               ]
    init=time()
    qurey=input("Enter your qurey:")
    matchs=[mach(qurey,sentence) for sentence in sentences]
    sortedsentscore=[sentscore for sentscore in sorted(zip(matchs,sentences))]
    results=0
    Founds=[]
    for score, item in sortedsentscore:
        if score>0:
            results+=1
            Founds.append(item)
            # print(f"\n\"{item}\"")
    print(f"{results} Result Found\n")
    print("\""+"\"\n\"".join(Founds)+"\"")
    print(f"\nYour Result found in {time()-init}")