from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello, World!"}


@app.get("/account/{account_number}")
def get_account(account_number: int):
    # Perform some logic to retrieve values for the account
    ramal = "1234"
    serial = "ABCD1234"
    mac = "00:11:22:33:44:55"
    ztp = True
    photo_url = "https://example.com/photo.jpg"

    # Return the values as a dictionary
    return {"ramal": ramal, "serial": serial, "mac": mac, "ztp": ztp, "photo_url": photo_url}
