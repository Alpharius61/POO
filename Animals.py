import random
import Data as Data


class Animal:
    
    
    def __init__(
        
        self,
        Number,
        Spicies,
        Color,
        Speed = 0,
        Age = 1        
        ): 


        """
            Constructeur
        """
        self.Number = Number
        self.Spicies = Spicies
        self.Color = Color
        self.Speed = Speed
        self.Age = Age

    
    
    @classmethod
    def PrintAnimals(cls):
        
        AnimalsPossibility = ["Lapin","Blaireau", "Chat", "Mésange", "Python", "Chien", "Tourterelle", "Coccinelle", "Abeille"]
        ColorList  = ["Blanc", "Vert", "Bleu", "Rouge", "Jaune"]
        
        Data.AnimalsList = []
        
        CorrectEntry = False
        while CorrectEntry == False :

            try :
                AnimalNumber = int(input("Combien d'animaux voulez vous ? "))
                CorrectEntry = True
            except :
                continue
        
        
        for MyAnimal in range (0, AnimalNumber) :
            AnimalIndex = random.randint(0, len(AnimalsPossibility)-1)
            ColorIndex = random.randint(0, len(ColorList)-1)
            NewAnimal = Animal(MyAnimal, AnimalsPossibility[AnimalIndex],ColorList[ColorIndex],Age = random.randint(1,20))
            Data.AnimalsList.append(NewAnimal)
            
            Determinant = "Le "

            if NewAnimal.Spicies == "Mésange" or NewAnimal.Spicies == "Tourterelle" or NewAnimal.Spicies == "Coccinelle":
                Determinant = "La "
            
            elif NewAnimal.Spicies == "Abeille" :
                Determinant = "L'"
            
            print(f"{Determinant}{NewAnimal.Spicies}, animal numéro {NewAnimal.Number + 1}, de couleur {NewAnimal.Color} a {NewAnimal.Age} ans")
    


    @classmethod
    def AgingAnimals(cls) :
        Data.AnimalsList
        



