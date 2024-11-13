\ProvidesClass{resume}[2010/07/10 v0.9 Resume class]

\LoadClass[11pt,letterpaper]{article} % Font size and paper type
\usepackage{times}
\usepackage[parfill]{parskip} % Remove paragraph indentation
\usepackage{array} % Required for boldface (\bf and \bfseries) tabular columns
\usepackage{ifthen} % Required for ifthenelse statements
\usepackage{amsmath}
\usepackage{hyperref}
\input{glyphtounicode}
\pdfgentounicode=1
\pagestyle{empty} % Suppress page numbers
\usepackage{fontawesome}
\usepackage{xcolor}
\usepackage{graphicx}
\newcommand{\urlNewWindow}[1]{\href[pdfnewwindow=true]{#1}{\nolinkurl{#1}}}

% Set link options
\hypersetup{
    colorlinks=false,
    pdfborder={0 0 0}    % Remove borders around links
}

%----------------------------------------------------------------------------------------
%	HEADINGS COMMANDS: Commands for printing name and address
%----------------------------------------------------------------------------------------

\def \name#1{\def\@name{#1}} % Defines the \name command to set name
\def \@name {} % Sets \@name to empty by default

\def \addressSep {$\diamond$} % Set default address separator to a diamond

% One, two or three address lines can be specified 
\let \@addressone \relax
\let \@addresstwo \relax
\let \@addressthree \relax

% \address command can be used to set the first, second, and third address (last 2 optional)
\def \address #1{
  \@ifundefined{@addresstwo}{
    \def \@addresstwo {#1}
  }{
  \@ifundefined{@addressthree}{
  \def \@addressthree {#1}
  }{
     \def \@addressone {#1}
  }}
}

% \printaddress is used to style an address line (given as input)
\def \printaddress #1{
  \begingroup
    \def \\ {\addressSep\ }
    \centerline{#1}
  \endgroup
  \par
  \addressskip
}

% \printname is used to print the name as a page header
\def \printname {
  \begingroup
    \hfil{\MakeUppercase{\namesize\bf \@name}}\hfil
    \nameskip\break
  \endgroup
}

%----------------------------------------------------------------------------------------
%	PRINT THE HEADING LINES
%----------------------------------------------------------------------------------------

\let\ori@document=\document
\renewcommand{\document}{
  \ori@document  % Begin document
  \printname % Print the name specified with \name
  \@ifundefined{@addressone}{}{ % Print the first address if specified
    \printaddress{\@addressone}}
  \@ifundefined{@addresstwo}{}{ % Print the second address if specified
    \printaddress{\@addresstwo}}
     \@ifundefined{@addressthree}{}{ % Print the third address if specified
    \printaddress{\@addressthree}}
}

%----------------------------------------------------------------------------------------
%	SECTION FORMATTING
%----------------------------------------------------------------------------------------

% Defines the rSection environment for the large sections within the CV
\newenvironment{rSection}[1]{ % 1 input argument - section name
  \sectionskip
  \MakeUppercase{\bf #1} % Section title
  \sectionlineskip
  \hrule % Horizontal line
  \begin{list}{}{ % List for each individual item in the section
    \setlength{\leftmargin}{1.0em} % Margin within the section
  }
  \item[]
}{
  \end{list}
  \vspace{-0.3em}
}

%----------------------------------------------------------------------------------------
%	WORK EXPERIENCE FORMATTING
%----------------------------------------------------------------------------------------

\newenvironment{rSubsection}[3]{ % 3 input arguments - company name, year(s) employed, job title
  \ifthenelse{\equal{#1}{}}
    {}
    {% Otherwise
      {\bf #1}
    }% Bold company name
  \ifthenelse{\equal{#3}{}}% If the third argument (job title) is not specified
    {} % Do nothing
    { % Otherwise, print the pipe and job title
    \ \textbar\ { \em #3}% Pipe and italic job title
    }%
  \ifthenelse{\equal{#2}{}}
    { \vspace{0.8em} } % Do nothing
    {
      {\hfill {#2}\smallskip} % Date on the right
    }
  \begin{list}{\large$\boldsymbol{\cdot}$}{\leftmargin=0em} % \cdot used for bullets, no indentation
    \itemsep -0.6em \vspace{-0.6em} % Compress items in list together for aesthetics
  }{
  \end{list}
  \vspace{0.05em} % Some space after the list of bullet points
}

%----------------------------------------------------------------------------------------
%	PROJECTS FORMATTING
%----------------------------------------------------------------------------------------

\newenvironment{rProject}[4]{ % 3 input arguments - project name, GitHub Link, Technologies, Duration
  \ifthenelse{\equal{#2}{}}% If the second argument (GitHub Link) is not specified
    {% if link is empty simply print project name in bold
      \ifthenelse{\equal{#1}{}}
      {}
      {% Otherwise
        {\bf #1}
      }% Bold Project name
    }
    { % Otherwise print Bold Project name with hyperlink
      \href[pdfnewwindow=true]{#2}{\bf #1 \ \faLink}% Link Symbol and hyperlink to the project
    }%
  \ifthenelse{\equal{#3}{}}% If the third argument (Technologies) is not specified
    {} % Do nothing
    { % Otherwise, print the pipe and italic technologies
    \ \textbar\ { \em #3}% Pipe and italic Technologies
    }%
  \ifthenelse{\equal{#4}{}}
    { \vspace{0.8em} } % Do nothing
    {
      {\hfill {#4}\smallskip} % Date on the right
    }
  \begin{list}{\large$\boldsymbol{\cdot}$}{\leftmargin=0em} % \cdot used for bullets, no indentation [font=$\bullet$\scshape\bfseries]
    \itemsep -0.6em \vspace{-0.6em} % Compress items in list together for aesthetics
  }{
  \end{list}
  \vspace{0.1em} % Some space after the list of bullet points
}


% The below commands define the whitespace after certain things in the document - they can be \smallskip, \medskip or \bigskip
\def\namesize{\huge} % Size of the name at the top of the document
\def\addressskip{\smallskip} % The space between the two address (or phone/email) lines
\def\sectionlineskip{\smallskip} % The space above the horizontal line for each section 
\def\nameskip{\medskip} % The space after your name at the top
\def\sectionskip{\smallskip} % The space after the heading section