import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context()
        page = await context.new_page()
        await page.goto("https://www.bing.com/search?q=Accenture+trabalhe+conosco+carreiras", timeout=60000)
        await page.wait_for_timeout(2000)
        await page.screenshot(path="bing_debug.png")
        print("Salvo bing_debug.png")
        html = await page.content()
        with open("bing_debug.html", "w", encoding="utf-8") as f:
            f.write(html)
        await browser.close()

asyncio.run(main())
