from ibm_watson import AssistantV2
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

WATSONX_API_KEY = "0ngbmSwNHMNGHXJ3trzaQIJdHZEzhVDCkWifWPQTLQRA"
WATSONX_URL = "https://api.us-east.assistant.watson.cloud.ibm.com/instances/ea028fbb-a1b6-4764-b005-0e7dd04c7248"
WATSONX_ASSISTANT_ID = "4611841a-a8f2-4d13-b2e8-3dcccdaef0eb"
WATSONX_VERSION = "2024-08-25" 
WATSONX_ENVIRONMENT_ID = "d89f3c73-5665-4c8a-acd9-d08322df1654"

authenticator = IAMAuthenticator(WATSONX_API_KEY)
assistant = AssistantV2(version=WATSONX_VERSION, authenticator=authenticator)
assistant.set_service_url(WATSONX_URL)

def create_session():
    try:
        session = assistant.create_session(
            assistant_id=WATSONX_ASSISTANT_ID
        ).get_result()
        return session["session_id"]
    except Exception as e:
        return f"Session Creation Error: {str(e)}"


def watsonx_response(prompt):
    session_id = create_session()
    if "Error" in session_id:
        return session_id  # Return error if session creation fails

    try:
        response = assistant.message(
            assistant_id=WATSONX_ASSISTANT_ID,  # ❌ Remove `environment_id`
            session_id=session_id,
            input={"message_type": "text", "text": prompt},
        ).get_result()

        return response.get("output", {}).get("generic", [{}])[0].get("text", "No response received.")

    except Exception as e:
        return f"WatsonX API Error: {str(e)}"


# Example usage
if __name__ == "__main__":
    session_id = "test-session"  # You can replace this with a dynamically generated session ID
    user_query = "What is WatsonX?"
    
    print("User:", user_query)
    print("WatsonX:", watsonx_response(user_query, session_id))

