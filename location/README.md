[Active Projects](../)
# Location Projects for Open WebUI

GETTING STARTED

If you're contributing code, use our [Install for Building Locally](setup) steps.  
To build locally, you'll skip the local Docker install. Fork our [projects](https://github.com/ModelEarth/projects/) repo, which is a fork of open-webui.  

If you're NOT building code, use the [local Docker install](setup/docker).
This [Open WebUI video](https://www.youtube.com/watch?v=N-aRJe--txs) walks through downloading Ollama and Docker like we've documented on the local.

## Contribute in our Open WebUI "projects/location" folder

The "projects/location" folder is where we add extras - but we don't have a build process yet.  
To avoid merge errors, if you're making updates in the "src" and "backend" folders, 
prepend "team-" to the names of the files you've copied and customized.

TO DO: The html we added in this "projects" fork is breaking the GitHub Docker build.  
Instead try simple edits in our [open-webui-earthscape](https://github.com/earthscape/open-webui-earthscape) fork. (Write loren to be added as a contributor.)

## Our OpenWebUI Projects

TO DO: Use Flask in a [projects/backend/location](https://github.com/ModelEarth/projects/tree/main/backend) folder and interact with our Supabase REST API - Nanden

TO DO: Create an example of running .ipynb from our [RealityStream](../../RealityStream/) app.

TO DO: Set up [RAG context](https://docs.openwebui.com/tutorial/rag/) using our [Supabase International Trade Flow](../../OpenFootprint/prep/sql/supabase/) data.

TO DO: Set up [RAG context](https://docs.openwebui.com/tutorial/rag/) using our [superthermal evaporation](../../evaporation-kits/) page and related articles.


<!--TO DO: Activate hosting using Cloudflare.-->

TO DO: Provide a means to upload a list of members from a Google Sheet link.

DONE: Provide a button for admins to export the list of members as a CSV file. (In ModelEarthBranch) - Yuxin

TO DO: Update our Readme in localsite.js to one that supports [NOTE], [WARNING], [TIP]

DONE: The localsite.js is commented out until adjustments are made to prevent overlapping the top.

	<script type="text/javascript" src="https://model.earth/localsite/js/localsite.js?showheader=true&showsearch=true"></script>


# Contributing to MODEL.EARTH Open WebUI Project

1. **Branching from Main**: Always create a new branch when introducing new features. Avoid editing directly on the main branch to ensure the stability of the project.

2. **Version Updates**: Don’t forget to update the _version number_ when adding new features to the main branch. Failure to do so will cause the `build_release` workflow to fail.

3. **Frontend Formatting**: Before pushing changes to the frontend code, run `npm run format` and `npm run i18n:parse` to ensure proper formatting. Add your own tests under `./cypress/e2e/`, start the server, and run `npx cypress run` to execute the test suites. Ensure all tests pass without errors.

4. **Backend Formatting**: For any backend changes, run `npm run format:backend` to maintain code formatting. Add any necessary tests to ensure your code changes are covered.

5. **Pull Requests Merging**: After creating a pull request, fill in the template and wait for all workflows to execute. Address any issues if a workflow fails before merging into the main branch.



[Install for Building Locally](setup) 
