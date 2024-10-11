import streamlit as st
from langchain.prompts import PromptTemplate
from langchain.llms import CTransformers

## Function to get the response from the LLM model
def get_response(input_text, words, blog_style):
    llm = CTransformers(model="model\llama-2-7b-chat.ggmlv3.q8_0.bin",
                        model_type='llama',
                        config={'max_new_tokens': 256,
                                'temperature': 0.01})
    
    ## Prompt Template
    template = """
    Write a blog for {blog_style} job profile on the topic "{input_text}" within {words} words.
    """
    
    prompt = PromptTemplate(input_variables=["blog_style", "input_text", "words"], template=template)
    
    ## Generate the response
    formatted_prompt = prompt.format(blog_style=blog_style, input_text=input_text, words=words)
    response = llm(formatted_prompt)  # Adjust this line according to how CTransformers expects input
    
    print(response)  # This will print the response in the terminal
    return response

## Streamlit Config
st.set_page_config(page_title="Generate Blogs",
                   page_icon="🐤",
                   layout="centered",
                   initial_sidebar_state="collapsed")

## Streamlit App Interface
st.header("Generate Blog 🐤")

input_text = st.text_input("Enter the blog topic")
col1, col2 = st.columns([5, 5])

with col1:
    words = st.text_input('Number of words')
    
with col2:
    blog_style = st.selectbox('Writing the blog for:',
                              ('Researcher',
                               'Data scientist',
                               'Common people'), index=0)

submit = st.button("Generate")

if submit:
    if input_text and words:
        st.write(get_response(input_text, words, blog_style))
    else:
        st.error("Please fill out both the blog topic and number of words.")
