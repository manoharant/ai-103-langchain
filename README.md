# Azure OpenAI configuration

Copy `.env.example` to `.env` at the project root and fill in these settings:

```dotenv
AZURE_OPENAI_ENDPOINT=https://<resource>.services.ai.azure.com/openai/v1
AZURE_OPENAI_CHAT_DEPLOYMENT=<chat-deployment-name>
AZURE_OPENAI_API_KEY=<api-key>
```

For `langgraph/cloudxeus_support_agent.py`, also set:

```dotenv
AZURE_OPENAI_EMBEDDING_DEPLOYMENT=<embedding-deployment-name>
```

For `langchain/lanchain_telemetry.py`, also set:

```dotenv
APPLICATIONINSIGHTS_CONNECTION_STRING=<application-insights-connection-string>
```

Use the full OpenAI-compatible `/openai/v1` endpoint. Keep the API key out of
source files and version control. Existing environment variables take precedence
over values in `.env`. Install the project's dependencies before running the examples.