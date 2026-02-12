from locust import HttpUser, task, between

class HammerVoiceSimulator(HttpUser):
    wait_time = between(0.5, 1.5) # Simulates rapid-fire call arrivals

    @task
    def simulate_voice_call(self):
        """Simulates an IVR system sending a voice-to-text string to the backend."""
        # This mimics what Hammer does: hitting the API with 'Speech' data
        self.client.post("/ivr/v1/process_speech", json={
            "audio_transcription": "I want to speak to a nurse",
            "call_id": "CALL_998877",
            "caller_region": "MI"
        }, name="IVR Voice Call Simulation")