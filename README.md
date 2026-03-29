# LoLCoachApp

SUP専用・自分専用の League of Legends コーチアプリです。  
Riot API を使って直近の試合データを取得し、戦績の確認やプレイ改善のための分析を行うことを目的としています。

## 目的
既存の統計サイトのような「全体向けの情報」ではなく、  
自分の試合データから改善点を見つける「自分専用コーチ」を作ることを目指しています。

## コンセプト
- SUP専用
- 自分専用
- 段階的に機能追加
- GitHubでバージョン管理しながら開発

## 開発方針
このアプリはバージョンごとに機能を追加していきます。

- ver.1: 直近20試合の取得と一覧表示
- ver.2: 基本統計の表示
- ver.3: 勝ち試合 / 負け試合の比較
- ver.4: コーチコメント生成
- ver.5: 視界分析
- ver.6以降: UI改善、保存機能、公開対応

詳細は `document/versions.md` を参照してください。

## ver.1 の目標
Riot ID を入力すると、直近20試合のうち SUPPORT の試合を取得し、一覧表示できるようにする。

### ver.1 で表示する項目
- 勝敗
- 使用チャンピオン
- K / D / A
- ゲーム時間
- Vision Score
- Wards Placed
- Wards Killed

## 使用技術
### フロントエンド
- HTML
- CSS
- JavaScript

### バックエンド
- Python
- Flask

### 外部API
- Riot API

### 開発管理
- Git
- GitHub

## 想定ディレクトリ構成
```text
LoLCoachApp/
├── README.md
├── requirements.txt
├── .gitignore
├── document/
│   ├── versions.md
│   └── ver1_plan.md
├── app/
│   ├── __init__.py
│   ├── routes.py
│   ├── api/
│   │   └── riot_api.py
│   ├── services/
│   │   └── match_service.py
│   └── utils/
│       └── helpers.py
├── templates/
│   └── index.html
├── static/
│   ├── style.css
│   └── script.js
└── run.py