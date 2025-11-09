# Agentic App Summarizer

AI-powered text summarization API using FastAPI and OpenAI GPT-4o.

## Features

- 🤖 **AI Text Summarization** using OpenAI GPT-4o
- 🚀 **FastAPI** backend with automatic API documentation
- 🎨 **Modern Web Interface** with real-time character counting
- 🐳 **Docker** containerized deployment
- ☁️ **AWS ECR** ready for cloud deployment

## Quick Start

1. **Clone the repository:**
   ```bash
   git clone https://github.com/YOUR_USERNAME/agentic-app-summarizer.git
   cd agentic-app-summarizer
   ```

2. **Set up environment variables:**
   ```bash
   cp .env.example .env
   # Edit .env with your actual API keys
   ```

3. **Run with Docker Compose:**
   ```bash
   docker-compose up --build
   ```

4. **Open your browser:**
   - Web Interface: http://localhost:8000
   - API Docs: http://localhost:8000/docs

## Environment Variables

- `OPENAI_API_KEY`: Your OpenAI API key
- `AWS_ACCESS_KEY_ID`: AWS access key (for ECR deployment)
- `AWS_SECRET_ACCESS_KEY`: AWS secret key
- `AWS_REGION`: AWS region (e.g., us-east-2)
- `AWS_ACCOUNT_ID`: Your AWS account ID

## Development

```bash
# Install dependencies
uv sync

# Run locally
uv run --env-file .env uvicorn app.main:app --reload
```

## Deployment

### AWS ECR
```bash
# Build and tag
docker-compose build
docker tag agentic_app-agentic-app-summarizer:latest $AWS_ACCOUNT_ID.dkr.ecr.$AWS_REGION.amazonaws.com/summarizer_app

# Push to ECR
aws ecr get-login-password --region $AWS_REGION | docker login --username AWS --password-stdin $AWS_ACCOUNT_ID.dkr.ecr.$AWS_REGION.amazonaws.com
docker push $AWS_ACCOUNT_ID.dkr.ecr.$AWS_REGION.amazonaws.com/summarizer_app
```

## API Endpoints

- `GET /` - Web interface
- `GET /health` - Health check
- `POST /summarize` - Text summarization
- `GET /docs` - API documentation

## License

MIT License