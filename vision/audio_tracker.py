import numpy as np
import sounddevice as sd


class AudioTracker:
    def __init__(self, sample_rate: int = 44100, noise_threshold_db: float = 60.0):
        """
        Initializes real-time acoustic signal processing for decibel estimation.
        
        :param sample_rate: Audio sampling frequency in Hz
        :param noise_threshold_db: Threshold above which sound is flagged as high noise
        """
        self.sample_rate = sample_rate
        self.noise_threshold_db = noise_threshold_db

    def process_audio_chunk(self, duration: float = 0.1) -> dict:
        """
        Captures a short audio frame from the microphone and computes sound intensity.
        
        :param duration: Duration in seconds to record per frame processing loop
        :return: Telemetry dictionary with decibel reading and noise detection status
        """
        try:
            # Record a short audio chunk from default microphone
            recording = sd.rec(
                int(duration * self.sample_rate),
                samplerate=self.sample_rate,
                channels=1,
                dtype='float32'
            )
            sd.wait()  # Block until recording finishes

            # Calculate Root Mean Square (RMS) and convert to dB scale
            rms = np.sqrt(np.mean(recording ** 2))
            
            if rms > 0:
                # Approximate dynamic range scaling for standard webcams/microphones
                db_level = round(float(20 * np.log10(rms) + 90), 1)
            else:
                db_level = 0.0

            # Determine anomaly status based on configured threshold
            status = "NORMAL"
            if db_level > self.noise_threshold_db:
                status = "HIGH_NOISE_DETECTED"

            return {
                "db_level": db_level,
                "status": status,
                "is_anomalous": db_level > self.noise_threshold_db
            }

        except Exception as e:
            # Fallback if microphone access fails or device is disconnected
            return {
                "db_level": 0.0,
                "status": "AUDIO_ERROR",
                "error": str(e),
                "is_anomalous": False
            }


# -----------------------------------------------------------------------------
# Standalone Module Test (`python audio/audio_tracker.py`)
# -----------------------------------------------------------------------------
if __name__ == "__main__":
    import time
    
    print("Testing AudioTracker... Speak or make noise into the mic. Press Ctrl+C to stop.")
    tracker = AudioTracker(noise_threshold_db=60.0)

    try:
        while True:
            result = tracker.process_audio_chunk(duration=0.2)
            print(f"Decibels: {result['db_level']} dB | Status: {result['status']}")
            time.sleep(0.1)
        
    except KeyboardInterrupt:
        print("\nAudio test stopped.")