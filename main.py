import json
from fastapi import FastAPI, HTTPException # type: ignore

with open("pembayaran.json", "r") as read_file:
    data = json.load(read_file)
app = FastAPI()

@app.get('/')
async def root():
    return {"Halo Admin Nyam Yamyam! Selamat Datang di Menu Konfirmasi Pembayaran Tunai"}

@app.get('/pembayaran/{item_id}')
async def read_pembayaran(item_id: int):
    for pembayaran_item in data['pembayaran']:
        if pembayaran_item['idBayar'] == item_id:
            return pembayaran_item
    raise HTTPException(
        status_code=404, detail=f'Item not found'
    )

@app.get('/pembayaran/')
async def read_all_pembayaran():
    return data['pembayaran']

@app.put('/pembayaran/{item_id}')
async def update_status_pembayaran(item_id: int, new_name: str):
    for pembayaran_item in data['pembayaran']:
        if pembayaran_item['idBayar'] == item_id:
            pembayaran_item['status'] = new_name
        read_file.close()    
        with open("pembayaran.json", "w") as write_file:
            json.dump(data, write_file, indent = 4)
        write_file.close()
    return {'Payment Status updated'}