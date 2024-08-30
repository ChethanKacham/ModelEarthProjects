# Remove and add back Ollama

Under development:
The first script will allow us to Sync from the parent repo without conflicts by temporarily adding back Ollama.  
The second script will comment out Ollama again.

**comment-out.py**
Remove before deploying via Docker to Google Cloud (or other host)

**uncomment.py**
Add back Ollama to sync with the parent open-webui repo

Fork and clone the projects repor (which is a fork of open-webui)
[github.com/ModelEarth/projects](https://github.com/ModelEarth/projects)

Run in the root of your website to apply scripts.

	python projects/location/setup/ollama/comment-out.py "projects"


After completing code updates using the "projects" repo,
make a fork of this repo: [github.com/datascape/open-webui](https://github.com/datascape/open-webui)

Pull your fork locally, then run:

	python projects/location/setup/ollama/comment-out.py "open-webui"

Update the "uncomment.py" script to do the reverse of the "comment-out.py" script.