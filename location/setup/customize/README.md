# Customize for Teams and Locations

We custom code, then remove customizations when syncing from the open-webui parent.

## Customize.py

Comment out Ollama

Remove before deploying via Docker to Google Cloud (or other host)

# TO DO in src/app.html

Change title="Open WebUI" to "Open WebUI ModelEarth"

# Insert:

	<script type="text/javascript" src="https://model.earth/localsite/js/localsite.js?showheader=true&showsearch=true"></script>


## Sync.py

TO DO: Change title back to "Open WebUI" and remove inserted localsite.js

Add back Ollama to sync with the parent open-webui repo

Fork and clone the projects repor (which is a fork of open-webui)
[github.com/ModelEarth/projects](https://github.com/ModelEarth/projects)

Run in the root of your website to apply scripts.

	python projects/location/setup/ollama/customize.py "projects"


After completing code updates using the "projects" repo,
make a fork of this repo: [github.com/datascape/open-webui](https://github.com/datascape/open-webui)

Pull your fork locally, then run:

	python projects/location/setup/ollama/customize.py "open-webui"

Update the "sync.py" script to do the reverse of the "customize.py" script.