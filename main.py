class Robot:
    def __init__(self, name, purpose, language):
        
        self.name = name
        self.purpose = purpose
        self.language = language
        
    def introduce(self):
        print(f"hello, I am {self.name}.")
        print(f"My purpose is to {self.purpose}.")
        print(f"I communicate using {self.language}.")
        
class AI_Robot(Robot):
    def __init__(self, name, purpose, language,version):
        super().__init__(name, purpose, language)
        self.version = version
    
    def ai_details(self):
        print(f"i am powered by AI , version {self.version}.")
        print("i learn from interactions and improve with time.")
        
my_robot = AI_Robot("Tequila's robot", "assist tequila  with information and tasks", "natural language", "6.1")


my_robot.introduce()
my_robot.ai_details()