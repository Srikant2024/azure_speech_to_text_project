import azure.cognitiveservices.speech as speechsdk

# Replace with your Azure Speech Service key and region
subscription_key = "00ec1686e9f84998949ebaba5b697005"
region = "eastus2"

def text_to_speech(text, output_file):
    # Create a speech configuration with your subscription key and region
    speech_config = speechsdk.SpeechConfig(subscription=subscription_key, region=region)

    # Set the output format to MP3 (if available)
    speech_config.speech_synthesis_output_format = speechsdk.SpeechSynthesisOutputFormat.Audio16Khz32KBitRateMonoMp3

    # Create audio configuration
    audio_config = speechsdk.audio.AudioOutputConfig(filename=output_file)

    # Create a speech synthesizer
    synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=audio_config)

    # Synthesize the text to speech
    result = synthesizer.speak_text(text)

    # Check result
    if result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
        print(f"Successfully synthesized the text to {output_file}.")
    elif result.reason == speechsdk.ResultReason.Canceled:
        cancellation_details = speechsdk.SpeechSynthesisCancellationDetails.from_result(result)
        print(f"Speech synthesis canceled: {cancellation_details.reason}")
        print(f"Error details: {cancellation_details.error_details}")

# Example usage
text = "Hello, this is a sample text to speech conversion using Azure."
output_file = "output.mp3"
text_to_speech(text, output_file)
