class personalInfo:
    def __init__(self, number, mail, linkedin, github):
        self.number = number
        self.mail = mail
        self.linkedin = linkedin
        self.github = github
    
    def getLatex(self):
        
		# \href[pdfnewwindow=true]{tel:+16232122089}{\scalebox{1.2}{\faMobilePhone} \ +1 (623) 212-2089} \\ 
		# \href[pdfnewwindow=true]{mailto:aniket.patil1406@gmail.com}{\faEnvelope \ \underline{aniket.patil1406@gmail.com}} \\ 
		# \href[pdfnewwindow=true]{https://www.linkedin.com/in/apatil1406}{\faLinkedin \ \underline{linkedin.com/in/apatil1406}} \\ 
		# \href[pdfnewwindow=true]{https://www.github.com/patil-aniket}{\faGithub \ \underline{github.com/patil-aniket}}