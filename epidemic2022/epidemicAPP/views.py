import json
import pandas as pd
from django.shortcuts import render
from .models import Province_epidemic_TB,City_epidemic_TB,China_epidemic_TB
from django.db.models import Sum,Max,Min,Count,Avg
from django.http import  HttpResponse
# Create your views here.

#省份数据
Proc_db=Province_epidemic_TB.objects.all()
Proc_df=pd.DataFrame([i.todict() for i in Proc_db])
#城市数据
City_db=City_epidemic_TB.objects.all()
City_df=pd.DataFrame([i.todict() for i in City_db])

def get_China_data(request):
    China_db=China_epidemic_TB.objects.all()
    China_dict=[i.todict() for i in China_db][0]
    return  HttpResponse(json.dumps(China_dict,ensure_ascii=False))

#全国疫情新增数量前十
def get_province_add_top10_data(requests):
    Proc_df_new=Proc_df
    Proc_df_new['全部新增疫情数']=Proc_df_new['新增确诊人数']+ Proc_df_new['新增无症状']+Proc_df_new['本地新增']+Proc_df_new['境外新增']
    data=Proc_df_new[['省份名称','全部新增疫情数']].sort_values(by='全部新增疫情数',ascending=False)
    data_top10=data.head(10)
    return HttpResponse(json.dumps({
        'Provinc_name':data_top10['省份名称'].tolist(),'data_sort':data_top10['全部新增疫情数'].tolist()
    },ensure_ascii=False))

#全国城市新增疫情数量前十
def get_City_add_top10_data(requests):
    filler_str=['地区待确认','境外输入']
    City_df_new=City_df
    index=City_df_new[City_df_new.城市名称.isin(filler_str)].index.tolist()
    City_df_new.drop(labels=index,axis=0,inplace=True)

    City_df_new['全部新增疫情数']=City_df_new['新增确诊人数']+ City_df_new['新增无症状']
    data=City_df_new[['城市名称','全部新增疫情数','省份名称']].sort_values(by='全部新增疫情数',ascending=False)
    data_top10=data.head(10)
    return HttpResponse(json.dumps({
        'City_name': data_top10['城市名称'].tolist(),
        'Provinc_name':data_top10['省份名称'].tolist(),
        'data_sort':data_top10['全部新增疫情数'].tolist()
    },ensure_ascii=False))

# 全国各省风险地区数据
def get_province_RiskArea(request):
    return HttpResponse(json.dumps({
        'Procvince_name': Proc_df['省份名称'].tolist(),
        'HRiskArea_data': Proc_df['高风险地区'].tolist(),
        'MRiskArea_data': Proc_df['中风险地区'].tolist()
    }, ensure_ascii=False))

# 全国各省城市风险地区数据
def get_province_city_RiskArea(request):
    filler_str=['地区待确认','境外输入']
    Proc_df_new = Proc_df
    City_df_new=City_df
    index=City_df_new[City_df_new.城市名称.isin(filler_str)].index.tolist()
    City_df_new.drop(labels=index,axis=0,inplace=True)
    data_list={}
    Proc_List=[]
    for i in Proc_df_new['省份名称']:
        filler_List=['台湾','澳门','香港']
        if i not in filler_List:
            data=City_df_new.groupby('省份名称')['城市名称','高风险地区','中风险地区'].get_group(i)
            data_list[i]={
               'city_name':data['城市名称'].tolist(),
                'HRiskArea_data': data['高风险地区'].tolist(),
                'MRiskArea_data': data['中风险地区'].tolist(),
            }
            Proc_List.append(i)
    Proc_df_new = Proc_df
    return HttpResponse(json.dumps({'data': data_list,'Proc_data':Proc_List},ensure_ascii=False))

#全国各省各城市疫情情况
def get_province_city_comfirm(request):
    data_Dict={}
    Proc_df_new = Proc_df
    Proc_List = []
    filler_List = ['台湾', '澳门', '香港']
    for i in Proc_df_new['省份名称']:
        if i not in filler_List:
            data_list = []
            data=City_df.groupby('省份名称')['城市名称','新增无症状','无症状数量','当前确诊人数','新增确诊人数','id'].get_group(i)
            for j in range(len(data)):
                data_list.append({
                    'id':data['id'].tolist()[j],
                    'city_name':data['城市名称'].tolist()[j],
                    'add_wzz': data['新增无症状'].tolist()[j],
                    'now_wzz': data['无症状数量'].tolist()[j],
                    'now_confirm': data['当前确诊人数'].tolist()[j],
                    'add_confirm':data['新增确诊人数'].tolist()[j]
                })
            data_Dict[i]=data_list
            Proc_List.append(i)
    return HttpResponse(json.dumps({
            'data': data_Dict,
            'Proc_data':Proc_List
        }, ensure_ascii=False))

#全国各省份各城市新增疫情情况
def get_province_city_add_comfirm(request):
    City_df_new = City_df
    City_df_new['全部新增疫情数'] = City_df_new['新增确诊人数'] + City_df_new['新增无症状']
    data_Dict={}
    Proc_df_new = Proc_df
    filler_List = ['台湾', '澳门', '香港']
    Proc_List=[]
    for i in Proc_df_new['省份名称']:
        if  i not in filler_List:
            data_list = []
            data=City_df_new.groupby('省份名称')['城市名称','全部新增疫情数'].get_group(i)
            for j in range(len(data)):
                data_list.append(
                    {'name':data['城市名称'].tolist()[j],'value':data['全部新增疫情数'].tolist()[j]})
                data_Dict[i]=data_list
            Proc_List.append(i)
    return  HttpResponse(json.dumps(
        {'data': data_Dict,'Proc_data':Proc_List}, ensure_ascii=False))


# 动态地图数据
def  get_map_Data(request):
    type=['累计确诊人数', '当前确诊人数', '新增确诊人数', '新增无症状', '本地新增', '境外新增', '高风险地区','中风险地区']
    data_list={}
    for i in type:
        data = Proc_df[['省份名称',i]].sort_values(by=i, ascending=False)
        data_list[i]=[data['省份名称'].values.tolist(),data[i].values.tolist()]
    return HttpResponse(json.dumps({'type':type,'data_list':data_list}, ensure_ascii=False))


