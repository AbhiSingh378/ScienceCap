# Emotion Detection App

Welcome to the Emotion Detection App! This interactive web application allows you to predict the underlying emotion in a given text using a trained machine learning model. Whether you want to analyze customer feedback, understand user reactions, or explore the emotional sentiment in social media posts, this app has got you covered.

## Features

- Predict emotions from user-entered text or select from sample sentences
- Interactive user interface with emojis and intuitive design
- Detailed "About" page explaining the emotion detection algorithm and its applications
- User feedback functionality with email notifications

## Demo

Try out the live demo of the Emotion Detection App [here](https://emotioonfinder.streamlit.app/).

## How It Works

The emotion detection algorithm follows these key steps:

1. **Data Preprocessing**: The text data is preprocessed by removing HTML tags, applying stemming, and removing stopwords using NLTK's PorterStemmer and ToktokTokenizer.

2. **Feature Extraction**: The preprocessed text is converted into numerical features using the Bag-of-Words (BoW) and TF-IDF techniques. This helps represent the text data in a format suitable for machine learning.

3. **Model Training and Evaluation**: A Logistic Regression model is trained on the extracted features using scikit-learn. The model's performance is evaluated using accuracy and classification report metrics.

4. **Prediction on New Text**: When a user enters new text, it undergoes the same preprocessing and feature extraction steps. The trained model is then used to predict the emotion expressed in the text.

To learn more about the emotion detection algorithm and its applications, check out the "About" page in the app.

## Installation

To run the Emotion Detection App locally, follow these steps:

1. Clone the repository:
   ```
   git clone https://github.com/AbhiSingh378/ScienceCap.git
   ```

2. Navigate to the project directory:
   ```
   cd emotion-detection-app
   ```

3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Run the Streamlit app:
   ```
   streamlit run myapp.py
   ```

5. Open your web browser and visit `http://localhost:8501` to access the app.

## Feedback

We value your feedback! If you have any suggestions or thoughts about the Emotion Detection App, please use the feedback form provided in the app. Your feedback will be sent directly to our team via email, and we'll do our best to incorporate your suggestions and improve the app.

## Contributing

Contributions are welcome! If you'd like to contribute to the Emotion Detection App, please follow these steps:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/your-feature`)
3. Commit your changes (`git commit -m 'Add your feature'`)
4. Push to the branch (`git push origin feature/your-feature`)
5. Open a pull request

## License

This project is licensed under the [MIT License](LICENSE).

## Contact

If you have any questions or inquiries, feel free to reach out to us:

- Abhishek Singh - [singh.abhishek3@northeastern.com](mailto:singh.abhishek3@northeastern.com)
- Adarsh Pathak - [pathak.ada@northeastern.com](mailto:pathak.ada@northeastern.com)

We hope you find the Emotion Detection App useful and insightful! Happy emotion analysis!