# main.py
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.spinner import Spinner
from kivy.uix.label import Label
from kivy.core.audio import SoundLoader
from kivy.clock import Clock
import edge_tts
import asyncio
import os
from functools import partial

# Voice options dictionary
VOICES = {
    'Emma (US)': 'en-US-EmmaNeural',
    'Jenny (US)': 'en-US-JennyNeural',
    'Guy (US)': 'en-US-GuyNeural',
    'Aria (US)': 'en-US-AriaNeural',
    'Davis (US)': 'en-US-DavisNeural',
    'Jane (UK)': 'en-GB-SoniaNeural',
    'Ryan (UK)': 'en-GB-RyanNeural',
    'Swara (Hindi)': 'hi-IN-SwaraNeural',
    'Madhur (Hindi)': 'hi-IN-MadhurNeural',
    'Pallavi (Tamil)': 'ta-IN-PallaviNeural',
    'Valluvar (Tamil)': 'ta-IN-ValluvarNeural'
}

class TTSConverter(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = 20
        self.spacing = 10
        
        # Title
        self.add_widget(Label(
            text='Text to Speech Converter',
            size_hint_y=None,
            height=50,
            font_size='20sp'
        ))
        
        # Voice selection
        self.voice_spinner = Spinner(
            text='Select Voice',
            values=list(VOICES.keys()),
            size_hint_y=None,
            height=50
        )
        self.add_widget(self.voice_spinner)
        
        # Text input
        self.text_input = TextInput(
            hint_text='Enter text here...',
            multiline=True,
            size_hint_y=None,
            height=200
        )
        self.add_widget(self.text_input)
        
        # Convert button
        self.convert_btn = Button(
            text='Convert to Speech',
            size_hint_y=None,
            height=50,
            background_color=(0.2, 0.6, 1, 1)
        )
        self.convert_btn.bind(on_press=self.convert_text)
        self.add_widget(self.convert_btn)
        
        # Status label
        self.status_label = Label(
            text='',
            size_hint_y=None,
            height=30
        )
        self.add_widget(self.status_label)
        
        # Play button (initially hidden)
        self.play_btn = Button(
            text='Play Audio',
            size_hint_y=None,
            height=50,
            background_color=(0.2, 1, 0.2, 1),
            opacity=0,
            disabled=True
        )
        self.play_btn.bind(on_press=self.play_audio)
        self.add_widget(self.play_btn)
        
        self.sound = None
        self.current_audio_file = None

    async def generate_speech(self, text, voice):
        try:
            # Generate unique filename
            self.current_audio_file = 'output.mp3'
            if os.path.exists(self.current_audio_file):
                os.remove(self.current_audio_file)
                
            communicate = edge_tts.Communicate(text, voice)
            await communicate.save(self.current_audio_file)
            return True
        except Exception as e:
            print(f"Error generating speech: {e}")
            return False

    def convert_text(self, instance):
        if not self.text_input.text.strip():
            self.status_label.text = 'Please enter some text'
            return
            
        if self.voice_spinner.text == 'Select Voice':
            self.status_label.text = 'Please select a voice'
            return
            
        self.convert_btn.disabled = True
        self.status_label.text = 'Converting...'
        
        # Get selected voice
        voice_name = self.voice_spinner.text
        voice_id = VOICES[voice_name]
        
        # Run async conversion
        async def run_conversion():
            success = await self.generate_speech(self.text_input.text, voice_id)
            Clock.schedule_once(lambda dt: self.conversion_complete(success))
            
        asyncio.run(run_conversion())

    def conversion_complete(self, success):
        self.convert_btn.disabled = False
        if success:
            self.status_label.text = 'Conversion successful!'
            self.play_btn.opacity = 1
            self.play_btn.disabled = False
        else:
            self.status_label.text = 'Conversion failed'
            self.play_btn.opacity = 0
            self.play_btn.disabled = True

    def play_audio(self, instance):
        if self.sound:
            self.sound.stop()
            self.sound.unload()
        
        if self.current_audio_file and os.path.exists(self.current_audio_file):
            self.sound = SoundLoader.load(self.current_audio_file)
            if self.sound:
                self.sound.play()

class TTSApp(App):
    def build(self):
        return TTSConverter()

if __name__ == '__main__':
    TTSApp().run()
