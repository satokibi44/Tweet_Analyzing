# PBL
## Functional Requirements
### Abstract Functions
#### English
- Function to retrieve messages
- Function to send the retrieved message to the API
- Function to measure the degree of slander
- Function to send the measurement result to slack
- Functionality for slackbot to send warnings
- 
#### 日本語
- メッセージを取得する機能
- APIに取得したメッセージを送る機能
- 誹謗中傷度計測機能
- 測定結果をslackに送る機能
- slackbotが警告を送信する機能
<br>

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
<br>

## Domain Model
### Glossary
- user
- slander
- slander level API
- alert-bot
- slack
- slackAPI
- Bert
<img width="754" alt="Glossary" src="https://user-images.githubusercontent.com/49672556/150481428-891a92ba-f60f-460e-91a7-6652b79012df.png">
<br>

## Usecase Analysis
### Usecase diagram (complete)
<img width="1168" alt="whole use case diagram" src="https://user-images.githubusercontent.com/44742053/150332812-72a511d0-2d0a-4422-93b1-66ff89f11ad2.png">
<br>

### 1. メッセージを取得する機能 Function to retrieve messages
- Basic Course:
  - slackAPIが指定のチャンネルに送信されたメッセージを検知 slackAPI detects a message sent to a specified channel.
  - 送信されたメッセージを取得する Retrieve the message that was sent.
- Alternative Course:
  - メッセージの取得に失敗 Failed to retrieve message.
  - 再び取得を試みて、それでも取得できなければ終了 Try to get it again, and if you still can't get it, quit.
  - 運営に報告メッセージを送信する Send a report message to the management

#### Usecase diagram
<img width="500" alt="retrieve messages" src="https://user-images.githubusercontent.com/49672556/150351422-99471718-1f96-4b57-a0fa-a71d1f744449.png" title="usecase diagrams">

#### Robustness diagram
<img width="500" alt="retrieve messages" src="https://user-images.githubusercontent.com/49672556/150351699-41439953-1e79-4684-9696-d271492a4a7c.png" title="Robustness diagrams">
<br>

### 2. APIに取得したメッセージを送る機能 Function to send the retrieved message to the API
- Basic Course:
  - Send the retrieved message to the API
- Alternative Course:
  - Fail to send the retrieved message to the API.

#### Usecase diagram
<img width="500" alt="send the retrieved message to the API" src="https://user-images.githubusercontent.com/46553513/150320031-4710bf69-8a76-41d9-92e0-8416cb2a427d.jpg" title="usecase diagrams">

#### Robustness diagram
<img width="500" alt="send the retrieved message to the API" src="https://user-images.githubusercontent.com/46553513/150321960-16435812-dd09-41cb-aa88-5925023b863a.png" title="Robustness diagrams">
<br>

### 3. 誹謗中傷度計測機能 Function to measure the degree of slander
- Basic Course:
  - メッセージを受け取る Receive a message.
  - メッセージを形態素解析する Analyze the message using morphological analysis.
  - 学習したBertに形要素解析したメッセージを入力し、誹謗中傷度を推定する Input the morphological-analyzed message to the learned Bert, and estimate the degree of slander.
  - 学習したBertが誹謗中傷度を出力する The learned Bert outputs the slander level.
  - 誹謗中傷度を返す Return the slander level.
- Alternative Course:
  - Bertでの誹謗中傷度の算出に時間がかかり、エラーになればtime outのエラーを出力する It takes time for Bert to calculate the slander level, and if an error occurs, it outputs a timeout error.

#### Usecase diagram
<img width="975" alt="Function to measure the degree of slander" src="https://user-images.githubusercontent.com/44742053/150331774-fffed794-f1f3-494f-ace0-b401cafb5a6a.png">

#### Robustness diagram
<img width="859" alt="スクリーンショット 2022-01-20 16 46 43" src="https://user-images.githubusercontent.com/52820882/150295403-6c4723be-15ad-4e4b-8986-e3468e4e4a74.png" title="Robustness diagrams">
<br>

### 4. 測定結果をslackに送る機能 Function to send the measurement result to slack
- Basic Course:
  - After measuring the degree of slander, the user can receive a measurement result in slack sent by slack bot.
- Alternative Course:
  - If the message is not slander, the user receives nothing in slack.

#### Usecase diagram
<img width="622" alt="Function to send the measurement result to slack" src="https://user-images.githubusercontent.com/44742053/150313404-1a9ad098-962c-4d88-8087-3c808f577cdd.png">

#### Robustness diagram
<img width="500" alt="robustness" src="https://user-images.githubusercontent.com/44742053/150320148-e41d4eb5-a0ed-403e-9b6f-5afc96b782ad.png">
<br>

### 5. slackbotが警告を送信する機能 Function for slackbot to send warnings
- Basic Course:
  - slack botが警告メッセージを送ることに成功する. slack bot succed to send warning message to slack.
  - slackがbotから送られたメッセージを表示する. slack display message which slack bot send.
- Alternative Course:
  - slack botが警告メッセージを送ることに失敗(成功したというresponseがかえってこない). slack bot fail to send warning message to slack.(slack bot can’t get response of success from slack)
  - 4回までretryする slack bot retry to send message up to 4 times.
  - 4回失敗した場合、終了する. When slack bot fails 4 times to retry, slack bot stops sending messages.

#### Usecase diagram
<img width="500" alt="スクリーンショット 2022-01-19 4 58 14" src="https://user-images.githubusercontent.com/53958213/150278545-29d1fa59-5431-4907-9515-66a6b78d0a76.png">

#### Robustness diagram
<img width="500" alt="スクリーンショット 2022-01-19 4 58 14" src="https://user-images.githubusercontent.com/53958213/150310907-6b7b12d9-4a76-4c9d-b849-e50ce9771fa2.jpeg">

### Sequence diagram
<img width="800" alt="スクリーンショット 2022-01-27 19 13 54" src="https://user-images.githubusercontent.com/53958213/151343377-3a68ff5e-0cf2-4996-8099-9ea98f3c5fca.png">

### Class diagram
<img width="800" alt="スクリーンショット 2022-01-27 19 43 19" src="https://user-images.githubusercontent.com/53958213/154631280-12d03e3a-f553-46d1-91c7-53d322560d7e.png">

