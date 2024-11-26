import docGen
from Structure.info import info
from Structure.personalInfo import personalInfo
from Structure.section import section

name = "Kaustubh"
phone = "+16027578002"
email = "knegi2@asu.edu"

added = section("Education", "Arizona State University")
addPersonalInfo = personalInfo(phone, email, "", "")
addInfo = info(name, addPersonalInfo)
addInfo.addSection(added)

content = addInfo.getLatex()
docGen.createDoc("test1", content)