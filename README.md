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

### env
`_env.py`をコピーして、`env.py`を作成し以下の設定値を更新してください
|設定変数|詳細|
|--|--|
|open_ai_key|`OpenAI`のAPIキー|
|conversations|過去の会話設定。<br/>chatGPTに過去の会話を読み込ませたり、ロールプレイを設定をしたい場合はフォーマットに沿って設定してください|
|byebye|終了する合言葉。<br/>ユーザーがここで設定した言葉を発するとアプリを終了し、今までの会話ログを出力します|

### 起動
`python -m talkGPT`
