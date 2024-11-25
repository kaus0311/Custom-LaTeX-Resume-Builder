from string import Template

class personalInfo:
    def __init__(self, number, mail, linkedin, github):
        self.number = number
        self.mail = mail
        self.linkedin = linkedin
        self.github = github
    
    from string import Template

    def getLatex(self):
        result = []

        if self.number:
            template = Template(r"\href[pdfnewwindow=true]{tel:+$number}{\scalebox{1.2}{\faMobilePhone} \ $number} \\")
            numScript = template.substitute(number=self.number)
            result.append(numScript)

        if self.mail:
            template = Template(r"\href[pdfnewwindow=true]{mailto:$mail}{\faEnvelope \ \underline{$mail}} \\")
            mailScript = template.substitute(mail=self.mail)
            result.append(mailScript)

        if self.linkedin:
            template = Template(r"\href[pdfnewwindow=true]{$linkedin}{\faLinkedin \ \underline{$linkedin}} \\")
            linkedinScript = template.substitute(linkedin=self.linkedin)
            result.append(linkedinScript)

        if self.github:
            template = Template(r"\href[pdfnewwindow=true]{$github}{\faGithub \ \underline{$github}} \\")
            githubScript = template.substitute(github=self.github)
            result.append(githubScript)

        return r"""\address""" + "\n\t{\n\t\t" + "\n\t\t".join(result) + "\n\t}"

