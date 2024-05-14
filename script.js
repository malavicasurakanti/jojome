async function synthesizeSpeech() {
    const text = document.getElementById('text-input').value;
    const response = await fetch('/synthesize', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ text: text })
    });

    const data = await response.json();
    const audioBlob = new Blob([new Uint8Array(data.audio)], { type: 'audio/wav' });
    const audioUrl = URL.createObjectURL(audioBlob);
    const audioElement = document.getElementById('audio-output');
    audioElement.src = audioUrl;
    audioElement.play();
}

