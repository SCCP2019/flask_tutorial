# HTTP ヘッダー

## HTTP ヘッダーとは

クライアントやサーバーがリクエストやレスポンスで追加情報を渡すための仕組みです。
以下のように構成されています。

```
  ヘッダー名:値(改行なし)
```

ヘッダー名は大文字、小文字を区別しません。

以下の画像のはその一例です(Aizu Online Juduge)

![](./images/http-header.png)

上記画像で `Response Headers` と `Request Headers` に分かれている通りいくつかの分類があります。

- General header
  - リクエスト、レスポンスの両方に適用されるが、最終的に本文で転送されるデータとは関係がない
- Request header
  - 読み込むリソースやクライアント自身に関する情報を持つ
- Response heade
  - レスポンスに関する情報やサーバー自身に関する情報を持つ
- Entity header
  - コンテンツの長さ、 MIME タイプなどエンティティの情報を持つ

例えばログインのための認証やセッション管理などには

- Authorization
  - `Authorization: <type> <credential>`といった形でよく使用されるのは`Authorization: Bearer <token>`
  - ex) `Authorization: Bearer czEyNDAxMTkucGFzc3dvcmQK`
- Cookie
  - `Cookie: <cookie-list>` という構文で書かれます
  - ex) `Cookie: name=value; name2=value2; name3=value3`
- Set-Cookie
  - `Set-Cookie: <cookie-name>=<cookie-value>` という構文で書かれます。
  - ex) `Set-Cookie: name=value; name2=value2; name3=value3`

## Content-Type

### Content-Type とは

`Content-Type` とはリソースのメディア種別(画像や音声など)を示すために使用されます。
これからどのようなファイルを送るのかファイル名や拡張子からではファイルの種類が把握できないことがあります。 しかし、Content-Type を指定することでファイルを受け取る側がとのような種類のファイルか把握することが可能になります。(Content-Type が間違っている場合や Content-Type が脆弱性の原因になる場合もあります)

正しい Content-Type の指定を HTTP ヘッダーに付与することでその種類に応じさまざまな処理を行うことができます。

以下が Content-Type の例です。

| Content-Type           | 何を示すか          |
| ---------------------- | ------------------- |
| text/plain             | テキストファイル    |
| text/csv               | CSV ファイル        |
| text/html              | HTML ファイル       |
| application/javascript | JavaScript ファイル |
| application/json       | JSON ファイル       |
| image/png              | PNG ファイル        |
| image/jpeg             | JPEG ファイル       |

### 参考資料

#### header について

- [MDN web docs](https://developer.mozilla.org/ja/docs/Web/HTTP/Headers)

#### Content-Type について

- [MDN web docs](https://developer.mozilla.org/ja/docs/Web/HTTP/Headers/Content-Type)
- [Wikipedia メディアタイプ](https://ja.wikipedia.org/wiki/%E3%83%A1%E3%83%87%E3%82%A3%E3%82%A2%E3%82%BF%E3%82%A4%E3%83%97#%E4%B8%BB%E3%81%AA%E4%BE%8B)
