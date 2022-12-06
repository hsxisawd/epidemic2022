import  requests
import json
import pymysql


def get_Data(res,cursor,db):
    C = res['data']['diseaseh5Shelf']['chinaTotal']
    ChinaList=[
            '中国',C["nowConfirm"],C["confirm"],C["confirmAdd"],C["dead"],C["heal"],C["highRiskAreaNum"],C["localWzzAdd"],
            C["nowLocalWzz"],C["mtime"],C["deadAdd"],C["mediumRiskAreaNum"],C["localConfirmAdd"],C["importedCase"],
            C["localConfirm"],C["localWzzAdd"]
        ]
    saveChinaData_to_Mysql(ChinaList,cursor,db)
    for i  in res['data']['diseaseh5Shelf']['areaTree'][0]['children']:
        ProvinceList = [
            i['name'],i['total']['nowConfirm'], i['total']['confirm'], i['today']['local_confirm_add'],
            i['total']['dead'],i['today']['dead_add'], i['total']['heal'], i['adcode'], i['total']['highRiskAreaNum'],
            i['today']['wzz_add'],i['total']['wzz'], i['total']['mtime'], i['total']['mediumRiskAreaNum']
            ,i['today']['local_confirm_add'],i['today']['abroad_confirm_add']
        ]
        saveProvinceData_to_Mysql(ProvinceList,cursor,db)
        for ii in i['children']:
            if ii['today']['wzz_add']=='':
                ii['today']['wzz_add']=0
            CityList=[
                ii['name'],i['name'],ii['total']['nowConfirm'],ii['total']['confirm'],ii['today']['local_confirm_add'],
                ii['total']['dead'],ii['total']['heal'],ii['adcode'],ii['total']['highRiskAreaNum'],ii['today']['wzz_add'],
                ii['total']['wzz'],ii['total']['mtime'],ii['total']['mediumRiskAreaNum']
                  ]
            saveCityData_to_Mysql(CityList,cursor,db)

def saveProvinceData_to_Mysql(l,cursor,db):
    sql = """insert into province_epidemic_tb(Provinc_name, nowConfirm, confirm, confirm_add,
                dead, dead_add, heal, Provinc_adcode,highRiskAreaNum, wzz_add,
                wzz, mtime, mediumRiskAreaNum,local_confirm_add,abroad_confirm_add)
                values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s,%s)"""
    try:
        cursor.execute(sql, (l[0], l[1], l[2], l[3], l[4], l[5], l[6], l[7], l[8], l[9], l[10], l[11], l[12], l[13], l[14]))
        db.commit()
    except Exception as e:
        db.rollback()
        print(e,'saveProvinceData_to_Mysql')

def saveCityData_to_Mysql(l,cursor,db):
    sql = """insert into city_epidemic_tb(
                City_name, Pname, nowConfirm, confirm,
                confirm_add, dead, heal, City_adcode,
                highRiskAreaNum, wzz_add,wzz, mtime, mediumRiskAreaNum)
                values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
    try:
        cursor.execute(sql, (l[0],l[1],l[2],l[3],l[4],l[5],l[6],l[7],l[8],l[9],l[10],l[11],l[12]))
        db.commit()
    except Exception as e:
        db.rollback()
        print(e,"saveCityData_to_Mysql",l[0])

def saveChinaData_to_Mysql(l,cursor,db):
    sql = """insert into china_epidemic_tb(
                Counity_name, nowConfirm,confirm,confirm_add,dead,heal,
                highRiskAreaNum,wzz_add,wzz,mtime,dead_add,mediumRiskAreaNum,
                local_confirm_add, abroad_confirm,local_confirm, localWzzAdd)
                values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s, %s, %s)"""
    try:
        cursor.execute(sql, (l[0],l[1],l[2],l[3],l[4],l[5],l[6],l[7],l[8],l[9],l[10],l[11],l[12],l[13],l[14],l[15]))
        db.commit()
    except Exception as e:
        db.rollback()

def main():
    api = 'https://api.inews.qq.com/newsqa/v1/query/inner/publish/modules/list?modules=localCityNCOVDataList,diseaseh5Shelf'

    headers = {
        'Accept-Encoding': 'deflate',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.42'
    }

    res=requests.get(api,headers=headers).json()

    # with open('data.json','w',encoding='utf-8') as f:
    #     f.write(res)

    db = pymysql.connect(
        host="localhost",
        user="root",
        password="123456",
        port=3306,
        db="2022epidemicdata")
    cursor = db.cursor()
    # with open('data.json', 'r', encoding='utf-8') as f:
    #     res = json.loads(f.read())

    get_Data(res,cursor,db)


if __name__ == "__main__":
        main()