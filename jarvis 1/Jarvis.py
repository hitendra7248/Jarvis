
from brain.aibrain import ReplyBrain
from brain.Qna import QuestionAnswer
from Body.ListenHindi import MicExecution
print(">> Starting The Alis :  Wait For Some Seconds.")
from Body.SpeakHindi import Speak
from Features.Clap import Tester
print(">> Starting The Alis :  Wait For Few Seconds More")



def MainExecution():

    Speak("Hello Sir")
    Speak("I Am Alis , I am Ready to Assist You Sir")

    while True:

        Data = MicExecution()
        Data = str(Data)

        if len(Data)<3:
            pass

        elif "what is my little sister's name" in Data:
            Speak("your little sister name is pooja")
        
        elif "brake"in Data:
            Speak("Ok Sir , You Call Me Anytime !")
            break

        elif "what is" in Data or  "where is" in Data or "question" in Data or "answer " in Data :
            Reply = QuestionAnswer (Data)

        else:   
            Reply = ReplyBrain(Data)
            Speak(Reply)

def ClapDetect():

    query = Tester()
    if "True-Mic" in query:
        print("")
        print(">> Alis Ready!!  >>")
        print("")
        MainExecution()
    else:
        pass    

ClapDetect()



