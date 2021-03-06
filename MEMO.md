# 請求データプロセス

## 概略

### a.請求データ

1. 請求データの準備通知（各社ごとにメール受信）
2. 請求データのダウンロード -> python + selenium 作成ずみ
3. 請求データの加工(都道府県正規化, 日付正規化, 着店扱い, 着店名から都道府県＋市区町村へ変換) -> 一部 python で実装済み
4. 都道府県・住所が正規化できなかった明細を修正
5. 請求データの local-DB 登録

### b.照合用データ準備

1. AS/400 売上伝票・移動伝票から問番ありのみ loca-DB 登録
2. 1.のデータを問番のパターンと便種を比較して修正
3. DH-BOX 問番データを物件分問番データへ登録
4. 物件データ問番の抜けチェック (物件管理データ等と照合)
5. 物件分問番データ local-DB 登録
6. 西濃実績データから AS/400 売上伝票・移動伝票で問番なしを対象に伝票番号の該当をさがして 1 と同じテーブルへ登録

### a と b の照合、集計

1. a のデータを基準に b のデータを使用してクラス分けを実行 （請求由来元の特定）
2. 集計表（住設分 + 住設以外の都道府県別）、営業所・区分別集計（参考資料・対前年同月対比あり)
3. 請求由来が不明な分を抽出し、調査・修正可能な分は修正
4. 3.で修正が発生した場合は 2.をもう一度実施する
