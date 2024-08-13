[Active Projects](../)
# Location Projects for Open WebUI

GETTING STARTED

If you're contributing code, use our [Install for Building Locally](setup) steps.  
To build locally, you'll skip the local Docker install. Fork our [projects](https://github.com/ModelEarth/projects/) repo, which is a fork of open-webui.  

If you're NOT building code, use the [local Docker install](setup/docker).
This [Open WebUI video](https://www.youtube.com/watch?v=N-aRJe--txs) walks through downloading Ollama and Docker like we've documented on the local.

## Contribute in our Open WebUI "projects/location" folder

The "projects/location" folder is where we add extras - we're still perfecting [build process](setup).  
To avoid merge errors, if you're making updates in the "src" and "backend" folders, 
prepend "team-" to the names of the files you've copied and customized.

TO DO: The html we added in this "projects" fork is breaking the GitHub Docker build.  
Instead try simple edits in our [open-webui-earthscape](https://github.com/earthscape/open-webui-earthscape) fork. (Write loren to be added as a contributor.)

## Our OpenWebUI Projects

TO DO: Use Flask in a [projects/backend/location](https://github.com/ModelEarth/projects/tree/main/backend) folder and interact with our Supabase REST API - Nanden

TO DO: Create an example of running [Run-Models-bkup.ipynb](https://github.com/ModelEarth/RealityStream/tree/main/models) saved from our [RealityStream CoLab](../../RealityStream/).

TO DO: Set up [RAG context](https://docs.openwebui.com/tutorial/rag/) using our [Supabase International Trade Flow](../../OpenFootprint/prep/sql/supabase/) data.

TO DO: Set up [RAG context](https://docs.openwebui.com/tutorial/rag/) using our [superthermal evaporation](../../evaporation-kits/) page and related articles.


<!--TO DO: Activate hosting using Cloudflare.-->

TO DO: Provide a means to upload a list of members from a Google Sheet link.

DONE: Provide a button for admins to export the list of members as a CSV file. (In ModelEarthBranch) - Yuxin

TO DO: Update our Readme in localsite.js to one that supports [NOTE], [WARNING], [TIP]

DONE: The localsite.js is commented out until adjustments are made to prevent overlapping the top.

	<script type="text/javascript" src="https://model.earth/localsite/js/localsite.js?showheader=true&showsearch=true"></script>


[Install for Building Locally](setup) 
