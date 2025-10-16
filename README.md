
This branch is used exclusively for the project's documentation site.

Usage: In order to update the online documentation 
- `make html` command inside doc_1 folder
- delete the previous content of docs folder except no_jekyll
- copy the content of html folder inside docs_1 into docs
- commit and push then the online doc will be updated

- if the main package changed inside docs branch use `git checkout main -- idpet/` then add, commit and push