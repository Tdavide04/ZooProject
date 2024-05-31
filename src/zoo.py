'''
Creaiamo un sistema di gestione di uno zoo virtuale

Sistema di gestione dello zoo virtuale

Classi:

1. Zoo: questa classe rappresenta uno zoo. Lo zoo ha dei recinti fences e dei guardiani dello zoo, zoo_keepers.

2. Animal: questa classe rappresenta un animale nello zoo. 
Ogni animale ha questi attributi: name, species, age, height, width, preferred_habitat, health che è uguale a round(100 * (1 / age), 3).

3. Fence: questa classe rappresenta un recinto dello zoo in cui sono tenuti gli animali. I recinti possono contenere uno o più animali. 
I recinti possono hanno gli attributi area, temperature e habitat.

4. ZooKeeper: questa classe rappresenta un guardiano dello zoo responsabile della gestione dello zoo. I guardiani dello zoo hanno un nome, un cognome, e un id. 
Essi possono nutrire gli animali, pulire i recinti e svolgere altri compiti nel nostro zoo virtuale.

Funzionalità:

1. add_animal(animal: Animal, fence: Fence) (Aggiungi nuovo animale): consente al guardiano dello zoo di aggiungere un nuovo animale allo zoo. 
L'animale deve essere collocato in un recinto adeguato in base alle esigenze del suo habitat e se c'è ancora spazio nel recinto, 
ovvero se l'area del recinto è ancora sufficiente per ospitare questo animale.

2. remove_animal(animal: Animal, fence: Fence) (Rimuovi animale): consente al guardiano dello zoo di rimuovere un animale dallo zoo. 
L'animale deve essere allontanato dal suo recinto. Nota bene: L'area del recinto deve essere ripristinata dello spazio che l'animale rimosso occupava.

3. feed(animal: Animal) (Dai da mangiare agli animali): implementa un metodo che consenta al guardiano dello zoo di nutrire tutti gli animali dello zoo. 
Ogni volta che un animale viene nutrito, la sua salute incrementa di 1% rispetto alla sua salute corrente, 
ma le dimensioni dell'animale (height e width) vengono incrementate del 2%. Perciò, 
l'animale si può nutrire soltanto se il recinto ha ancora spazio a sufficienza per ospitare l'animale ingrandito dal cibo.

4. clean(fence: Fence) (Pulizia dei recinti): implementare un metodo che consenta al guardiano dello zoo di pulire tutti i recinti dello zoo. 
Questo metodo restituisce un valore di tipo float che indica il tempo che il guardiano impiega per pulire il recinto. 
Il tempo di pulizia è il rapporto dell'area occupata dagli animali diviso l'area residua del recinto. Se l'area residua è pari a 0, restituire l'area occupata.

5. describe_zoo() (Visualizza informazioni sullo zoo): visualizza informazioni su tutti i guardani dello zoo, sui recinti dello zoo che contengono animali. 

E.s.: Se abbiamo un guardiano chiamato Lorenzo Maggi con matricola 1234, e un recinto Fence(area=100, temperature=25, 
habitat=Continentale) con due animali Animal(name=Scoiattolo, species=Blabla, age=25, ...), 
Animal(name=Lupo, species=Lupus, age=14,...) ci si aspetta di avere una rappresentazione testuale dello zoo come segue:

Guardians:

ZooKeeper(name=Lorenzo, surname=Maggi, id=1234)

Fences:

Fence(area=100, temperature=25, habitat=Continent)

with animals:

Animal(name=Scoiattolo, species=Blabla, age=25)

Animal(name=Lupo, species=Lupus, age=14)

#########################
Fra un recinto e l'altro mettete 30 volte il carattere #.
'''



class Animal:
 
    def __init__(self, name, species, age, height, width, preferred_habitat):
        self.name = name
        self.species = species
        self.age = age
        self.height = height
        self.width = width
        self.preferred_habitat = preferred_habitat
        self.health = round(100 * (1 / age), 3)
        self.animal_area = self.height * self.width
        self.fence = None
       
       
class Fence:
    def __init__(self, area, temperature, habitat):
        self.area = area
        self.temperature = temperature
        self.habitat = habitat
        self.list_of_animal = []
        
    def occupied_area(self) -> int:
        return sum(animal.animal_area for animal in self.list_of_animal)
    
    def residual_area(self) -> int:
        return self.area - self.occupied_area()
        
        
class ZooKeepers:
    def __init__(self, name, surname, id):
        self.name = name
        self.surname = surname
        self.id = id
    
    def add_animal(self, animal: Animal, fence: Fence):
        if animal.animal_area < fence.residual_area():
            if animal.preferred_habitat == fence.habitat:
                fence.list_of_animal.append(animal)
                animal.fence = fence
        else:
            return "There is no space"

    def remove_animal(self, animal: Animal, fence: Fence):
        if animal in fence.list_of_animal:
            fence.list_of_animal.remove(animal)

    def feed(self, animal: Animal):
        if animal.fence is None:
            return "Animal is not in any fence"
        
        new_height = animal.height  * 1.02
        new_width = animal.width * 1.02
        animal.animal_area = new_height * new_width
        
        if animal.animal_area <= animal.fence.residual_area():
            for animal_in_fence in animal.fence.list_of_animal:
                animal_in_fence.width = new_width
                animal_in_fence.height = new_height
                animal_in_fence.health *= 1.01
            else:
                return "Impossible to feed animals. There is no space"
    
    def clean(self, fence: Fence):
        if fence.residual_area() == 0:
            return fence.occupied_area()
        return fence.occupied_area() / fence.residual_area()
    
class Zoo:
    def __init__(self):
        self.fences: list[Fence] = []
        self.zoo_keepers: list[ZooKeepers] = []

    def describe_zoo(self):
        print("Guardian:")
        for keeper in self.zoo_keepers:
            print(f"Zookeeper(name = {keeper.name}, surname = {keeper.surname}, id = {keeper.id})")
        
        print("Fences:")
        for fence in self.fences:
            print(f"Fence(area = {fence.area}, temperature = {fence.temperature}, habitat = {fence.habitat})")
            print("with animal:")
            for animal in fence.list_of_animal:
                print(f"Animal(name = {animal.name}, species = {animal.species}, age = {animal.age})")
            print("#"*30)




#Matteo = ZooKeepers("Matteo", "Rossi", 123)
#Giacomo = ZooKeepers("Giacomo", "tonto", 45)

#Gatto = Animal("Gatto", "Felis catus", 5, 30, 20, "Domestico")
#Lupo = Animal("Lupo", "Canis lupus", 8, 80, 100, "Blabla")

#Recinto1 = Fence(2000000, 25, "Domestico")
#Recinto2 = Fence(4000000, 32, "Blabla")

#Matteo.add_animal(Gatto, Recinto1)
#Matteo.add_animal(Lupo, Recinto2)

#zoo = Zoo([Recinto1, Recinto2], [Matteo, Giacomo])
#zoo.describe_zoo()

#Matteo.feed(Gatto)
#Matteo.feed(Lupo)

##zoo.describe_zoo()




