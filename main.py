import docGen
from Structure.info import info
from Structure.personalInfo import personalInfo

name = "Kaustubh"
phone = "+16027578002"
email = "knegi2@asu.edu"

addPersonalInfo = personalInfo(phone, email, "", "")
addInfo = info(name, addPersonalInfo)

content = addInfo.getLatex()
docGen.createDoc("test1", content)