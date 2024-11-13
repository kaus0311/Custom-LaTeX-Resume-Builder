import docGen
def genLat(name, phone, email, linkedin, github):
    header_template = r"""\documentclass{{type1}} % Ensure 'resume' class is properly defined or included

\usepackage[left=0.4in,top=0.4in,right=0.4in,bottom=0.4in]{{geometry}} % Margins setup
\usepackage{{hyperref}} % For clickable links
\usepackage{{fontawesome}} % For icons

\name{{{name}}} % Your name
\address 
    {{
        \href[pdfnewwindow=true]{{tel:{phone}}}{{\scalebox{{1.2}}{{\faMobilePhone}} \ {phone}}} \\ 
        \href[pdfnewwindow=true]{{mailto:{email}}}{{\faEnvelope \ \underline{{{email}}}}} \\ 
        \href[pdfnewwindow=true]{{{linkedin}}}{{\faLinkedin \ \underline{{linkedin.com/in/{linkedin_handle}}}}} \\ 
        \href[pdfnewwindow=true]{{{github}}}{{\faGithub \ \underline{{github.com/{github_handle}}}}}
    }}
\start{{document}}
\end{{document}}
    """
    
    # Extract handles from LinkedIn and GitHub URLs
    linkedin_handle = linkedin.split('/')[-1]
    github_handle = github.split('/')[-1]
    
    # Format the template with the provided arguments
    formatted_header = header_template.format(
        name=name,
        phone=phone,
        email=email,
        linkedin=linkedin,
        github=github,
        linkedin_handle=linkedin_handle,
        github_handle=github_handle
    )
    
    return formatted_header

# Example usage
latex_header = genLat(
    name="Kaustubh Negi",
    phone="+1 (623) 212-2089",
    email="aniket.patil1406@gmail.com",
    linkedin="https://www.linkedin.com/in/apatil1406",
    github="https://www.github.com/patil-aniket"
)

docGen.createDoc("Aniket",latex_header)