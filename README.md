## talkGPT
ユーザーの音声に`VoiceVox`の音声が応答してくれるお遊びアプリ</br>
返答の音声作成に`VoiceVox`が必要なので、<br/>以下からダウンロード・インストールして VoiceVox を起動してからアプリを起動してください
- https://voicevox.hiroshiba.jp/

### Flow
ユーザーの音声
=>
pyaudio
=>
whisper
=>
chatGPT
=>
voicevox
=>
simpleaudio

### 起動
`python -m talkGPT`
