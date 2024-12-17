# GitHub Issues WordCloud

## 📄 概要
**GitHub Issues WordCloud** は、GitHubのIssuesを取得し、  
形態素解析エンジン **MeCab** を使用して **日本語ワードクラウド** を生成するツールです。

- GitHub Issuesからデータを取得
- MeCabで名詞を抽出
- 外部ストップワードファイルを活用し、不要な単語を除外
- 日本語フォントをサポート

---

## 🛠️ 使用方法

### 1. 環境構築

**必要なライブラリ** をインストールします：

```bash
brew install mecab
brew install mecab-ipadic
pip install requests mecab-python3 wordcloud matplotlib
```

---

### 2. ストップワードの確認

本リポジトリには **`stopwords.txt`** が含まれています。  
このファイルには、ワードクラウド生成時に除外する単語が記述されています。  
必要に応じて `stopwords.txt` を編集してください。

---

### 3. プログラムの実行

以下のコマンドでワードクラウドを生成します：

```bash
python3 wordcloud_github_mecab.py
```

---

### 4. 出力結果

- 生成されたワードクラウド画像が表示されるので適宜保存してください。  
- 不要な単語（ストップワード）が除外され、日本語の名詞が中心のワードクラウドが表示されます。

---

## ⚙️ カスタマイズ

### GitHubリポジトリの設定  
対象のGitHubリポジトリは、以下のコードで設定可能です：

```python
OWNER = "リポジトリのオーナー名"
REPO = "リポジトリ名"
```

### ストップワードの編集  
リポジトリ内の **`stopwords.txt`** ファイルを編集することで、除外する単語を自由にカスタマイズできます。

---

## 🔧 動作環境

- Python 3.8 以上
- MacOS / Linux（MeCabが動作する環境）

---

## 📷 スクリーンショット

![WordCloud Example](Figure_1.png)

---

## 💡 参考

- [MeCab - 形態素解析エンジン](https://taku910.github.io/mecab/)
- [WordCloudライブラリ](https://github.com/amueller/word_cloud)
- [GitHub API ドキュメント](https://docs.github.com/en/rest)
