class info:
    def __init__(self, name, personalInfo):
        self.name = name
        self.personalInfo = personalInfo
        self.sections = {}
    
    def addSection(self,sectionName, content):
        self.sections.append(content)
             
adding = info("Kaus", "Negi")
adding.addSection("Hello World")

