# Customize Open Web UI

We're building add-ons for Teams and Locations.
The following will remove our custom changes so we can sync from [open-webui](https://github.com/open-webui/open-webui).

## Sync.py

Develop sync.py in [github.com/ModelEarth/projects](https://github.com/ModelEarth/projects) (which is a fork of open-webui)

<!-- TO DO: Change title back to "Open WebUI" and remove inserted localsite.js -->

TO DO: Remove comments we added to deactivate Ollama. 
Files and lines updated are in file-lines.py (which will also be used by customize.py to add comments).

Run in the root of your website to apply scripts.

	python projects/location/setup/ollama/sync.py "projects"


After completing code updates using the "projects" repo,
make a fork of this repo: [github.com/datascape/open-webui](https://github.com/datascape/open-webui)

Pull your fork locally, then run:

	python projects/location/setup/ollama/sync.py "open-webui"


## Customize.py

We comment out Ollama to reduce costs when deploying Docker to Google Cloud.

Update the "customize.py" script to do the reverse of the "sync.py" script.

**TO DO in src/app.html**

Change title="Open WebUI" to "Open WebUI ModelEarth"

Insert:

	<script type="text/javascript" src="https://model.earth/localsite/js/localsite.js?showheader=true&showsearch=true"></script>

