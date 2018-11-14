# Content-Type

### Content-Type とは

`Content-Type` とはリソースのメディア種別(画像や音声など)を示すために使用されます。
これからどのようなファイルを送るのかファイル名や拡張子からではファイルの種類が把握できないことがあります。 しかし、Content-Type を指定することで  ファイルを受け取る側がとのような種類のファイルか把握することが可能になります。(Content-Type が間違っている場合や Content-Type が脆弱性の原因になる場合もあります)

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

- [MDN web docs](https://developer.mozilla.org/ja/docs/Web/HTTP/Headers/Content-Type)
- [Wikipedia メディアタイプ](https://ja.wikipedia.org/wiki/%E3%83%A1%E3%83%87%E3%82%A3%E3%82%A2%E3%82%BF%E3%82%A4%E3%83%97#%E4%B8%BB%E3%81%AA%E4%BE%8B)
