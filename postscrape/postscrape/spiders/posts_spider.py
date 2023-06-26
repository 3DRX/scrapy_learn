import scrapy


class PostsSpider(scrapy.Spider):
    name: str = "posts"
    start_urls: list[str] = [
        "https://www.3drx.top/blog/",
    ]

    def parse(self, response: scrapy.http.Response) -> None:
        page: list[str] = response.url.split("/")[-1]
        filename: str = f"posts-{page}.html"
        with open(filename, "wb") as f:
            f.write(response.body)
            pass
        pass
    pass
