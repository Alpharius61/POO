import random
import json
import Data as Data


class Animal:
    
    
    def __init__(
        
        self,
        Number,
        Spicies,
        Name,
        Color,
        Speed,
        Age = 1        
        ): 


        """
            Constructeur
        """
        self.Number = Number
        self.Spicies = Spicies
        self.Name = Name
        self.Color = Color
        self.Speed = Speed
        self.Age = Age

    
    
    
    def LoadAnimalsData():

        try :
            with open("SpiciesCaract.json","r", encoding="utf-8") as AnimalsFile :
                Data.AnimalsData= json.load(AnimalsFile)
                
        except :
            print("Erreur lors du chargement des données des animaux")

    @classmethod
    def PrintAnimals(cls):
        
        AnimalsPossibility = ["Lapin","Blaireau", "Chat", "Mésange", "Python", "Chien", "Tourterelle", "Coccinelle", "Abeille","Cochon"]
        ColorList  = ["Blanc", "Vert", "Bleu", "Rouge", "Jaune","Rose"]
        
        Data.AnimalsList = []
        
        CorrectEntry = False
        while CorrectEntry == False :

            try :
                AnimalNumber = int(input("Combien d'animaux voulez vous (entre 2 et 10) ? "))
                if AnimalNumber>=2 and AnimalNumber<=10 :
                    CorrectEntry = True
            except :
                continue
        
        
        for MyAnimal in range (0, AnimalNumber) :
            # AnimalIndex = random.randint(0, len(AnimalsPossibility)-1)
            # ColorIndex = random.randint(0, len(ColorList)-1)
            # MyAnimal= Animal(MyAnimal, AnimalsPossibility[AnimalIndex],ColorList[ColorIndex],Age = random.randint(1,20))

            SpieciesSelcted = random.choice(AnimalsPossibility)
            AnimalNameIndex = random.randint(0, len(Data.AnimalsData[SpieciesSelcted]['Name'])-1)
            AnimalColorIndex = random.randint(0, len(Data.AnimalsData[SpieciesSelcted]['Colors'])-1)
            AnimalSpeed = random.randint(Data.AnimalsData[SpieciesSelcted]['SpeedMin'],Data.AnimalsData[SpieciesSelcted]['SpeedMax'])
            
            MyAnimal = Animal(MyAnimal, Data.AnimalsData[SpieciesSelcted]['Spiecies'], Data.AnimalsData[SpieciesSelcted]['Name'][AnimalNameIndex], Data.AnimalsData[SpieciesSelcted]['Colors'][AnimalColorIndex],AnimalSpeed,Age = random.randint(1,20))
        
            Data.AnimalsList.append(MyAnimal)
            Data.AnimalsData[SpieciesSelcted]['Name'].pop(AnimalNameIndex)
            
            if len(Data.AnimalsData[SpieciesSelcted]['Name']) == 0 :
                AnimalsPossibility.remove(SpieciesSelcted)
            
            Determinant = "Le "

            if MyAnimal.Spicies == "Mésange" or MyAnimal.Spicies == "Tourterelle" or MyAnimal.Spicies == "Coccinelle":
                Determinant = "La "
            
            elif MyAnimal.Spicies == "Abeille" :
                Determinant = "L'"
            
            # print(f"{Determinant}{MyAnimal.Spicies}, animal numéro {MyAnimal.Number + 1}, de couleur {MyAnimal.Color} a {MyAnimal.Age} ans")
    

    @classmethod
    def AnimalRacing(cls):
        CorrectEntry = False
        while CorrectEntry == False :

            try :
                RacingLength = int(input("\nQuelle est la longueure de la course (entre 100 et 1000 Km) :\n"))
                if RacingLength>= 100 and RacingLength<= 1000:
                    CorrectEntry = True
            except :
                continue
    
        
        ListOfAnimalsSpeed = []
        for AnimalRacer in Data.AnimalsList :
            ListOfAnimalsSpeed.append(AnimalRacer.Speed)
        ListOfAnimalsSpeed = sorted(ListOfAnimalsSpeed,reverse= True)
        
        Ranking = 1
        for AnimalSpeed in ListOfAnimalsSpeed :
            for Animal in Data.AnimalsList :
                if AnimalSpeed == Animal.Speed :
                    end = "ème"
                    if Ranking == 1:
                        end = "er"

                    print(f"Le {Animal.Spicies} nommé {Animal.Name}, avançant à {Animal.Speed}km/h, est arrivé {Ranking}{end} ")
                    Ranking += 1



    @classmethod
    def AgingAnimals(cls) :
        
        Restart = True
        while Restart == True :
        
            InputRight = False
            while InputRight == False :
                try :
                    AnimalChoice = int(input("\nChoisir un animal : 1(Lapin), 2(Blaireau), 3(Chat), 4(Mésange),5(Python)\n6(Chien), 7(Tourterelle), 8(Coccinelle), 9(Abeille), 10(Cochon) 0(Quitter) :\n"))
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
            elif AnimalChoice == 10 : 
                AnimalChoice = "Cochon"
            elif AnimalChoice == 0 : 
                Restart = False
                break

            InputRight = False
            while InputRight == False :
                try :
                    NewAnimalAge = int(input("De combien d'année(s) les animaux viellissent ?\n"))
                    InputRight = True
                
                except:
                    continue
    
            
            for Animal in Data.AnimalsList :
                
                if Animal.Spicies ==  AnimalChoice :
                    Animal.Age += NewAnimalAge
                
                if NewAnimalAge <= 0 :
                    Restart = False

                Determinant = "Le "

                if Animal.Spicies == "Mésange" or Animal.Spicies == "Tourterelle" or Animal.Spicies == "Coccinelle":
                    Determinant = "La "
                
                elif Animal.Spicies == "Abeille" :
                    Determinant = "L'"
                
                print(f"{Determinant}{Animal.Spicies}, animal numéro {Animal.Number + 1}, de couleur {Animal.Color} a {Animal.Age} ans")

            
                

    


