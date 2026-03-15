from azure.ai.formrecognizer import DocumentAnalysisClient
from azure.core.credentials import AzureKeyCredential

def extract_text_from_image(image_path, endpoint, api_key):

    client = DocumentAnalysisClient(
        endpoint=endpoint,
        credential=AzureKeyCredential(api_key)
    )

    with open(image_path, "rb") as f:

        poller = client.begin_analyze_document(
            "prebuilt-read",
            document=f
        )

    result = poller.result()

    lines = []

    for page in result.pages:
        for line in page.lines:
            lines.append(line.content)

    return "\n".join(lines)