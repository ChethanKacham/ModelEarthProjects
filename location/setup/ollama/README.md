# Remove and add back Ollama

**comment-out.py**
Remove before deploying via Docker to Google Cloud (or other host)

**uncomment.py**
Add back Ollama to sync with the parent open-webui repo


Run in the root of your website to apply scripts.
Change "projects" to other open-webui forks in your webroot.

	python projects/location/setup/ollama/comment-out.py "projects"