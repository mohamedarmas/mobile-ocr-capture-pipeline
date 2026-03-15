from azure.ai.formrecognizer import DocumentAnalysisClient
from azure.core.credentials import AzureKeyCredential

#**** IMPORTANT NOTE ****

#This is a demo function to simulate OCR response. In production, you would replace this with actual calls to Azure's OCR service.

# def extract_text_from_image(image_path, endpoint, api_key):

#     print("Sending image to Azure OCR...")
#     print("Simulating OCR response")

#     demo_text = [
#         "Login",
#         "Username",
#         "Password",
#         "Sign In"
#     ]

#     return "\n".join(demo_text)



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