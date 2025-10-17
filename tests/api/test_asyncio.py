import asyncio
import pytest


BASE_URL = "https://petstore.swagger.io/v2"


async def upload_image(session):
    # time 0.68
    async with session.post(f"{BASE_URL}/pet/1/uploadImage") as response:
        assert response.status == 415
        print("1 ______OK______")


async def upload_image2(session):
    # time 0.68
    async with session.post(f"{BASE_URL}/pet/2/uploadImage") as response:
        assert response.status == 415
        print("2 ______OK______")

async def upload_image3(session):
    # time 0.68
    async with session.post(f"{BASE_URL}/pet/3/uploadImage") as response:
        assert response.status == 415
        print("3 ______OK______")

async def upload_image4(session):
    # time 0.68
    async with session.post(f"{BASE_URL}/pet/4/uploadImage") as response:
        assert response.status == 415
        print("4 ______OK______")

async def upload_image0(session):
    # time 0.68
    async with session.post(f"{BASE_URL}/pet/1/uploadImage") as response:
        assert response.status == 415
        print("0 ______OK______")


async def upload_image5(session):
    # time 0.68
    async with session.post(f"{BASE_URL}/pet/2/uploadImage") as response:
        assert response.status == 415
        print("5 ______OK______")

async def upload_image6(session):
    # time 0.68
    async with session.post(f"{BASE_URL}/pet/3/uploadImage") as response:
        assert response.status == 415
        print("6 ______OK______")

async def upload_image7(session):
    # time 0.68
    async with session.post(f"{BASE_URL}/pet/4/uploadImage") as response:
        assert response.status == 415
        print("7 ______OK______")

@pytest.mark.asyncio
async def test_parallel_requests(aiohttp_session):
    """Тест параллельного выполнения API запросов с использованием фикстуры сессии"""
    # Запускаем все запросы параллельно вместо последовательного выполнения
    await asyncio.gather(
        upload_image(aiohttp_session),
        upload_image2(aiohttp_session),
        upload_image3(aiohttp_session),
        upload_image4(aiohttp_session),
        upload_image0(aiohttp_session),
        upload_image5(aiohttp_session),
        upload_image6(aiohttp_session),
        upload_image7(aiohttp_session)
    )
