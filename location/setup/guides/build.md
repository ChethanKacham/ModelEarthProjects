# Building Branches Locally

## Important: To avoid failed "Actions" when contributing

**1. Use ModelEarthBranch**: Work in the ModelEarthBranch when introducing new features.  
Avoid editing the main branch to avoid `build_release` errors.  
We change the "version" number in package.json (and package-lock.json ?) whenever we add to the main branch.

**2. Frontend Formatting**:

A. Before pushing changes to the frontend code, run to ensure proper formatting:

    npm run format
    npm run i18n:parse

B. Add your own tests in the `cypress/e2e/` folder and start the server.  
Run the following to execute the test suites. Ensure all tests pass without errors.

    npx cypress run

**3. Backend Formatting**:
For any backend changes, run to maintain code formatting.  
Add any necessary tests to ensure your code changes are covered.

    npm run format:backend

**4. Pull Requests Merging**:
After creating a pull request, fill in the template and wait for all workflows to execute.  
Address any issues if a workflow fails before merging into the main branch.

Note: We removed Ollama and chat.cy.ts in the actions.  
See our [changelog](https://github.com/datascape/open-webui/blob/gha-test/.github/CHANGELOG-workflow.md). And a [workflow PR](https://github.com/ModelEarth/projects/pull/7) with these changes initially applied in datascape.
