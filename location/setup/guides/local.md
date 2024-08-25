# Install and Build

## Manual Install w/o Ollama locally

For Linux/MacOS:

    bash location/setup/script/conda-start.sh

For Windows:

```
copy .env.example .env

npm install
npm run build

cd .\backend

# Optional: To install using Conda as your development environment, follow these instructions:
# Create and activate a Conda environment
conda create --name open-webui-env python=3.11
conda activate open-webui-env

pip install -r requirements.txt -U

start.bat
```

Page should be up at http://localhost:8080
Avoid using `npm run dev` or you'll get a message that the backend did not build.
If you encounter issues, see our [Detailed Install Notes](../).

## Using Docker w/ Ollama

Make sure you have [docker](https://www.docker.com/products/docker-desktop/) and [Ollama](https://ollama.com/) installed. Also, follow this [guide](https://github.com/ollama/ollama/blob/86b907f82ad1cc5eb16e919d6cb5830765d73be4/docs/faq.md?plain=1#L62) to expose Ollama server. Then run this command:

```zsh
docker run -d -p 8080:8080 -v ollama:/root/.ollama -v open-webui:/app/backend/data --name open-webui --restart always [IMAGE]
```

### Add pipelines feature

Check out this [quick-start guide](https://docs.openwebui.com/pipelines/) and see our [Google Cloud cost comparisons](../google-clouds) and deployment steps.

## Other Installation Methods

Checkout Open WebUI official documentation [here](https://docs.openwebui.com/).
