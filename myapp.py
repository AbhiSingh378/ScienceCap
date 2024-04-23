import streamlit as st
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
import pickle

# Load the trained model and vectorizer
model = pickle.load(open('model.pkl', 'rb'))
vectorizer = pickle.load(open('vectorizer.pkl', 'rb'))

def predict_emotion(text):
    text_vec = vectorizer.transform([text])
    prediction = model.predict(text_vec)[0]
    return prediction

def main():
    st.set_page_config(page_title="Emotion Detection", page_icon=":guardsman:", layout="wide")
    
    # Add a title and description with emojis
    st.title("Emotion Detection App :robot_face:")
    st.write("Enter a sentence or select one from the sample sentences to predict the underlying emotion. :speech_balloon:")
    
    # Create a container for the input section
    with st.container():
        st.write("---")
        left_column, right_column = st.columns(2)
        
        with left_column:
            # Add a dropdown to select sample sentences
            sample_sentences = [
                "I don't have any strong feelings about the situation. It's just another ordinary day, and I'm pretty neutral about it.",
                "I can't believe this is happening. I feel so sad and heartbroken. It's like my world is falling apart. :cry:",
                "I'm so angry right now! How could they do this to me? I can't stand this injustice! :angry:",
                "I'm really worried about the upcoming exam. I don't know if I've prepared enough, and I'm afraid of failing. :worried:"
            ]
            selected_sentence = st.selectbox("Select a sample sentence", [""] + sample_sentences)
            
            # Update the text input with the selected sentence
            text = st.text_area("Enter your text or select a sample sentence", value=selected_sentence, height=200)
        
        with right_column:
            st.write("##")
            st.write("Click the button below to predict the emotion.")
            
            # Add a button to predict the emotion with an emoji
            if st.button("Predict Emotion :mag_right:"):
                if text:
                    emotion = predict_emotion(text)
                    st.success(f"Predicted Emotion: {emotion} :smile:")
                else:
                    st.warning("Please enter some text or select a sample sentence. :exclamation:")
    
    # Add a section for user feedback
    st.write("---")
    st.header("Feedback :memo:")
    feedback = st.text_input("Please provide your feedback or suggestions:")
    if st.button("Submit Feedback"):
        if feedback:
            st.success("Thank you for your feedback! We appreciate your input. :pray:")
        else:
            st.warning("Please enter your feedback before submitting. :exclamation:")
    
    # Add a footer with emojis
    st.write("---")
    st.write("Created by Abhishek Singh and Adarsh Pathak ")

if __name__ == '__main__':
    main()