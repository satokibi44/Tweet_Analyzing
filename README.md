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
- Warning against slander in the form of an alert-bot in slack.
- we can have some emoji to alert if one sends slander.
- Using a deep learning model to calculate the slander level of a message.
- If the slander score is 0.6 or higher, the alert-bot will send a warning to the person who sent the slander.


#### 日本語

- 誹謗中傷のメッセージが送信されると、ボットは警告メッセージを送信します。
- 誹謗中傷の回数をカウントし、例えば1週間に5回以上誹謗中傷された場合は警告を表示します。
- slackにbotという形で誹謗中傷に対する警告を行う。
- 誹謗中傷があったら、絵文字で警告するようにしてもいい。
- ディープラーニングモデルを使って、メッセージの誹謗中傷レベルを計算する。
- 誹謗中傷のスコアが0.6以上の場合、ボットは誹謗中傷を送った人に警告を送ります。
- 誹謗中傷が一定期間発生しなかった場合のご褒美機能（実装するかは不明）

## Domain Model
### Glossary
- user
- slander
- slander level API
- alert-bot
- slack


<img width="1328" alt="スクリーンショット 2022-01-19 4 31 42" src="https://user-images.githubusercontent.com/53958213/150005830-d0136bf5-10b1-4f1c-b7c2-6fad8426939b.png">


## Usecase Analysis

### メッセージを取得する機能 Function to retrieve messages
- Basic Course
  - slackAPIが指定のチャンネルに送信されたメッセージを検知 slackAPI detects a message sent to a specified channel.
  - 送信されたメッセージを取得する Retrieve the message that was sent.
- Alternative Course
  - メッセージの取得に失敗 Failed to retrieve message.
  - 再び取得を試みて、それでも取得できなければ終了 Try to get it again, and if you still can't get it, quit.
  - 運営に報告メッセージを送信する Send a report message to the management.
<br>

### APIに取得したメッセージを送る機能 Function to send the retrieved message to the API
- Basic Course:
  - Retrieving the message using function to retrieve message.
  - Send the message to the API successfully. 
- Alternative Course:
  - Not retrieved messages fail to send the message to the API.
<br>


### 誹謗中傷度計測機能 Function to measure the degree of slander
- Basic
  - Receive a message.
  - Analyze the message using form factors.
  - Input the form-factor-analyzed message to the learned Bert, and estimate the degree of slander.
  - The learned Bert outputs the slander level.
  - Return the slander level.
- Alternative Course
  - It takes time for Bert to calculate the slander level, and if an error occurs, it outputs a timeout error.

- Basic
  - メッセージを受け取る。
  - メッセージを形要素解析する。
  - 学習したBertに形要素解析したメッセージを入力し、誹謗中傷度を推定する。
  - 学習したBertが誹謗中傷度を出力する。
  - 誹謗中傷度を返す。
- Alternative Course
  - Bertでの誹謗中傷度の算出に時間がかかり、エラーになればtime outのエラーを出力する。
<br>
<img width="500" alt="スクリーンショット 2022-01-20 16 03 20" src="https://user-images.githubusercontent.com/52820882/150290007-679aa353-a3e4-4902-b6b7-dbb36b0e06cf.png">

### Function to send the measurement result to slack
- Basic Course:
  - After measuring the degree of slander, the user can receive a measurement result in slack sent by slack bot.
- Alternative Course:
  - If the message is not slander, the user receives nothing in slack.
<br>


### slackbotが警告を送信する機能 Function for slackbot to send warnings
- Basic Course:
  - slack botが警告メッセージを送ることに成功する. slack bot succed to send warning message to slack.
  - slackがbotから送られたメッセージを表示する. slack display message which slack bot send.
- Alternative Course:
  - slack botが警告メッセージを送ることに失敗(成功したというresponseがかえってこない). slack bot fail to send warning message to slack.(slack bot can’t get response of success from slack)
  - 4回までretryする slack bot retry to send message up to 4 times.
  - 4回失敗した場合、終了する. When slack bot fails 4 times to retry, slack bot stops sending messages.
<br>
<img width="500" alt="スクリーンショット 2022-01-19 4 58 14" src="https://user-images.githubusercontent.com/53958213/150278545-29d1fa59-5431-4907-9515-66a6b78d0a76.png">


### Usecase diagram
<img width="1690" alt="スクリーンショット 2022-01-19 4 58 14" src="https://user-images.githubusercontent.com/53958213/150009470-562c90bb-88e9-4d0b-aa0b-87a024c58f3e.png">
