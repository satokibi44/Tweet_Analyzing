# PBL

## Functional Requirements

### Abstract Functions

#### English
- Function to retrieve messages
- Function to send the retrieved message to the API
- Function to measure the degree of slander
- Function to send the measurement result to slack
- Functionality for slackbot to send warnings

#### 日本語
- メッセージを取得する機能
- APIに取得したメッセージを送る機能
- 誹謗中傷度計測機能
- 測定結果をslackに送る機能
- slackbotが警告を送信する機能

### Specific Functions

#### English
- User can send messages in Slack, the alert-bot can check whether it is a slanderous message based on slander level.
- When a slanderous message is sent, the alert-bot sends a warning message.
- The number of slanderous messages is counted, and if a message is slandered more than five times in a week, for example, the user is warned.
- This is how I envision an alert-bot that can be used for self-improvement.
- Warning against slander in the form of an alert-bot in slack.
- we can have some emoji to alert if one sends slander.
- Using a deep learning model to calculate the slander level of a message.
- If the slander score is 0.6 or higher, the alert-bot will send a warning to the person who sent the slander.
- When the slack alert-bot receives a message from the slack channel, it posts the message to the slander API and receives a score 


#### 日本語

- 誹謗中傷のメッセージが送信されると、ボットは警告メッセージを送信します。
- 誹謗中傷の回数をカウントし、例えば1週間に5回以上誹謗中傷された場合は警告を表示します。
- このように、自己啓発に活用できるbotをイメージしています。
- slackにbotという形で誹謗中傷に対する警告を行う。
- 誹謗中傷があったら、絵文字で警告するようにしてもいい。
- ディープラーニングモデルを使って、メッセージの誹謗中傷レベルを計算する。
- 誹謗中傷のスコアが0.6以上の場合、ボットは誹謗中傷を送った人に警告を送ります。
- slack botがslackのチャンネルからメッセージを受け取ると、誹謗中傷APIにメッセージをPOSTしてスコアを受け取る
- 誹謗中傷が一定期間発生しなかった場合のご褒美機能（今から具体化します）

## Domain Model
### Glossary
- user
- slander
- slander level
- slander level API
- alert-bot
- slack

<img width="1168" alt="スクリーンショット 2022-01-14 14 53 29" src="https://user-images.githubusercontent.com/53958213/149458720-3f6e38e4-9ae8-4281-a4ca-9ccbb8ed6116.png">

