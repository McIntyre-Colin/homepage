#Constant across pages

header = open('./templates/header.html').read()
footer = open('./templates/footer.html').read()

#Page content
index = open('./content/index.html').read()
projects = open('./content/projects.html').read()
resume = open('./content/resume.html').read()

#Combining into one variable
index = header + index + footer
projects = header + projects + footer
resume = header + resume + footer

#Crwating webpages
open('./docs/index.html', 'w+').write(index)
open('./docs/projects.html', 'w+').write(projects)
open('./docs/resume.html', 'w+').write(resume)