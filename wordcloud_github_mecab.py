import requests
import MeCab
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# GitHubのリポジトリ設定
OWNER = "snakajima"  # リポジトリのオーナー名
REPO = "life-is-beautiful"  # リポジトリ名
GITHUB_API_URL = f"https://api.github.com/repos/{OWNER}/{REPO}/issues"

# 日本語フォント（Mac標準フォント）
FONT_PATH = "/System/Library/Fonts/Supplemental/Arial Unicode.ttf"

def fetch_all_issues():
    """
    GitHub Issuesをページネーションで全件取得する
    """
    issues = []
    page = 1

    while True:
        response = requests.get(GITHUB_API_URL, params={"page": page, "per_page": 100})
        if response.status_code != 200:
            print(f"Error: {response.status_code}")
            break

        page_issues = response.json()
        if not page_issues:  # データが空なら終了
            break

        issues.extend(page_issues)
        page += 1  # 次のページへ

    print(f"合計 {len(issues)} 件のIssueを取得しました。")
    return issues

def mecab_tokenizer(text):
    """
    MeCabを使って名詞のみを抽出する
    """
    mecab = MeCab.Tagger("-Ochasen")
    parsed_text = mecab.parse(text)
    
    words = []
    for line in parsed_text.splitlines():
        if not line.strip():  # 空行をスキップ
            continue
        parts = line.split("\t")
        if len(parts) < 4:  # 要素数が4未満ならスキップ
            continue
        surface, _, _, pos = parts[:4]
        if pos.startswith("名詞"):  # 名詞を対象
            words.append(surface)
    return " ".join(words)

def load_stopwords(file_path):
    """
    外部ファイルからストップワードを読み込む
    """
    with open(file_path, "r", encoding="utf-8") as file:
        stopwords = {line.strip() for line in file if line.strip()}
    print(f"{len(stopwords)} 個のストップワードを読み込みました。")
    return stopwords

def generate_wordcloud(text, stopwords):
    """
    ワードクラウドを生成して表示
    """
    wordcloud = WordCloud(
        width=800,
        height=400,
        background_color='white',
        font_path=FONT_PATH,
        stopwords=stopwords
    ).generate(text)

    # ワードクラウドの表示
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.show()
    wordcloud.to_file("wordcloud_github_mecab.png")
    print("ワードクラウドをwordcloud_github_mecab.pngとして保存しました。")

def main():
    print("GitHub Issuesを取得しています...")
    issues = fetch_all_issues()
    if not issues:
        print("Issuesが取得できませんでした。")
        return

    # Issueのタイトルと本文を結合
    combined_text = " ".join(
        issue.get("title", "") + " " + issue.get("body", "")
        for issue in issues if "pull_request" not in issue
    )

    print("MeCabで形態素解析を行い、名詞を抽出します...")
    processed_text = mecab_tokenizer(combined_text)

    print("ストップワードを読み込んでいます...")
    stopwords = load_stopwords("stopwords.txt")  # 外部ファイル stopwords.txt を指定

    print("ワードクラウドを生成しています...")
    generate_wordcloud(processed_text, stopwords)

if __name__ == "__main__":
    main()

