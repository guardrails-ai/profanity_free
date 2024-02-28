from profanity_check import predict

# Test with a sample example
# This will load the model (if any) during installation
# instead of during the first run of the application
predict(["This is a test sentence with profanity."])
print("Profanity Check post-installation complete.")
