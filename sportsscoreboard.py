"""
1) Create the `Cricket` class.
   a) Define the constructor with player and score.
   b) Store player and score as private attributes using double underscores.

2) Add methods inside the `Cricket` class.
   a) Create `info()` to display cricket player details.
   b) Create `play()` to show cricket-specific action.
   c) Create `get_score()` to read the private score.
   d) Create `set_score()` to update the score safely.

3) Create the `Football` class.
   a) Define the constructor with player and score.
   b) Store player and score as private attributes.

4) Add methods inside the `Football` class.
   a) Create `info()` to display football player details.
   b) Create `play()` to show football-specific action.
   c) Create `get_score()` to read the private score.
   d) Create `set_score()` to update the score safely.

5) Create sports objects.
   a) Create one Cricket object.
   b) Create one Football object.

6) Demonstrate polymorphism.
   a) Loop through both sports objects.
   b) Call the same `info()` method on each object.
   c) Call the same `play()` method on each object.
   d) Observe how the same method names give different outputs.

7) Demonstrate encapsulation.
   a) Try to directly change the private cricket score.
   b) Use `get_score()` to show that the private score is still protected.

8) Update scores safely.
   a) Use `set_score()` to update the cricket score.
   b) Use `set_score()` to update the football score.
   c) Prevent negative scores using a condition inside the setter.
"""

class Cricket:
    def __init__(self,player, score):
      
        self.__player = player
        self.__score = score

    def info(self):
        print(f"Cricket Player: {self.__player}, Score: {self.__score}")

    def play(self):
        print(f"{self.__player} hits a six!")

    def get_score(self):
        return self.__score

    def set_score(self,  new_score):
        if new_score > 0:
            self.__score = new_score
            print(f"Score updated to {self.__score}")
        else: 
            print("Score cannot be negative.")


class Football: 
     def __init__(self,player, score):
          
            self.__player = player
            self.__score = score
     def info(self):
         print(f"Football Player: {self.__player}, Score: {self.__score}")
            
     def play(self):
         print(f"{self.__player} hits a goal!")

     def get_score(self):
         return self.__score
     
     def set_score(self,  new_score):
      if new_score > 0:
         self.__score = new_score
         print(f"Score updated to {self.__score}")
      else: 
         print("Score cannot be negative.")

c = Cricket("Shivam"
            , 100)
c.info()
c.play()
c.set_score(106)
print(c.get_score())

f = Football("Cristiano", 7)
f.info()
f.play()
f.set_score(10)
print(f.get_score())


for sport in (c, f):
    sport.info()
    sport.play()

print("Trying to change cricket score directly...")
c.__score = 999
print(c.get_score()) 
   

