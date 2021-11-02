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
            MyAnimal= Animal(MyAnimal, AnimalsPossibility[AnimalIndex],ColorList[ColorIndex],Age = random.randint(1,20))
            Data.AnimalsList.append(MyAnimal)
            
            Determinant = "Le "

            if MyAnimal.Spicies == "Mésange" or MyAnimal.Spicies == "Tourterelle" or MyAnimal.Spicies == "Coccinelle":
                Determinant = "La "
            
            elif MyAnimal.Spicies == "Abeille" :
                Determinant = "L'"
            
            print(f"{Determinant}{MyAnimal.Spicies}, animal numéro {MyAnimal.Number + 1}, de couleur {MyAnimal.Color} a {MyAnimal.Age} ans")
    


    @classmethod
    def AgingAnimals(cls) :
        
        
        InputRight = False
        while InputRight == False :
            try :
                AnimalChoice = int(input("Choisir un animal : 1(Lapin), 2(Blaireau), 3(Chat), 4(Mésange), 5(Python), 6(Chien), 7(Tourterelle), 8(Coccinelle), 9(Abeille)"))
                InputRight = True
            
            except:
                continue
        
        if AnimalChoice == 1:
            AnimalChoice = "Lapin"
        elif AnimalChoice == 2 : 
            AnimalChoice = "Blaireau"
        elif AnimalChoice == 3 : 
            AnimalChoice = "Chat"
        elif AnimalChoice == 4 : 
            AnimalChoice = "Mésange"
        elif AnimalChoice == 5 : 
            AnimalChoice = "Python"
        elif AnimalChoice == 6 : 
            AnimalChoice = "Chien"
        elif AnimalChoice == 7 : 
            AnimalChoice = "Tourterelle"
        elif AnimalChoice == 8 : 
            AnimalChoice = "Coccinelle"
        elif AnimalChoice == 9 : 
            AnimalChoice = "Abeille"

        InputRight = False
        while InputRight == False :
            try :
                NewAnimalAge = int(input("Combien d'année les animaux viellissent ?\n"))
                InputRight = True
            
            except:
                continue

        
        
        for Animal in Data.AnimalsList :
            
            if Animal.Spicies ==  AnimalChoice :
                Animal.Age += NewAnimalAge

            Determinant = "Le "

            if Animal.Spicies == "Mésange" or Animal.Spicies == "Tourterelle" or Animal.Spicies == "Coccinelle":
                Determinant = "La "
            
            elif Animal.Spicies == "Abeille" :
                Determinant = "L'"
            
            print(f"{Determinant}{Animal.Spicies}, animal numéro {Animal.Number + 1}, de couleur {Animal.Color} a {Animal.Age} ans")

            
                

    


