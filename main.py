import docGen

latex_content = r"""
\documentclass{type1} % Ensure 'resume' class is properly defined or included

\usepackage[left=0.4in,top=0.4in,right=0.4in,bottom=0.4in]{geometry} % Margins setup

\name{Kaustubh Negi} % Your name
\address 
	{
		\href[pdfnewwindow=true]{tel:+16232122089}{\scalebox{1.2}{\faMobilePhone} \ +1 (623) 212-2089} \\ 
		\href[pdfnewwindow=true]{mailto:aniket.patil1406@gmail.com}{\faEnvelope \ \underline{aniket.patil1406@gmail.com}} \\ 
		\href[pdfnewwindow=true]{https://www.linkedin.com/in/apatil1406}{\faLinkedin \ \underline{linkedin.com/in/apatil1406}} \\ 
		\href[pdfnewwindow=true]{https://www.github.com/patil-aniket}{\faGithub \ \underline{github.com/patil-aniket}}
	}


\begin{document}
	% Education Section
	\begin{rSection}{Education}
		{\bf Arizona State University} \hfill May 2026 \\
		Master of Science in Computer Software Engineering \\
		{\bf University of Mumbai} \hfill May 2022 \\
		Bachelor of Engineering in Information Technology
	\end{rSection}
	
	% Technical Skills Section
	\begin{rSection}{Technical Skills}
		 \begin{tabular}{ @{} >{\bfseries}l @{\hspace{6ex}} l }
			Languages & Python, JavaScript, C\#, C++, C, Java, PHP, JQuery \\
			Frameworks / Libraries & React.JS, Angular, .Net Core, SpringBoot, Laravel (PHP) \\ % Adjusted label for consistency
			Databases / Technologies & SQL, MongoDB, Kafka, Elasticsearch, Microservices \\
			Cloud Technologies & Azure, AWS, Firebase
		\end{tabular}
	\end{rSection}
	
	% Work Experience Section
	\begin{rSection}{Work Experience}
		\begin{rSubsection}{GEP Worldwide}{June 2022 - August 2024}{Software Engineer}
			\item Led the development of backend APIs using {\bf C\# (.NET Core)} within a microservices architecture, with {\bf MongoDB} and {\bf ElasticSearch} for efficient data management and retrieval, improving service scalability and cross-team collaboration.
			\item Engineered an anomaly detection system in the Invoice module, leveraging {\bf ElasticSearch} for analysing data and {\bf enhancing accuracy by 20\%}, which improved client audits and customer satisfaction.
			\item Integrated {\bf Generative AI (GenAI)} features into the Invoice module using {\bf FastAPI (Python)} for the backend and {\bf Angular} for the frontend, reducing manual effort and {\bf accelerating processes by 25\%}, delivering significant efficiency gains for customers.
			\item Encouraged teamwork and {\bf improved code quality} by conducting {\bf peer code reviews}, which enhanced collaboration, reduced defects, and accelerated development cycles, resulting in {\bf increased team efficiency}.
		\end{rSubsection}
		\begin{rSubsection}{Dquip CRM}{August 2021 - June 2022}{Jr. Software Developer (Intern)}
			\item Engineered critical operational features using {\bf Laravel (PHP)} and {\bf jQuery}, including slot request management, automated bill of lading, approval transfers, and a one-click multiple approvals function, that streamlined processes and enhanced workflows, significantly {\bf reducing manual effort and operational costs}.
			\item Optimized {\bf SQL stored procedures}, boosting system efficiency and ensuring data integrity, which accelerated data processing times and improved overall system performance.
		\end{rSubsection}
	\end{rSection}
	
	% Projects Section
	\begin{rSection}{Projects}
		\begin{rProject}{2048 Game}{https://github.com/patil-aniket/2048}{Next.js, Typescript, Tailwind CSS}{Fall 2024}
			\item Developing a web-based 2048 game using  {\bf Next.js} with {\bf typescript} including features like tile movement, merging logic, and responsive UI
			\item Implementing an  {\bf auto-solver} algorithm to autonomously play and solve the game.
		\end{rProject}
		\begin{rProject}{AI Game Solvers}{https://github.com/patil-aniket/AI-Game-Solvers}{Python}{Spring 2024}
			\item Engineered AI solvers for Sliding Tiles, Sudoku, and 2048 using advanced techniques. 
			\item Implemented  {\bf A*, BFS, and DFS} for Sliding Tiles with  {\bf Manhattan distance optimization}.
			\item Built a 2048 solver using  {\bf Expectiminimax with alpha-beta pruning}, achieving sub-0.2 second move computations.
		\end{rProject}
		\begin{rProject}{Water Management System}{https://github.com/patil-aniket/WaterManage}{React Native, Firebase, C, NodeMCU}{Summer 2022}
			\item Developed an Internet of Things (IoT)-enabled model and application for automated water management.
			\item Designed a circuit using  {\bf NodeMCU} to detect the level of water in storage tank.
			\item Integrated a mobile application for  {\bf real-time water level monitoring} and controlling the system remotely.
		\end{rProject}
	\end{rSection}

	% ACHIEVEMENTS Section
	\begin{rSection}{Achievements}
		\begin{rSubsection}{}{}{}
			\item Achieved Award for Exemplary Contribution In GEP Worldwide
			\item Ranked 2nd in inter college coder of the semester competition during Semester 6
			\item Led a winning team for project-based learning in 3rd semester of engineering
		\end{rSubsection}
	\end{rSection}

\end{document}

"""

docGen.createDoc("Kaus",latex_content)