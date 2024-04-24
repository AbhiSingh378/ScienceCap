import streamlit as st
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(feedback):
    # Email configuration
    sender_email = "your_email@example.com"
    sender_password = "your_email_password"
    recipient_email = "Singh.abhishek3@northeastern.edu"

    # Create a multipart message
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = recipient_email
    message["Subject"] = "Feedback from Emotion Detection App"

    # Add the feedback as the email body
    body = f"Feedback:\n{feedback}"
    message.attach(MIMEText(body, "plain"))

    try:
        # Create a secure SSL/TLS connection
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        
        # Login to the email account
        server.login(sender_email, sender_password)
        
        # Send the email
        server.send_message(message)
        
        print("Email sent successfully!")
    except Exception as e:
        print("An error occurred while sending the email:", str(e))
    finally:
        # Close the SMTP connection
        server.quit()

def app():
    st.title("About Emotion Detection")
    
    st.header("What is Emotion Detection?")
    st.write("Emotion detection is the process of identifying and analyzing human emotions from text data. In this project, we have developed an algorithm that can automatically detect the emotional sentiment expressed in a given piece of text.")
    st.image("Emotion.jpg", caption="Emotion Detection", use_column_width=True)
    
    st.header("Why Emotion Detection?")
    st.write("Emotion detection has various applications and benefits, including:")
    st.write("- Understanding customer sentiment in business settings")
    st.write("- Analyzing user reactions to products or services")
    st.write("- Enhancing human-computer interaction by providing personalized experiences")
    st.write("- Assisting in mental health assessment and therapy")
    
    st.header("Dataset")
    st.write("The emotion detection algorithm uses the 'emotion_sentimen_dataset.csv' dataset, which contains text data labeled with corresponding emotions.")
    
    st.header("Data Exploration")
    st.write("We explore the dataset using various Pandas functions to understand its structure and content. This includes checking the head and tail of the dataset, examining the columns, checking for missing values, describing the dataset's statistics, and visualizing the distribution of emotions using countplots.")
    
    st.header("How Our Algorithm Works")
    st.write("Our emotion detection algorithm follows these key steps:")
    
    with st.expander("Data Preprocessing"):
        st.write("Before training the model, we preprocess the text data using the following steps:")
        st.write("1. Removing HTML tags and unwanted characters using BeautifulSoup.")
        st.write("2. Applying stemming to reduce words to their base or root form using NLTK's PorterStemmer.")
        st.write("3. Removing stopwords (common words like 'the', 'is', 'and') using NLTK's stopwords corpus and ToktokTokenizer.")
    
    with st.expander("Feature Extraction"):
        st.write("We convert the preprocessed text data into numerical features using two approaches:")
        st.write("1. Bag-of-Words (BoW): We use CountVectorizer to create a matrix where each column represents a unique word, and each row represents a text sample. The values in the matrix indicate the frequency of each word in the corresponding text sample.")
        st.write("2. TF-IDF: We use TfidfVectorizer to create a similar matrix, but the values are weighted by the term frequency-inverse document frequency (TF-IDF) scheme. This helps to highlight important words while downscaling common words.")
    
    with st.expander("Model Training and Evaluation"):
        st.write("We split the dataset into training and testing sets using the `train_test_split()` function from scikit-learn. We then initialize a Logistic Regression model and train it on the training data using the `fit()` function.")
        st.write("We evaluate the trained model's performance on the test data by making predictions and calculating the accuracy and classification report using scikit-learn's `accuracy_score()` and `classification_report()` functions.")
    
    with st.expander("Prediction on New Text"):
        st.write("To make predictions on new text data, we first preprocess the text using the same steps as before. We then transform the preprocessed text into numerical features using the trained vectorizer. Finally, we pass the features to the trained model to obtain the predicted emotion.")
    
    with st.expander("Model Persistence"):
        st.write("We save the trained model and the vectorizer using the `pickle` library. This allows us to load the model and vectorizer later for making predictions without retraining the model.")
    
    st.header("Applications of Emotion Detection")
    st.write("Emotion detection has a wide range of applications across different domains, such as:")
    
    applications = {
        "Customer Service": "Analyzing customer feedback and sentiment to improve customer satisfaction and support.",
        "Marketing": "Understanding audience reactions to marketing campaigns and adjusting strategies accordingly.",
        "Social Media": "Monitoring social media sentiment to gauge public opinion and track brand reputation.",
        "Healthcare": "Assisting in mental health assessment and providing personalized emotional support."
    }
    
    selected_application = st.selectbox("Select an application", list(applications.keys()))
    st.write(applications[selected_application])
    
    st.header("Benefits of Using Our Algorithm")
    st.write("By utilizing our emotion detection algorithm, you can:")
    st.write("- Gain valuable insights into customer or user emotions and preferences")
    st.write("- Make data-driven decisions to improve products, services, and user experiences")
    st.write("- Automate sentiment analysis tasks and save time and resources")
    st.write("- Enhance human-computer interaction by providing emotionally intelligent responses")
    
    st.header("Get Started")
    st.write("To start using our emotion detection algorithm, follow these steps:")
    st.write("1. Prepare your text data in a compatible format (CSV file)")
    st.write("2. Preprocess the text data using the provided functions")
    st.write("3. Train the emotion detection model using the preprocessed data")
    st.write("4. Use the trained model to predict emotions on new text data")
    st.write("5. Integrate the emotion predictions into your applications or decision-making processes")
    
    st.write("Feel free to explore the code and dataset in this repository to understand the implementation details.")
    
    st.write("---")
    st.header("Feedback :memo:")
    feedback = st.text_input("Please provide your feedback or suggestions:")
    if st.button("Submit Feedback"):
        if feedback:
            send_email(feedback)
            st.success("Thank you for your feedback! We appreciate your input. :pray:")
        else:
            st.warning("Please enter your feedback before submitting. :exclamation:")