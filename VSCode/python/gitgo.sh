# push for the first time

echo "<git init>"
git init

echo "<git add>"
git add .

# fill the "" with your commont
echo "<git commit>"
git commit -m ""

echo "<keygen>"
ssh-keygen -t rsa -C "2013114698@qq.com"

echo "<remote>"
git remote add origin https://github.com/YeungShaoFeng/converter.git

echo "<push>"
git push -u origin master

# if error = "fatal: remote origin already exists."
# then do the following
#git remote rm origin

git status