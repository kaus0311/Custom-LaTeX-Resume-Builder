import docGen
class info:
    def __init__(self, name, personalInfo):
        self.name = name
        self.personalInfo = personalInfo
        self.sections = {}
    
    def addSection(self, section):
        self.sections.add(section)
             
    def getLatex(self):
        name = r"""\name{""" + self.name +"}"
        per = self.personalInfo.getLatex()
        l1 = r"""\documentclass{resume}"""
        l2 = r"""\usepackage[left=0.4in,top=0.4in,right=0.4in,bottom=0.4in]{geometry}"""
        doc =  r"""\begin{document}""" + "\n"
        for i in self.sections:
            doc += i.getLatex() + "\n"
        doc += r"""\end{document}"""
        return l1 + "\n" + l2 + "\n" + name + "\n" + per + "\n" + doc