THE IDOLM@STER CINDERELLA GIRLS IDOL DATA API
===============
[発揮値計算機](https://github.com/zaubermaerchen/imas_cg_live_calc)で利用するアイドルのステータスやスキルの効果等のデータを取得する為のAPIです。

必要ミドルウェア・ライブラリ
---------------
* Python >= 2.7.7
* MariaDB >= 10.0.15(or MySQL >= 5.5.41)
* Memcached >= 1.4.21
* libMemcached >= 1.0.18

必要Pythonライブラリ
---------------
* Django >= 1.7.1
* MySQL-python >= 1.2.5
* pylibmc >= 1.4.1
* simplejson >= 3.6.5
* django-pylibmc >= 0.5.0
* simplejson >= 3.6.5

ローカル環境での起動手順
---------------
1. 必要ミドルウェア・ライブラリ、必要Pythonライブラリをインストールする
1. DBに[最新のデータ](http://www4018uf.sakura.ne.jp/imas_cg/data/imas_cg_api.sql)を登録する
1. プロジェクトのルートディレクトリで「python manage.py runserver 8000」を実行してサーバーを起動する
1. 「http://localhost:8000/imas_cg/api/admin/」にアクセスして管理画面にアクセスできるか確認する

APIリファレンス
---------------
### アイドルデータAPI
#### URL
/imas_cg/api/idol/list/

#### リクエストパラメータ

|パラメータ|項目名|必須|備考|
|---|---|---|---|
|type|属性| |0:キュート 1:クール 2:パッション|
|rarity|レアリティ| |0:ノーマル 1:ノーマル+ 2:レア 3:レア+ 4:Sレア 5:Sレア+|
|fields|取得パラメータ| |半角スペース区切りで取得したいレスポンスパラメータ名を記述|

#### レスポンスパラメータ

    {
        "1500111": {
            "idol_id": 1500111, 
            "name": "[普通の女の子]天海春香+", 
            "type": 0, 
            "rarity": 5, 
            "cost": 10, 
            "offense": 2784, 
            "defense": 2784, 
            "max_defense": 8704, 
            "max_offense": 8704, 
            "skill_id": 101070003, 
            "skill_name": "THE☆王道", 
            "hash": "e7fe451b0e7483323d10d1c8b038bf94" 
        },
    }

|パラメータ|項目名|備考|
|---|---|---|---|
|idol_id|アイドルID| |
|name|アイドル名| |
|type|属性|0:キュート 1:クール 2:パッション|
|rarity|レアリティ|0:ノーマル 1:ノーマル+ 2:レア 3:レア+ 4:Sレア 5:Sレア+|
|cost|コスト| |
|offense|初期攻めアピール力| |
|defense|初期守りアピール力| |
|max_offense|最大攻めアピール力| |
|max_defense|最大守りアピール力| |
|skill_id|スキルID| |
|skill_name|スキル名| |
|hash|ハッシュ|画像ファイル名|

### スキルデータAPI
#### URL
/imas_cg/api/skill/list/

#### リクエストパラメータ
なし

#### レスポンスパラメータ

    {
        "100000001": {
            "skill_id": 100000001,
            "target_unit": 0,
            "target_member": 0,
            "target_type": 7,
            "target_num": -1,
            "target_param": 0,
            "skill_value_id": 13,
            "skill_value_list": [40, 45, 50, 55, 60, 65, 70, 75, 80, 90, 91, 92],
            "comment": "自分の攻守 中アップ",
        },
    }

|パラメータ|項目名|備考|
|---|---|---|---|
|skill_id|スキルID| |
|target_unit|対象ユニット|0:自ユニット 1:相手ユニット|
|target_member|対象メンバー|0:自分 1:フロントメンバー 2:バックメンバー 3:フロント・バックメンバー|
|target_type|対象属性|1:キュート 2:クール 3:キュート/クール 4:パッション 5:キュート/パッション 6:クール/パッション 7:全属性|
|target_num|対象バックメンバー数| |
|target_param|対象ステータス|0:攻守 1:攻 2:守|
|skill_value_id|スキル効果ID| |
|skill_value_list|スキル効果量|スキルレベルごとの効果量|
|comment|スキル効果概要| |