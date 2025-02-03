import streamlit as st
#from chatgpt_api import chatgpt_stream_response
from watsonx_api import watsonx_response
#from perplexity_api import perplexity_response
from deepseek_api import deepseek_response
from evaluation import evaluate_response
import json
import plotly.graph_objects as go

# Load predefined queries
with open("queries.json", "r") as file:
    queries = json.load(file)

st.title("🤖 AI Comparison Demo")
st.sidebar.header("Choose a comparison dimension:")
dimension = st.sidebar.selectbox(
    "Select Dimension",
    ["Accuracy", "Creativity", "Speed", "Contextual Understanding", "Bias and Fairness"]
)

prompt = st.text_area("Enter your query:", value="Write a short story about a robot learning to love.")
if st.button("Compare AI Responses"):

    responses = {
        #"ChatGPT": chatgpt_stream_response(prompt),
        "WatsonX": watsonx_response(prompt),
        #"Perplexity": perplexity_response(prompt),
        "DeepSeek": deepseek_response(prompt),
    }

    # Display responses
    for ai, res in responses.items():
        st.subheader(ai)
        st.write(res)

    # Compute scores
    scores = {ai: evaluate_response(res, dimension.lower()) for ai, res in responses.items()}

    # Create radar chart
    fig = go.Figure()
    categories = list(scores.keys())
    values = list(scores.values())
    
    fig.add_trace(go.Scatterpolar(
        r=values + [values[0]],  # Loop back to start
        theta=categories + [categories[0]],
        fill="toself",
        name="AI Performance"
    ))

    fig.update_layout(polar=dict(radialaxis=dict(visible=True)), showlegend=True)
    st.plotly_chart(fig)

st.sidebar.info("AI comparison tool for performance analysis across multiple dimensions.")

#chatgptapi = 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
