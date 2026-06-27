import httpx
import trafilatura


def fetch_article(url: str) -> str:
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    with httpx.Client(
        follow_redirects=True,
        timeout=20
    ) as client:

        response = client.get(
            url,
            headers=headers
        )

        response.raise_for_status()

    article = trafilatura.extract(
        response.text,
        include_comments=False,
        include_tables=True,
        include_images=False,
    )

    return article or ""