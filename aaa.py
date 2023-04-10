from boxsdk import CCGAuth, Client

# 認証情報を設定
auth = CCGAuth(
  client_id="ifxgm52f01bb8j8te4h2tv6lmo4xlw4r",
  client_secret="A5laygJ3jqXCIUH5NXnMjus3euMKM1Bc",
  access_token='9ggVFmR4Ovi1rBjdqDHOu8Ji8kHKyh6p'
)

client = Client(auth)

new_folder = client.folder('202361405223').create_subfolder('New Folder Name')