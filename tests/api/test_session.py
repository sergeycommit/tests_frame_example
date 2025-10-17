import requests
import aiohttp


BASE_URL = "https://petstore.swagger.io/v2"


def upload_image(session):
    # time 0.68
    response = session.post(f"{BASE_URL}/pet/1/uploadImage")
    assert response.status_code == 415
    print("1 ______OK______")


def upload_image2(session):
    # time 0.68
    response = session.post(f"{BASE_URL}/pet/2/uploadImage")
    assert response.status_code == 415
    print("2 ______OK______")

def upload_image3(session):
    # time 0.68
    response = session.post(f"{BASE_URL}/pet/3/uploadImage")
    assert response.status_code == 415
    print("3 ______OK______")

def upload_image4(session):
    # time 0.68
    response = session.post(f"{BASE_URL}/pet/4/uploadImage")
    assert response.status_code == 415
    print("4 ______OK______")


def test():
    with requests.session() as session:
        upload_image(session)
        upload_image2(session)
        upload_image3(session)
        upload_image4(session)
        upload_image(session)
        upload_image2(session)
        upload_image3(session)
        upload_image4(session)
