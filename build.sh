rm ./docs/index.html
rm ./docs/projects.html
rm ./docs/resume.html

cat ./templates/header.html ./content/index.html ./templates/footer.html > ./docs/index.html
cat ./templates/header.html ./content/projects.html ./templates/footer.html > ./docs/projects.html
cat ./templates/header.html ./content/resume.html ./templates/footer.html > ./docs/resume.html