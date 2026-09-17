import os
from openai import OpenAI, BadRequestError


def make_client() -> OpenAI:
    resource = os.environ["FOUNDRY_RESOURCE"]
    base_url = f"https://{resource}.openai.azure.com/openai/v1/"

    key = os.environ.get("AZURE_INFERENCE_CREDENTIAL")
    if key:
        return OpenAI(base_url=base_url, api_key=key)

    from azure.identity import DefaultAzureCredential, get_bearer_token_provider
    token_provider = get_bearer_token_provider(
        DefaultAzureCredential(),
        "https://ai.azure.com/.default",
    )
    return OpenAI(base_url=base_url, api_key=token_provider)


def ask(client: OpenAI, deployment: str, prompt: str) -> str:
    try:
        response = client.responses.create(model=deployment, input=prompt)
        return response.output_text
    except BadRequestError as err:
        # Fall back only when the model can't use the Responses API.
        # Any other 400 is a real problem with the request.
        if "not supported" not in str(err).lower():
            raise
    completion = client.chat.completions.create(
        model=deployment,
        messages=[{"role": "user", "content": prompt}],
    )
    return completion.choices[0].message.content
