'''
Program: drGui.py
James Volino

Gui based version of the non-directive physcotherapy doctor program from chapter 5

'''

#Import statement
from breezypythongui import EasyFrame
import random

#Variables and Constants
hedges = ("Please tell me more.", "Many of my patients tell me the same thing.", "Please continue.")
qualifiers = ("Why do you say that ", "You seem to think that ","Can you explain why ", "I don't think ", "Maybe ")
replacements = {"I":"you", "me":"you", "my":"your", "we":"you", "mine":"yours", "am":"are"}

class DrGui(EasyFrame):
#Handles the interactio between the user and program (Dr.Gui)
    
    def __init__(self):
    #Sets up the windows and widgets
        EasyFrame.__init__(self, title = "Dr.Gui", background = "skyblue")
        self.addLabel(text = "Good day, hope you are feeling well today!", row = 0, column = 0, background = "skyblue")
        self.addLabel(text = "What can I do for you?", row = 1, column = 0, background = "skyblue", sticky = "NSEW")
        self.userText = self.addTextField(text = "", row = 2, column = 0, sticky = "NSEW")
        #Bind the text entry to click the enter key to submit
        self.userText.bind("<Return>", lambda event: self.reply())
        self.responseLabel = self.addLabel(text = "", row = 3, column = 0, background = "skyblue")
        self.addButton(text = "Submit", row = 4, column = 0, command = self.reply)
    
    def reply(self):
    #Executes the command of the button
        sentence = self.userText.getText()
        probability = random.randint(1,4)
        if probability == 1:
            self.responseLabel["text"] = random.choice(hedges)
        else:
            self.responseLabel["text"] = random.choice(qualifiers) + changePerson(sentence)

def changePerson(sentence):
#Replaces first person pronouns with second person pronouns
    words = sentence.split()
    replyWords = []
    for word in words:
        replyWords.append(replacements.get(word, word))
    return " ".join(replyWords)
    
#Main Function
def main():
    DrGui().mainloop()   

#Global call to main
main()