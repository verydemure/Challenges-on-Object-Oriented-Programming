class flashcard:

    def __init__(self,word,meaning):
        self.word = word
        self.meaning = meaning

    def __str__(self):
        return f"{self.word} ( {self.meaning} )"
    

flash = []
print("welcome to flashcard application")

while(True):
    word = input("enter the name you want to ass to flashcard:")
    meaning = input("enter the meaning :")

    flash.append(flashcard(word,meaning))
    option = int(input("enter 0,if you wanna play :"))

    if(option):
        break

print("\nYour flashcards")
for i in flash:
    print(">",i)

    