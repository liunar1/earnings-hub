import asyncio
from playwright.async_api import async_playwright

async def get_page():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        await page.goto("https://earningshub.com/earnings-calendar/this-week")
        title = await page.content()
        print(title)
        await browser.close()