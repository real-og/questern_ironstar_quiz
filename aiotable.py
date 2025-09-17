import gspread_asyncio
from google.oauth2.service_account import Credentials
from loader import SHEET_LINK
import datetime

link = SHEET_LINK
def get_creds():
    creds = Credentials.from_service_account_file("key.json")
    scoped = creds.with_scopes([
        "https://spreadsheets.google.com/feeds",
        "https://www.googleapis.com/auth/spreadsheets",
        "https://www.googleapis.com/auth/drive",
    ])
    return scoped


agcm = gspread_asyncio.AsyncioGspreadClientManager(get_creds)
async def get_sheet(agcm=agcm):
    agc = await agcm.authorize()
    ss = await agc.open_by_url(link)
    zero_ws = await ss.get_worksheet(0)
    return zero_ws


# async def append_user(id, username, phone_number, name, email, datetime_str):
#     sheet = await get_sheet()
#     await sheet.append_row([str(id), str(username), str(phone_number), str(name), str(email), str(datetime_str)])


async def append_user_strict(datetime_str, id,  username):
    sheet = await get_sheet()
    # Получаем все строки и находим первую действительно пустую
    all_values = await sheet.get_all_values()
    first_empty_row = len(all_values) + 1  # следующая за последней заполненной

    values = [str(datetime_str), str(id), str(username),]
    await sheet.insert_row(values, first_empty_row)


async def update_cell(id, cell_num, value):
    sheet = await get_sheet()
    cell = await sheet.find(str(id))
    if cell is None:
        return
    row_number = cell.row
    await sheet.update_cell(row_number, cell_num, str(value))
    

async def get_row_number(id):
    sheet = await get_sheet()
    cell = await sheet.find(str(id))
    if cell is None:
        return
    return cell.row

async def get_score(id):
    sheet = await get_sheet()
    all_values = await sheet.get_all_values()
    
    needed_row = None
    for row in all_values:
        print(row)
        if row and str(row[1]) == str(id):
            needed_row = row
            break
    sum = 0
    print(needed_row)
    if needed_row:
        for i in range(6, 16):
            sum += int(needed_row[i])
    
    return sum
    
    
