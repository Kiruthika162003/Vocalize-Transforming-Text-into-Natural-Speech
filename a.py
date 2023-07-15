import pyttsx3

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Set properties for the speech
engine.setProperty('rate', 150)  # Speed of speech (words per minute)
engine.setProperty('volume', 0.8)  # Volume level (0.0 to 1.0)

# Get input text from the user
text = input("Enter the text you want to convert to speech: ")

# Convert text to speech
engine.say(text)

# Play the speech
engine.runAndWait()
