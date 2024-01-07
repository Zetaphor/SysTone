import numpy as np
import pyaudio
import psutil

class OscillatingTone:
    def __init__(self, frequency, sample_rate=44100, amplitude=0.5, base_mod_frequency=8.0, mod_depth=1):
        self.frequency = frequency
        self.sample_rate = sample_rate
        self.amplitude = amplitude
        self.phase = 0

        self.base_mod_frequency = base_mod_frequency
        self.mod_depth = mod_depth

    def get_cpu_load_modulation(self):
        # Fetch the CPU percentage and normalize it between 0.1 and 2.0
        # This will allow mod frequencies between 0.1*base_mod_frequency to 2.0*base_mod_frequency
        return 0.1 + 1.9 * (psutil.cpu_percent() / 100.0)

    def generate_tone(self, duration=1.0):
        t = np.linspace(0, duration, int(self.sample_rate * duration), False)

        # Adjust mod_frequency based on current CPU load
        mod_frequency = self.base_mod_frequency * self.get_cpu_load_modulation()

        tone = self.amplitude * np.sin(2 * np.pi * self.frequency * t + self.phase)

        # Amplitude modulation
        mod_wave = 1 + self.mod_depth * np.sin(2 * np.pi * mod_frequency * t)
        tone = tone * mod_wave

        self.phase += 2 * np.pi * self.frequency * duration
        return tone.astype(np.float32)

def play_oscillating_tone(stream, frequency=440.0, duration=2.0):
    tone_generator = OscillatingTone(frequency)
    try:
        print(f"Playing oscillating tone at {frequency}Hz with {duration}s buffer. Press Ctrl+C to stop.")
        while True:
            samples = tone_generator.generate_tone(duration)
            stream.write(samples.tobytes())
    except KeyboardInterrupt:
        print("\nTone stopped.")

if __name__ == "__main__":
    FREQUENCY = 100.0
    BUFFER_DURATION = 1

    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paFloat32,
                    channels=1,
                    rate=44100,
                    output=True,
                    frames_per_buffer=int(44100 * BUFFER_DURATION))

    play_oscillating_tone(stream, FREQUENCY, BUFFER_DURATION)

    stream.stop_stream()
    stream.close()
    p.terminate()
